# -*- coding:utf-8 -*-

import ray

ray.init()
# ray.init(redis_address="localhost:6379")


@ray.remote
def f(x):
    return x * x


futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))
