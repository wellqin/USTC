import profile
import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    """this algorithm is slow af, mind u"""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def fib2(n):
    r = [0, 1]
    if n < 2:
        return r[n]
    else:
        for i in range(2, n + 1):
            r.append(r[i-1] + r[i-2])
        return r[n]

def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq

def fib_seq2(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq2(n - 1))
    seq.append(fib2(n))
    return seq

# print(fib(3))
# print(fib2(3))
if __name__ == "__main__":
    profile.run('print(fib_seq(30)); print()')
    profile.run('print(fib_seq2(30)); print()')