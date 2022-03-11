import time, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
import textwrap
import hashlib

def show_struct(s):
    print(' tm_year :', s.tm_year)
    print(' tm_mon  :', s.tm_mon)
    print(' tm_mday :', s.tm_mday)
    print(' tm_hour :', s.tm_hour)
    print(' tm_min  :', s.tm_min)
    print(' tm_sec  :', s.tm_sec)
    print(' tm_wday :', s.tm_wday)
    print(' tm_yday :', s.tm_yday)
    print(' tm_isdst:', s.tm_isdst)

@addBreaker
def time_get_clock_info():
    """Implementation details for the clocks vary by platform
    """
    available_clocks = [
        # ('clock', time.clock), # time.clock is deprecated ..
        ('monotonic', time.monotonic),
        ('perf_counter', time.perf_counter),
        ('process_time', time.process_time),
        ('time', time.time),
    ]
    # i confirmed difference between winos64 and macos in the book 
    
    for clock_name, func in available_clocks:
        print(textwrap.dedent('''\
        {name}:
            adjustable      : {info.adjustable}
            implementations : {info.implementation}
            monotonic       : {info.monotonic}
            resolution      : {info.resolution}
            current         : {current}
        ''').format(
            name=clock_name,
            info=time.get_clock_info(clock_name),
            current=func())      
        )

@addBreaker
def time_time_vs_ctime():
    print('the time is      :', time.time())
    print('the time is      :', time.ctime())
    later = time.time() + 15
    print('15 secs from now :', time.ctime(later))

@addBreaker
def time_monotonic():
    start = time.monotonic()
    time.sleep(.1)
    end   = time.monotonic()
    print('start   : {:>9.2f}'.format(start))
    print('end     : {:>9.2f}'.format(end))
    print('span    : {:>9.2f}'.format(end - start))

@addBreaker
def time_clock():
    # data to use to calculate md5 checksums
    data = open(__file__, 'rb').read() # bad practice, no close statement ..
    for i in range(5):
        h = hashlib.sha1()
        print(time.ctime(), '   {:0.3f} {:0.3f}'.format(time.time(), time.clock()))
        for i in range(3_000_000):
            h.update(data)
        cksum = h.digest()
    return

@addBreaker
def time_clock_sleep():
    info_template = '{} - {:0.2f} - {:0.2f}'
    print(info_template.format(time.ctime(), time.ctime(), time.clock()))
    for i in range(3, 0, -1):
        print('Sleeping', i)
        """
        # ! `time.sleep` yields control from the current thread and asks that
        # ! thread to wait for the system to wake it back up.
        # ! if a program has only one thread, this function effectively blocks
        # ! the app so that it does no work
        """
        time.sleep(i)
        print(info_template.format(time.ctime(), time.time(), time.clock()))
    return

@addBreaker
def time_perf_counter():
    # data to use to calculate md5 checksums
    data = open(__file__, 'rb').read() # bad practice, no close statement ..
    loop_start = time.perf_counter()
    for i in range(5):
        iter_start = time.perf_counter()
        h          = hashlib.sha1()
        for i in range(3_000_000):
            h.update(data)
        cksum = h.digest()
        now   = time.perf_counter()
        loop_elapsed = now - loop_start
        iter_elapsed = now - iter_start
        print(time.ctime(), ': {:0.3f} {:0.3f}'.format(iter_elapsed, loop_elapsed))
    return

@addBreaker
def time_struct():
    print('gmtime:')
    # gm shorts for Greenwich Mean Time
    show_struct(time.gmtime())
    print('\nlocaltime:')
    show_struct(time.localtime())
    print('\nmktime:', time.mktime(time.localtime()))

@addBreaker
def time_timezone():
    """
    # ! changing timezone does NOT change the actual time, 
    # ! just the way it is represented. -- smart ass
    """
    def show_zone_info():
        print(' TZ     :', os.environ.get('TZ', '(not set)'))
        print(' tzname :', time.tzname)
        print(' Zone   : {} ({})'.format(time.timezone, (time.timezone / 3_600)))
        print(' DST    :', time.daylight)
        print(' Time   :', time.ctime())
        print()
    print('Default:')
    show_zone_info()
    ZONES = [
        'GMT',
        'Europe/Amsterdam',
    ]
    for zone in ZONES:
        os.environ['TZ'] = zone
        # pylint bug
        time.tzset()
        print(zone, ':')
        show_zone_info()
    return

@addBreaker
def time_strptime_vs_strftime():
    now = time.ctime(1483391847.433716)
    print('Now:', now)
    # string presents time. returns a `time_struct` obj
    parsed = time.strptime(now)
    print('time.strptime({!r})'.format(parsed))
    print('\nParsed:')
    show_struct(parsed)
    # string formats time
    print('\nFormatted:', time.strftime('%a %b %d %H:%M:%S %Y', parsed))
    return










if __name__ == "__main__":
    # time(), monotonic(), perf_counter(), process_time()
    # time_get_clock_info()
    # ctime()
    # time_time_vs_ctime()
    # monotonic()
    # time_monotonic()
    # ! clock() --> deprecated Python >= 3.8
    # time_clock()
    # sleep()
    # time_clock_sleep()
    # perf_counter()
    # time_perf_counter()
    # time components: year, month, day, hour, second, workday, yearday etc
    # time_struct()
    # timezone
    # time_timezone() --> don't run this to mess up office pc
    # strptime() vs strftime()
    time_strptime_vs_strftime()