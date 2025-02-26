HuaweiSwitchCommands = [
    "display current-configuration",  # 当前运行的配置
    "display version",  # 设备版本信息
    "display device manuinfo",  # 设备制造信息
    "display power",  # 电源状态
    "display fan",  # 风扇状态
    "display cpu",  # CPU信息
    "display memory",  # 内存信息
    "display environment",  # 环境信息
    "display vlan",  # VLAN信息
    "display vlan all",  # 所有VLAN信息
    "display ip interface",  # IP接口信息
    "display ip interface brief",  # IP接口简要信息
    "display interface brief",  # 接口简要信息
    "display link-aggregation summary",  # 链路聚合摘要
    "display ospf peer",  # OSPF邻居信息
    "display bgp peer ipv4",  # BGP邻居信息
    "display ip routing-table",  # IP路由表
    "display ip routing-table statistics",  # 路由表统计信息
    "display ip routing-table protocol ospf",  # OSPF路由表
    "display ip routing-table protocol bgp",  # BGP路由表
    "display vrrp",  # VRRP信息
    "display vrrp verbose",  # VRRP详细信息
    "display stp",  # STP信息
    "display stp brief",  # STP简要信息
    "display ntp status",  # NTP状态
    "display logbuffer",  # 日志缓冲区
    "display track all",  # 跟踪所有信息
    "display nqa statistics",  # NQA统计信息
    "display nqa history",  # NQA历史信息
    "display dev manuinfo",  # 设备制造信息
]

    

H3CSwitchCommands = [
    "screen-length disable",  # 取消分页一次性输出
    "display current-configuration",  # 显示设备当前运行的配置信息
    "display saved-configuration",  # 显示设备保存的配置文件内容
    "display boot-loader",  # 显示软件映像文件
    "display clock",  # 显示设备的当前系统时间
    "display version",  # 显示设备的版本信息、启动时间等
    "display environment",  # 显示设备的温度信息
    "display power",  # 显示设备的电源模块状态和供电情况
    "display fan",  # 显示设备风扇的运转状态
    "display cpu-usage",  # 查看CPU的最近5秒、1分钟、5分钟的占用率
    "display cpu history",  # 查看CPU的使用记录
    "display memory",  # 显示内存的总大小和当前占用情况
    "display interface brief",  # 查看接口的基本状态和流量信息
    "display interface",  # 详细查看某个接口的详细信息，包括流量、链路状态等
    "display link-aggregation summary",  # 查看链路聚合组的情况
    "display port trunk",  # 查看参与trunk（端口聚合）的端口信息
    "display ip routing-table",  # 显示设备的IP路由表信息
    "display ospf peer",  # 显示OSPF协议的邻居信息
    "display vrrp",  # 查看虚拟路由冗余协议（VRRP）的配置信息
    "display vrrp statistics",  # 查看VRRP的主备用状态
    "display stp root",  # 查看STP的根桥信息
    "display stp brief",  # 查看STP的简要信息
    "display stp abnormal-port",  # 查看STP中是否有非正常端口
    "display vlan",  # 查看VLAN
    "display vlan brief",  # 查看VLAN接口
    "display ndp",  # 查看邻居信息
    "display ip interface",  # VLAN端口统计信息
    "display lldp neighbor-information",  # 查看邻居信息
    "display arp",  # 查看ARP表
    "display elabel",  # 查看设备的电子标签信息
    "display mac-address",  # 查看设备的MAC地址表
    "display ntp status",  # 查看网络时间协议（NTP）的状态信息
    "display transceiver interface",  # 查看光模块的状态和参数信息
    "reset counters interface",  # 清除接口统计信息
]
