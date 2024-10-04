import sys, decimal
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def decimal_getcontext():
    # ! using override default behaviors to set user-defined behaviors
    # `getcontext()` return scope context obj
    context = decimal.getcontext()
    print(type(context))
    for attr in 'Emax, Emin, capitals, prec, rounding'.split(','):
        print('{:<10} = {}'.format(attr.strip(), getattr(context, attr.strip())))
    print('\nflags    :')
    for flag, val in context.flags.items():
        print('     {}: {}'.format(flag, val))
    print('\ntraps    :')
    for trap, val in context.traps.items():
        print('     {}: {}'.format(trap, val))
    return

@addBreaker
def decimal_ud_precision():
    d = decimal.Decimal('0.123456')
    for i in range(1, 5):
        # simple, straightforward
        decimal.getcontext().prec = i
        print(i, ':', d, d * i)

@addBreaker
def decimal_ud_rounding():
    """ round modes
    ROUND_CEILING
    ROUND_DOWN
    ROUND_FLOOR
    ROUND_HALF_DOWN
    ROUND_HALF_EVEN
    ROUND_HALF_UP
    ROUND_UP
    ROUND_05UP
    """
    context     = decimal.getcontext()
    ROUND_MODES = [
        'ROUND_CEILING',
        'ROUND_DOWN',
        'ROUND_FLOOR',
        'ROUND_HALF_DOWN',
        'ROUND_HALF_EVEN',
        'ROUND_HALF_UP',
        'ROUND_UP',
        'ROUND_05UP',
    ]
    header_fmt = '{:10}' + ' '.join(['{:^8}'] * 6) 
    print(header_fmt.format(
        ' ',
        '1/8 (1)', '-1/8 (1)',
        '1/8 (2)', '-1/8 (2)',
        '1/8 (3)', '-1/8 (3)',
    ))
    for round_mode in ROUND_MODES:
        print('{:10}'.format(round_mode.partition('_')[-1]), end=' ')
        for precision in [1, 2, 3]:
            context.prec     = precision
            context.rounding = getattr(decimal, round_mode)
            value            = decimal.Decimal(1) / decimal.Decimal(8)
            print('{:^8}'.format(value), end=' ')
            value            = decimal.Decimal(-1) / decimal.Decimal(8)
            print('{:^8}'.format(value), end=' ')
        print()
    return

@addBreaker
def decimal_context_manager():
    # ! nice 
    with decimal.localcontext() as c:
        c.prec = 2
        c.rounding = decimal.ROUND_FLOOR
        print('local precision:', c.prec)
        print('3.14 / 3 =', decimal.Decimal('3.14') / 3)
    print()
    print('default precision:', decimal.getcontext().prec)
    print('3.14 / 3 =', decimal.Decimal('3.14') / 3)
    return

@addBreaker
def decimal_per_instance_context():
    # set up a context with limited precision
    c = decimal.getcontext()
    c.prec = 3

    # create a constant using the instance c
    pi = c.create_decimal('3.1415')

    # the constant value is rounded off
    print('PI       :', pi)
    # the result of using the constant uses the global context
    print('RESULT   :', decimal.Decimal('2.01') * pi)
    return

@addBreaker
def decimal_thread_context():
    import threading, queue
    
    class Multiplier(threading.Thread):
        def __init__(self, a, b, prec, q):
            self.a    = a
            self.b    = b
            self.prec = prec
            self.q    = q
            threading.Thread.__init__(self)
        def run(self):
            c = decimal.getcontext().copy()
            c.prec = self.prec
            # ! pairs as always, getcontext() vs setcontext()
            decimal.setcontext(c)
            self.q.put((self.prec, self.a * self.b))

    a = decimal.Decimal('3.14')
    b = decimal.Decimal('1.234')
    # a PriorityQueue will return values sorted by precision,
    # no matter in which order the threads finish.
    q = queue.PriorityQueue()
    threads = [Multiplier(a, b, i, q) for i in range(1, 6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    for _ in range(5):
        prec, value = q.get()
        print('{}   {}'.format(prec, value))
    
    return

if __name__ == "__main__":
    decimal_getcontext()
    # user defined precision
    decimal_ud_precision()
    # user defined rounding mode
    decimal_ud_rounding()
    # localcontext
    decimal_context_manager()
    # per instance context
    decimal_per_instance_context()
    # the `global` context is actually thread-local, 
    # so each thread can potentially be configured usinng different values
    decimal_thread_context()