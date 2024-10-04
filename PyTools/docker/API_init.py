"""
-------------------------------------------------
File Name:        API
Author :          wellqin
date:             2020/5/13

首先，docker开放远程访问：
登录docker远程服务,在/usr/lib/systemd/system/docker.service配置远程访问：
# vim /usr/lib/systemd/system/docker.service
[Service] ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock
配置完后，需要重启docker去重新读取配置文件，重新启动docker服务：
# systemctl daemon-reload
# systemctl restart docker
上述步骤都无报错后，就可以对远端服务进行api调用了。
-------------------------------------------------


1.丢弃了python2.6的支持
2.最低支持API版本为1.12(Engine version 1.9.0+)
3.`docker.Client`被替换成`docker.APIClient`
4.`docker.from_env`初始化一个docker客户端实例代替了`APIClient `实例
5.从`APIClient.start`中移除了HostConfig参数
6.开始由之前的docker-py模块变为docker
7.`docker.ssladapter`替换为`docker.transport.ssladapter`

"""
import docker
import json

# 客户端初始化的三种方法
"""
docker.api()
docker.APIClient()
docker.client()  # docker.DockerClient() 其实就是docker.client()的一个子集
                 # docker.from_env() 其实也是docker.client()的一个子集

"""

# 一、初始化客户端
# 1.Docker客户端的初始化工作
"""
Args:
      base_url (str): 指定链接路径，可以通过socket或者tcp方式链接
          ``unix:///var/run/docker.sock`` or ``tcp://127.0.0.1:1234``.
          
      version (str): 指定API使用的版本(docker=2.0.0默认的api版本是1.24,最低支持1.21,docker1.9+的api是1.21),
                     因此在使用python的docker模块时一定要注意docker的api以及docker模块的api是否兼容。
                     当然如果设置为 ``auto`` 将回去自动检测server的版本
      
      timeout (int): 使用API调用的默认超时时间，默认单位为秒
      
      tls (bool or :py:class:`~docker.tls.TLSConfig`): Enable TLS. Pass
          ``True`` to enable it with default options, or pass a
          :py:class:`~docker.tls.TLSConfig` object to use custom
          configuration.
"""
# root  15547   1  0 May10 ?  00:00:00 /usr/bin/dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2375
client = docker.APIClient(base_url="tcp://101.132.140.235:2375", version="1.39", timeout=500)
docker_version = json.dumps(client.version(), indent=1)  # 打印版本信息
print(docker_version)


"""
{
 "Arch": "amd64",
 "KernelVersion": "3.10.0-862.11.6.el7.x86_64",
 "Os": "linux",
 "ApiVersion": "1.39",
 "Version": "18.09.0-ce-beta1",
 "Components": [  # 部件
  {
   "Version": "18.09.0-ce-beta1",
   "Details": {
    "KernelVersion": "3.10.0-862.11.6.el7.x86_64",
    "Experimental": "false",
    "Os": "linux",
    "Arch": "amd64",
    "ApiVersion": "1.39",
    "MinAPIVersion": "1.12",
    "GitCommit": "78a6bdb",
    "BuildTime": "",
    "GoVersion": "go1.10.4"
   },
   "Name": "Engine"
  }
 ],
 "MinAPIVersion": "1.12",
 "GitCommit": "78a6bdb",
 "Platform": {
  "Name": ""
 },
 "GoVersion": "go1.10.4"
}
"""
