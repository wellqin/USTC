# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        子进程
Description :   
Author :          wellqin
date:             2019/9/10
Change Activity:  2019/9/10
-------------------------------------------------
"""
"""
子进程
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
nslookup可以指定查询的类型,可以查到DNS记录的生存时间还可以指定使用哪个DNS服务器进行解释。
在已安装TCP/IP协议的电脑上面均可以使用这个命令。主要用来诊断域名系统 (DNS) 基础结构的信息。
"""
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
"""
$ nslookup www.python.org
��Ȩ��Ӧ��:
������:  mx.ustc.edu.cn
Address:  202.38.64.56

����:    dualstack.python.map.fastly.net
Addresses:  2a04:4e42:12::223
	  151.101.76.223
Aliases:  www.python.org

Exit code: 0
"""


# 如果子进程还需要输入，则可以通过communicate()方法输入：
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
#print(output.decode('utf-8'))
print('Exit code:', p.returncode)
"""
上面的代码相当于在命令行执行命令nslookup，然后手动输入：

set q=mx
python.org
exit
"""