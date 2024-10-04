#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/9/4 19:16
@Author  : qinwei05
"""

import signal
import time
import sys
import os


def handle_int(sig, frame):
    print("get signal: %s, I will quit" % sig)
    sys.exit(0)


def handle_hup(sig, frame):
    print("get signal: %s" % sig)


if __name__ == "__main__":
    signal.signal(2, handle_int)
    signal.signal(1, handle_hup)
    print("My pid is %s" % os.getpid())
    while True:
        time.sleep(3)
