import dis

def fib(n):
    r = [0, 1]
    if n < 2:
        return r[n]
    else:
        for i in range(2, n + 1):
            r.append(r[i-1] + r[i-2])
        return r[n]

# print(fib(3))

if __name__ == "__main__":
    dis.dis(fib)
    dis.show_code(fib)