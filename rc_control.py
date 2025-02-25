"""
rc_control.py

Author: Ryan Zhang
Date: 2025-02-24 21:32:15 UTC+8
Version: B1.0
GitHub: https://github.com/hz157
"""

import re
import time
import paramiko
import logging

def ssh_exec_command(ip: str, username: str, password: str, command: str, port: int = 22, timeout: int = 240) -> str:
    output = ""
    try:
        # 初始化 SSH 客户端并连接
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=password)

        # 激活交互式 shell
        terminal = ssh.invoke_shell()
        terminal.send(f"{command}\n")
        time.sleep(1)  # 初始等待，确保命令开始执行

        start_time = time.time()
        while True:
            # 超时判断
            if time.time() - start_time > timeout:
                logging.error(f"Timeout reached while waiting for command '{command}' to complete on {ip}.")
                break

            # 如果有数据可接收，则读取
            if terminal.recv_ready():
                received_data = terminal.recv(65535).decode('utf-8', errors='ignore')
                output += received_data

                # 如果检测到 "---- More ----" 提示，发送空格键继续输出
                if "---- More ----" in received_data:
                    terminal.send(" ")
                    time.sleep(2.5)
                    continue

            # 等待数据累计
            time.sleep(0.5)

            # 检查最后一行是否为提示符（以 > 或 # 结尾）
            lines = output.strip().splitlines()
            if lines:
                last_line = lines[-1]
                if re.search(r'[>#]\s*$', last_line):
                    break

        ssh.close()
        return output

    except Exception as e:
        return output
