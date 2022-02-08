# -*- coding:utf-8 -*-

# abstract_rate_limit_strategy
import abc
from time import time
from threading import RLock

"""
https://github.com/luengwaiban/rate_limit_collect/blob/master/rate_limit_collect.py
https://github.com/QPromise/rate-limit/blob/master/token_bucket.py
"""

class AbstractRateLimitStrategy(object):
    @abc.abstractmethod
    def execute_rate_limit(self, in_num1, in_num2):
        raise NotImplementedError("Method Not Implement...")


class LeakyBucket(AbstractRateLimitStrategy):

    def __init__(self, capacity, leak_rate, is_lock=False):
        """
        :param capacity:  The total tokens in the bucket.
        :param leak_rate:  The rate in tokens/second that the bucket leaks
        """
        self._capacity = float(capacity)
        self._used_tokens = 0
        self._leak_rate = float(leak_rate)
        self._last_time = time()
        self._lock = RLock() if is_lock else None

    def get_used_tokens(self):
        if self._lock:
            with self._lock:
                return self._get_used_tokens()
        else:
            return self._get_used_tokens()

    def _get_used_tokens(self):
        now = time()
        delta = self._leak_rate * (now - self._last_time)
        self._used_tokens = max(0, self._used_tokens - delta)
        return self._used_tokens

    def _consume(self, tokens):
        if tokens + self._get_used_tokens() <= self._capacity:
            self._used_tokens += tokens
            self._last_time = time()
            return True
        return False

    def consume(self, tokens):
        if self._lock:
            with self._lock:
                return self._consume(tokens)
        else:
            return self._consume(tokens)

    def execute_rate_limit(self, in_num1, in_num2):
        pass


class TokenBucket(AbstractRateLimitStrategy):

    def __init__(self, capacity, fill_rate, is_lock=False):
        """
        : param capacity:  The total tokens in the bucket.
        : param fill_rate:  The rate in tokens/second that the bucket will be refilled
        """
        self._capacity = float(capacity)
        self._tokens = float(capacity)
        self._fill_rate = float(fill_rate)
        self._last_time = time()
        self._is_lock = is_lock
        self._lock = RLock()

    def _get_cur_tokens(self):
        if self._tokens < self._capacity:
            now = time()
            delta = self._fill_rate * (now - self._last_time)
            self._tokens = min(self._capacity, self._tokens + delta)
            self._last_time = now
        return self._tokens

    def get_cur_tokens(self):
        if self._is_lock:
            with self._lock:
                return self._get_cur_tokens()
        else:
            return self._get_cur_tokens()

    def _consume(self, tokens):
        if tokens <= self.get_cur_tokens():
            self._tokens -= tokens
            return True
        return False

    def consume(self, tokens):
        if self._is_lock:
            with self._lock:
                return self._consume(tokens)
        else:
            return self._consume(tokens)

    def execute_rate_limit(self, in_num1, in_num2):
        pass


class RateLimitStrategyContext:

    _strategy = None

    def __init__(self, in_strategy):
        self._strategy = in_strategy

    def execute_strategy(self, in_num1, in_num2):
        return self._strategy.do_operation(in_num1, in_num2)


rate_limit_strategy = RateLimitStrategyContext(in_strategy=TokenBucket())
rate_limit_strategy.execute_strategy()

