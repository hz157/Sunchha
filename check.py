"""
check.py

Author: Ryan Zhang
Date: 2025-02-25 22:32:15 UTC+8
Version: B1.0
GitHub: https://github.com/hz157
"""
from command import HuaweiSwitchCommand
from file_handle import write_to_txt
from rc_control import ssh_exec_command

# ANSI 颜色定义
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_BLUE = "\033[94m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"


def check_all(device):
    if device.get("brand") == "HUAWEI":
        for command in HuaweiSwitchCommand:
            try:
                # 通知用户当前执行的命令
                print(f"{COLOR_BLUE}🚀 正在执行命令: {command} on {device.get('ip')}{COLOR_RESET}")
                
                # 执行SSH命令获取输出数据
                data = ssh_exec_command(
                    ip=device.get("ip"),
                    username=device.get("username"),
                    password=device.get("password"),
                    command=str(command),
                    port=device.get("port")
                )
                # 构造文件路径（例如：./output/192.168.1.1/display version.txt）
                file_path = f"./output/{device.get('ip')}/{str(command)}.txt"
                if write_to_txt(file_path=file_path, content=data):
                    print(f"{COLOR_GREEN}✅ {device.get('ip')} 执行 {command} 回显已写入文件：{file_path}{COLOR_RESET}")
                else:
                    print(f"{COLOR_RED}❌ {device.get('ip')} 执行 {command} 回显写入失败：{file_path}{COLOR_RESET}")
            except Exception as e:
                print(f"{COLOR_RED}❌ Error executing {command}: {e}{COLOR_RESET}")


def check_specify(device):
    commands = device.get("command")
    if commands:
        for command in commands.split("\n"):
            command = command.strip()
            if not command:
                continue  # 跳过空行
            try:
                # 通知用户当前执行的命令
                print(f"{COLOR_BLUE}🚀 正在执行命令: {command} on {device.get('ip')}{COLOR_RESET}")
                
                data = ssh_exec_command(
                    ip=device.get("ip"),
                    username=device.get("username"),
                    password=device.get("password"),
                    command=command,
                    port=device.get("port")
                )
                file_path = f"./output/{device.get('ip')}/{command}.txt"
                if write_to_txt(file_path=file_path, content=data):
                    print(f"{COLOR_GREEN}✅ {device.get('ip')} 执行 {command} 回显已写入文件：{file_path}{COLOR_RESET}")
                else:
                    print(f"{COLOR_RED}❌ {device.get('ip')} 执行 {command} 回显写入失败：{file_path}{COLOR_RESET}")
            except Exception as e:
                print(f"{COLOR_RED}❌ Error executing {command}: {e}{COLOR_RESET}")

