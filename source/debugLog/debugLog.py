#!/usr/bin/python3

import logging
import logging.config

# 采用配置文件
logging.config.fileConfig("/mnt/hgfs/source/AutoPush/AutoPush/source/debugLog/resource/logging.conf")
# 获取普通用户记录日志角色
logger = logging.getLogger("logUser")

# 打印函数
def debuglog(sysinfo):
    logger.debug(sysinfo)

