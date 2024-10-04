# -*- coding:utf-8 -*-

import redis


class RedisPool:
    """
    redis连接池
    """
    _redis_pool = {}

    def __init__(self):
        self.config = {
            'default': {
                'host': '127.0.0.1',
                'port': 6379,
                'db': 0
            }
        }

    def get_instance(self, redis_name='default'):
        """
        单例模式 # 可增加一个名字参数，根据该参数加载对应的配置
        :return:
        """
        if not self.config.get(redis_name):
            return None

        host = self.config.get(redis_name).get('host')
        port = self.config.get(redis_name).get('port')
        db = self.config.get(redis_name).get('db')

        key = host + str(port)
        if not RedisPool.redis.get(key):
            if not host:
                raise IOError('error: host is null!')
            try:
                port = int(port)
            except:
                raise TypeError('error: port must be integer!')

            try:
                RedisPool.redis[key] = redis.StrictRedis(host=host, port=port, db=db)
            except:
                raise IOError('error: connect error!')

        return RedisPool.redis.get(key)


if __name__ == '__main__':
    host = '10.60.81.83'
    password = ''
    r = RedisPool.get_instance(host)
    r.hset('key', 'a', 'b')
    print(r.hget('key', 'a'))
