# -*- coding:utf-8 -*-

import time
import func_timeout
from func_timeout import func_set_timeout
import threading
from queue import Queue

# https://www.python-china.com/html/206.html


@func_set_timeout(5)  # 设置最大运行时间
def test_time_out(num):
    for i in range(num):
        time.sleep(1)


class DoUrl(threading.Thread):
    def __init__(self, p_name, q_list):
        threading.Thread.__init__(self, name=p_name)
        self.data = q_list

    def run(self):
        while True:
            try:
                num = self.data.get()
                try:
                    test_time_out(num)
                    print('test_time_out({})程序正常执行完成'.format(num))
                except func_timeout.exceptions.FunctionTimedOut:
                    print('test_time_out({})程序超时,退出'.format(num))
                print('还有队列{}个'.format(self.data.qsize()))
                if self.data.qsize() == 0:
                    print('线程{}完成'.format(self.getName()))
                    break
            except Exception as e:
                print(e)
                break
        return None


if __name__ == '__main__':
    q_list = Queue()
    for i in range(10):
        q_list.put(i)
    for i in range(0, 3):
        # 对象实例化
        do_url_threading = DoUrl('线程' + str(i), q_list)  # 加入队列线程
        # 启动线程
        do_url_threading.start()
