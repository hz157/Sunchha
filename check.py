import os
from command import H3CSwitchCommands, HuaweiSwitchCommands
from file_handle import write_to_txt
from rc_control import ssh_exec_command

# ANSI 颜色定义
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_BLUE = "\033[94m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"



def execute_commands(device, commands):
    """执行设备的命令列表，并保存输出"""
    for command in commands:
        if not command:
            continue  # 跳过空行

        try:
            # 通知用户当前执行的命令
            print(f"{COLOR_BLUE}🚀 正在执行命令: {command} on {device.get('ip')}{COLOR_RESET}")

            # 执行 SSH 命令
            data = ssh_exec_command(
                ip=device.get("ip"),
                username=device.get("username"),
                password=device.get("password"),
                command=command,
                port=device.get("port")
            )

            if data == "SSH_CONNECTION_FAILED":
                print(f"{COLOR_RED}❌ 设备 {device.get('ip')} 连接失败，跳过当前设备{COLOR_RESET}")
                return  # 连接失败，跳过后续命令

            # 构造文件路径（例如：./output/192.168.1.1/display version.txt）
            output_dir = os.path.join("output", device.get("ip"))
            os.makedirs(output_dir, exist_ok=True)
            file_path = os.path.join(output_dir, f"{command}.txt")

            # 写入文件
            if write_to_txt(file_path=file_path, content=data):
                print(f"{COLOR_GREEN}✅ {device.get('ip')} 执行 {command} 回显已写入文件：{file_path}{COLOR_RESET}")
            else:
                print(f"{COLOR_RED}❌ {device.get('ip')} 执行 {command} 回显写入失败：{file_path}{COLOR_RESET}")

        except Exception as e:
            print(f"{COLOR_RED}❌ 设备 {device.get('ip')} 执行 {command} 发生错误: {e}{COLOR_RESET}")


def full_query(device):
    """检查设备品牌并执行默认命令"""
    brand = device.get("brand")
    if brand not in ["HUAWEI", "H3C"]:
        print(f"{COLOR_RED}⚠️ 不支持的设备品牌: {brand}{COLOR_RESET}")
        return
    if brand == "HUAWEI":
        commands = HuaweiSwitchCommands
    elif brand == "H3C":
        commands = H3CSwitchCommands
    execute_commands(device, commands)

def auto_match(device):
    if device.get("command") is None:
        full_query(device=device)
    else:
        commands = device.get("command", "").split("\n")
        execute_commands(device, commands)

