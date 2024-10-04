# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        introduce
Description :   
Author :          wellqin
date:             2020/4/5
Change Activity:  2020/4/5
-------------------------------------------------
"""


# 设计模式七大原则


# 单一职责原则，简单地说，就是一个类负责一项职责。
# 现有一Log类原本只有单个职责“离线收集日志”，现在新增需求希望给日志做实时大数据分析

class Log(object):
    def __init__(self):
        pass

    def collect(self, log_dir):  # 离线收集日志
        print("Collecting the log files under {} offline.".format(log_dir))

    # 新增需求希望给日志做实时大数据分析
    # 这样写是不好的 NOT Perfect
    # def LogOnlineAnalysis(self, log_dir):
    #     pass


class LogOnlineAnalysis(object):
    def __init__(self):
        pass

    # Perfect 单一职责原则
    def analyze(self, log_dir):
        print("Analyzing the log files under {}. online.".format(log_dir))


class Client(object):
    def __init__(self):
        pass

    def act(self):
        log = Log()
        log.collect("C:\\logs\\")
        log.collect("/opt/logs")

        # Perfect 单一职责原则
        print("=================================================")
        analysis = LogOnlineAnalysis()
        analysis.analyze("C:\\logs\\")
        analysis.analyze("/opt/logs")


if __name__ == '__main__':
    client = Client()
    client.act()  # 原来调用不变act内新增实现
