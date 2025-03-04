import os
import platform
import subprocess
from check import auto_match, full_query
from file_handle import read_target_info
from update.update import Updater
from color import *

VERSION = "v1.0.0"
RELEASEDATE = "2025-03-04"
PLATFORM = None

    
def clear_console():
    """ 清空控制台 """
    global PLATFORM
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
        PLATFORM = "Windows"
    elif system_name in ["Linux", "Darwin"]:
        os.system("clear")
        PLATFORM = "Linux"

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
        Version: {version}   Release Date: {release_date}
    """.format(version=VERSION, release_date=RELEASEDATE) + COLOR_RESET)


def menu():
    """ 显示菜单并处理用户输入 """
    options = {
        "1": lambda: check_devices(auto_match, "🔍 开始自动匹配..."),
        "2": lambda: check_devices(full_query, "🔍 开始全量自检...")
    }

    while True:
        print(COLOR_GREEN + """
        请选择要执行的操作：
        1. 自动匹配 (自动匹配Excel当中的command列)
        2. 全量自检
        q. 退出
        """ + COLOR_RESET)
        
        choice = input(COLOR_YELLOW + "请输入选项，默认1 (1/2/q): " + COLOR_RESET).strip().lower()

        if choice == "q":
            print(COLOR_RED + "程序已退出。" + COLOR_RESET)
            break
        options.get(choice, options["1"])()  # 默认执行自动匹配


def check_devices(check_func, start_msg):
    """ 通用设备检查函数，执行不同类型的巡检 """
    print(COLOR_BLUE + start_msg + COLOR_RESET)
    try:
        targets = read_target_info()
        if not targets:
            print(COLOR_YELLOW + "⚠️ 未找到任何设备信息，请检查目标文件。" + COLOR_RESET)
            return

        for item in targets:
            if "SSH" in item.get("protocol", ""):
                print(f"🖥️ 正在检查设备: {item.get('ip')} ...")
                check_func(item)

        print(COLOR_GREEN + "✅ 检查完成" + COLOR_RESET)

    except Exception as e:
        print(COLOR_RED + f"❌ 发生错误: {e}" + COLOR_RESET)


if __name__ == "__main__":
    welcome()
    menu()
