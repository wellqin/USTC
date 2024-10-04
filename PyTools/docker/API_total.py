"""
-------------------------------------------------
File Name:        API_total
Author :          wellqin
date:             2020/5/13
-------------------------------------------------
"""
import docker

# docker包 ==> docker-py
# https://docker-py.readthedocs.io/en/stable/images.html#

# https://docker-py.readthedocs.io/en/stable/
# https://github.com/docker/docker-py -- Git源码


client = docker.APIClient(base_url="tcp://101.132.140.235:2375", version="1.39", timeout=500)
print(client.containers())
