import os
import platform
from check import check_all, check_specify
from file_handle import read_target_info

# ANSI 颜色代码
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_CYAN = "\033[96m"
COLOR_RESET = "\033[0m"

def clear_console():
    """ 清空控制台 """
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    elif system_name in ["Linux", "Darwin"]:
        os.system("clear")

def welcome():
    """ 显示欢迎信息 """
    clear_console()
        # 免责声明
    print(COLOR_RED + """
⚠️ 免责声明：
本自动化程序仅建议用于进行巡检操作，并不建议使用此自动化程序进入使能模式执行配置命令等高危操作。
如使用该程序执行自动化配置命令造成的网络中断后果，请自行负责！
""" + COLOR_RESET)
    
    print(COLOR_CYAN + r"""
     ____                       _      _            
    / ___|  _   _  _ __    ___ | |__  | |__    __ _ 
    \___ \ | | | || '_ \  / __|| '_ \ | '_ \  / _` |
     ___) || |_| || | | || (__ | | | || | | || (_| |
    |____/  \__,_||_| |_| \___||_| |_||_| |_| \__,_|

        Github Repo: https://github.com/hz157/Sunchha  
        Version: B1.0   Release Date: 2025-02-25
    """ + COLOR_RESET)


def menu():
    """ 显示菜单并处理用户输入 """
    while True:
        print(COLOR_GREEN + """
        请选择要执行的操作：
        1. 全量自检 (执行内置的所有巡检命令)
        2. 指定检查 (请将检查命令放置在目标excel当中)
        q. 退出
        """ + COLOR_RESET)
        
        choice = input(COLOR_YELLOW + "请输入选项 (1/2/q): " + COLOR_RESET).strip()
        
        if choice == "1":
            full_check()
        elif choice == "2":
            specific_check()
        elif choice == "q" or choice == "Q":
            print(COLOR_RED + "程序已退出。" + COLOR_RESET)
            break
        else:
            print(COLOR_RED + "❌ 无效输入，请重新选择！" + COLOR_RESET)

def full_check():
    """ 对所有设备进行全量检查 """
    print(COLOR_BLUE + "🔍 开始全量自检..." + COLOR_RESET)
    try:
        targets = read_target_info()
        if not targets:
            print(COLOR_YELLOW + "⚠️ 未找到任何设备信息，请检查目标文件。" + COLOR_RESET)
            return

        for item in targets:
            if "SSH" in item.get("protocol"):
                print(f"🖥️ 正在检查设备: {item.get('ip')} ...")
                check_all(item)

        print(COLOR_GREEN + "✅ 全量检查完成！" + COLOR_RESET)

    except Exception as e:
        print(COLOR_RED + f"❌ 发生错误: {e}" + COLOR_RESET)

def specific_check():
    """ 允许用户指定检查命令进行检查 """
    try:
        targets = read_target_info()
        if not targets:
            print(COLOR_YELLOW + "⚠️ 未找到任何设备信息，请检查目标文件。" + COLOR_RESET)
            return

        print(COLOR_BLUE + "🔍 开始指定检查..." + COLOR_RESET)
        for idx, item in enumerate(targets, start=1):
            print(f"{idx}. {item.get('ip')}")

        for item in targets:
            if "SSH" in item.get("protocol"):
                print(f"🖥️ 正在检查设备: {item.get('ip')} ...")
                check_specify(item)

        print(COLOR_GREEN + "✅ 指定检查完成！" + COLOR_RESET)

    except Exception as e:
        print(COLOR_RED + f"❌ 发生错误: {e}" + COLOR_RESET)

if __name__ == "__main__":
    welcome()
    menu()
