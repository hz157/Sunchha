import paramiko
import time
import re
import logging

def ssh_exec_command(ip: str, username: str, password: str, command: str, port: int = 22, timeout: int = 240) -> str:
    output = ""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # 连接 SSH
        ssh.connect(hostname=ip, port=port, username=username, password=password, allow_agent=False, look_for_keys=False)
    except Exception as e:
        print(f"❌ SSH Error: {e}")
        return "SSH_CONNECTION_FAILED"
    
    try:
        # 激活交互式 shell
        terminal = ssh.invoke_shell()
        terminal.send(f"{command}\n")
        time.sleep(1)  # 初始等待，确保命令开始执行

        start_time = time.time()
        while True:
            # 超时判断
            if time.time() - start_time > timeout:
                logging.error(f"⏳ Timeout reached while executing '{command}' on {ip}.")
                break

            # 读取可用数据
            if terminal.recv_ready():
                received_data = terminal.recv(65535).decode('utf-8', errors='ignore')
                output += received_data

                # 处理分页
                if "---- More ----" in received_data:
                    terminal.send(" ")
                    time.sleep(2.5)
                    continue

            # 短暂等待，减少 CPU 占用
            time.sleep(0.5)

            # 检查是否返回到 CLI 提示符（通常以 `>` 或 `#` 结尾）
            lines = output.strip().splitlines()
            if lines and re.search(r'[>#]\s*$', lines[-1]):
                break

    except Exception as e:
        return output
    finally:
        ssh.close()

    return output

