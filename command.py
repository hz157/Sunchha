"""
command.py

Author: Ryan Zhang
Date: 2025-02-24 21:13:15 UTC+8
Version: B1.0
GitHub: https://github.com/hz157
"""

from enum import Enum
from typing import Protocol

class Commands(Protocol):
    def __str__(self) -> str:
        ...

class HuaweiSwitchCommand(Enum):
    DISPLAY_CONFIG = "display current-configuration"
    DISPLAY_VERSION = "display version"
    DISPLAY_DEVICE_INFO = "display device manuinfo"
    DISPLAY_POWER = "display power"
    DISPLAY_FAN = "display fan"
    DISPLAY_CPU = "display cpu"
    DISPLAY_MEMORY = "display memory"
    DISPLAY_ENV = "display environment"
    DISPLAY_VLAN = "display vlan"
    DISPLAY_VLAN_ALL = "display vlan all"
    DISPLAY_IP_INTERFACE = "display ip interface"
    DISPLAY_IP_INTERFACE_BRIEF = "display ip interface brief"
    DISPLAY_INTERFACE_BRIEF = "display interface brief"
    DISPLAY_LAG_SUMMARY = "display link-aggregation summary"
    DISPLAY_OSPF_PEER = "display ospf peer"
    DISPLAY_BGP_PEER = "display bgp peer ipv4"
    DISPLAY_ROUTING_TABLE = "display ip routing-table"
    DISPLAY_ROUTING_TABLE_STATS = "display ip routing-table statistics"
    DISPLAY_ROUTING_TABLE_OSPF = "display ip routing-table protocol ospf"
    DISPLAY_ROUTING_TABLE_BGP = "display ip routing-table protocol bgp"
    DISPLAY_VRRP = "display vrrp"
    DISPLAY_VRRP_VERBOSE = "display vrrp verbose"
    DISPLAY_STP = "display stp"
    DISPLAY_STP_BRIEF = "display stp brief"
    DISPLAY_NTP_STATUS = "display ntp status"
    DISPLAY_LOGBUFFER = "display logbuffer"
    DISPLAY_TRACK_ALL = "display track all"
    DISPLAY_NQA_STATS = "display nqa statistics"
    DISPLAY_NQA_HISTORY = "display nqa history"
    DISPLAY_DEV_MANUINFO = "display dev ma"

    def __str__(self):
        """返回枚举的值，使其默认转换为字符串"""
        return self.value

    @classmethod
    def list_commands(cls):
        """返回所有命令的字符串列表"""
        return [str(command) for command in cls]
    