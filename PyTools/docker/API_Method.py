"""
-------------------------------------------------
File Name:        API_Method
Author :          wellqin
date:             2020/5/13
-------------------------------------------------

2.Docker客户端的具体方法

docker相关的方法使用: 使用DockerClient对象，会有以下方法：
    client.api,
    client.containers,
    client.events,
    client.from_env,
    client.images,
    client.info,
    client.login,
    client.networks,
    client.nodes,
    client.ping,
    client.services,
    client.swarm,
    client.version,
    client.volumes,


输出docker的相关信息，相当于docker info
    client.info()
"""

from PyTools.docker import API_init

# 二、api方法使用示例
# 1. login方法定义
"""
client.login()

login(*args, **kwargs) method of docker.client.DockerClient instance

    Authenticate with a registry. Similar to the ``docker login`` command.
    
    Args:
        username (str): The registry username
        password (str): The plaintext password
        email (str): The email for the registry account
        registry (str): URL to the registry.  E.g.``https://index.docker.io/v1/``
        reauth (bool): Whether refresh existing authentication on the Docker server.
        dockercfg_path (str): Use a custom path for the ``.dockercfg`` file
                              (default ``$HOME/.dockercfg``)
    
    Returns:返回的错误日志信息
        (dict): The response from the login request
        Raises::py:class:`docker.errors.APIError` If the server returns an error.
"""

client = API_init.client
# return {'IdentityToken': '', 'Status': 'Login Succeeded'}
# print(client.login(email="1050346754@qq.com", password="123qinwei123", username="1050346754@qq.com",
#                    registry="registry.cn-shanghai.aliyuncs.com"))  # email可选项


# 2.images 类定义

"""
    List images. Similar to the ``docker images`` command.
    Args:
        name (str): Only show images belonging to the repository ``name``
        quiet (bool): Only return numeric IDs as a list.
        all (bool): Show intermediate image layers. By default, these are
            filtered out.
        filters (dict): Filters to be processed on the image list.
            Available filters:
            - ``dangling`` (bool)
            - `label` (str|list): format either ``"key"``, ``"key=value"``
                or a list of such.
    
    Returns:
        (dict or list): A list if ``quiet=True``, otherwise a dict.
    
    Raises:
        :py:class:`docker.errors.APIError` If the server returns an error.
        
    # 源码
    def images(self, name=None, quiet=False, all=False, filters=None)
        params = {
            'filter': name,
            'only_ids': 1 if quiet else 0,
            'all': 1 if all else 0,
        }
        if filters:
            params['filters'] = utils.convert_filters(filters)
        res = self._result(self._get(self._url("/images/json"), params=params),
                           True)
        if quiet:
            return [x['Id'] for x in res]
        return res
"""
# def images(self, name=None, quiet=False, all=False, filters=None)
# quiet=True：sha256值  all=True：表示忽略中间镜像层
# filters它需要一个dict：过滤器(dict) -- "dangling": True 表示找出无用的
print(client.images(name="ssh_docker_python38:latest", all=True, filters={"dangling": False}))
"""
[
  {
    "Size": 998441788,
    "Id": "sha256:0f5a163e727010f75efe45497fb23b402a058d3e53656680b360e59968e42890",
    "VirtualSize": 998441788,
    "RepoDigests": [
      "registry.cn-shanghai.aliyuncs.com/wellqin/software@sha256:9ade55d3012a1f416953efc1a8902077e7a84760f19fc8c588ea9954a0cc4176"
    ],
    "Created": 1588699571,
    "SharedSize": -1,
    "ParentId": "sha256:6f619c4c3ce481b4c5ba82e07f88935182510e41046afe00e0d0f9c2e93b4ed4",
    "RepoTags": [
      "ssh_docker_python38:latest",
      "registry.cn-shanghai.aliyuncs.com/wellqin/software:V1.0"
    ],
    "Containers": -1,
    "Labels": {
      "maintainer": "wellqin",
      "org.label-schema.schema-version": "1.0",
      "org.label-schema.name": "CentOS Base Image",
      "org.label-schema.build-date": "20180804",
      "org.label-schema.vendor": "CentOS",
      "org.label-schema.license": "GPLv2"
    }
  },
  ......
]
"""

# 3.docker管理容器相关
"""
containers类，下面有相关的方法：

    containers: List containers. Similar to the ``docker ps`` command.
    
    
    
    
    
"""
"""
def containers(self, quiet=False, all=False, trunc=False, latest=False,
                   since=None, before=None, limit=-1, size=False,
                   filters=None):
"""
print(client.containers)

# 一个完整的创建容器的例子
# Command line:  docker run -itd -P --cpuset_cpus='0,1' --cpu_shares=2 --cpu_period=10000 --hostname=xxbandy
# --mem_limit=512m --net=none --oom_kill_disable=True -P -u admin busybox /bin/sh
"""
Python API:
c1 = C.containers.run('busybox',command='/bin/sh',name='xxb-test',detach=True,tty=True,stdin_open=True,cpuset_cpus='0,1',cpu_shares=2,cpu_period=10000,hostname='xxbandy',mem_limit='512m',network_mode='none',oom_kill_disable=True,publish_all_ports=True,user='root')

查看容器相关信息：
容器id，64位的字符
In [20]: c1.id
Out[20]: '499db0824206d61d09db2f36c70aa84bdb1a4b6d508b001a618d2010a23fea7e'


c1.logs 
c1.name      获取容器名信息
c1.reload
c1.remove    删除容器信息，相当于docker rm 参数：c1.remove(v=True,link=True,force=True)
c2.rename    重命名容器名，相当于docker renmame oldname newname
c1.resize    设置tty session信息
c1.restart   重启容器信息
c1.start     启动容器信息
c1.stats     容器状态

c1.update    动态调整容器内部信息（blkio_weight，cpu_period，cpu_quota，cpu_shares，cpuset_cpus，
                                cpuset_mems，mem_limit，mem_reservation）
    Args:
        blkio_weight (int): 块IO权重比例（10-100）
        cpu_period (int): 限制cpu公平调度周期
        cpu_quota (int): 限制cpu公平调度配额
        cpu_shares (int): 设置cpu共享权重
        cpuset_cpus (str): 指定cpu执行(0-3, 0,1)
        cpuset_mems (str): 指定cpu内存的执行(0-3, 0,1)
        mem_limit (int or str): 内存限制
        mem_reservation (int or str): 内存软限制
        memswap_limit (int or str): swap限制总的可使用内存限制(memory + swap)，-1表示关闭swap
        kernel_memory (int or str): 内核内存限制
        restart_policy (dict): 重启策略
"""

