"""
Table of strptime/strftime Format codes

+--------+----------------------------------------+----------------------------+
| Symbol | Meaning                                | Example                    |
+========+========================================+============================+
| %a     | Abbreviated weekday name               | 'Wed'                      
+--------+----------------------------------------+----------------------------+
| %A     | Full weekday name                      | 'Wednesday'                |
+--------+----------------------------------------+----------------------------+
| %w     | Weeknum: 0(Sunday) throu 6(Staturday)  | '3'                        |
+--------+----------------------------------------+----------------------------+
| %d     | day                                    | '13'                       |
+--------+----------------------------------------+----------------------------+
| %b     | Abbreviated month name                 | 'Jan'                      |                    
+--------+----------------------------------------+----------------------------+
| %B     | Full month name                        | 'January'                  |                 
+--------+----------------------------------------+----------------------------+
| %m     | month                                  | '01'                       |  
+--------+----------------------------------------+----------------------------+
| %y     | year w/o century                       | '16'                       |            
+--------+----------------------------------------+----------------------------+
| %Y     | year w/ century                        | '2016'                     |            
+--------+----------------------------------------+----------------------------+
| %H     | hour (24-hour clock)                   | '17'                       |                
+--------+----------------------------------------+----------------------------+
| %I     | hour (12-hour clock)                   | '05'                       |                 
+--------+----------------------------------------+----------------------------+
| %p     | AM/PM                                  | 'PM'                       |  
+--------+----------------------------------------+----------------------------+
| %M     | minutes                                | '00'                       |   
+--------+----------------------------------------+----------------------------+
| %S     | seconds                                | '00'                       |   
+--------+----------------------------------------+----------------------------+
| %f     | microseconds                           | '000000'                   |             
+--------+----------------------------------------+----------------------------+
| %z     | UTC offsetfor timezone obj             | '-0500'                    |                          
+--------+----------------------------------------+----------------------------+
| %Z     | Time zone name                         | 'EST'                      |            
+--------+----------------------------------------+----------------------------+
| %j     | Day of the year                        | '013'                      |            
+--------+----------------------------------------+----------------------------+
| %W     | Week of the year                       | '02'                       |             
+--------+----------------------------------------+----------------------------+
| %c     | Date and Time (current locale)         | 'Wen Jan 13 17:00:00 2016' |                                                
+--------+----------------------------------------+----------------------------+
| %x     | Date (current locale)                  | '01/13/16'                 |                        
+--------+----------------------------------------+----------------------------+
| %X     | Time (current locale)                  | '17:00:00'                 |                        
+--------+----------------------------------------+----------------------------+
| %%     | A literal % char                       | '%'                        |            
+--------+----------------------------------------+----------------------------+

"""

import datetime, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def datetime_time():
    t = datetime.time(1, 2, 3)
    print(t)
    print('hour       :', t.hour)
    print('minute     :', t.minute)
    print('second     :', t.second)
    print('microsecond:', t.microsecond)
    print('tzinfo     :', t.tzinfo)

@addBreaker
def datetime_time_minmax():
    # 24-hour
    print('Earliest  :', datetime.time.min)
    print('Latest    :', datetime.time.max)
    print('Resolution:', datetime.time.resolution)

@addBreaker
def datetime_time_resolution():
    for m in [1, 0, 0.1, 0.6]:
        try:
            print('{:02.1f} :'.format(m),
                datetime.time(0, 0, 0, microsecond=m)
            )
        except TypeError as err:
            print('ERROR:', err)
    return

@addBreaker
def datetime_date():
    today = datetime.date.today()
    print(today)
    print('ctime    :', today.ctime())
    # timetuple() is an obj similar with time_struct() in time module
    tt = today.timetuple()
    print('tuple    : tm_year =', tt.tm_year)
    print('         : tm_mon =', tt.tm_mon)
    print('         : tm_mday =', tt.tm_mday)
    print('         : tm_hour =', tt.tm_hour)
    print('         : tm_min =', tt.tm_year)
    print('         : tm_sec =', tt.tm_sec)
    print('         : tm_wday =', tt.tm_wday)
    print('         : tm_yday =', tt.tm_yday)
    print('         : tm_isdst =', tt.tm_isdst)
    print('ordinal  :', today.toordinal())
    print('Year     :', today.year)
    print('Mon      :', today.month)
    print('Day      :', today.day)
    return

@addBreaker
def datetime_date_fromordinal_vs_fromtimestamp_vs_replace():
    import time
    o = 733_114
    print('o                :', o)
    print('fromordinal(o)   :', datetime.date.fromordinal(o))
    t = time.time()
    print('t                :', t)
    print('fromtimestamp(t) :', datetime.date.fromtimestamp(t))
    # another way to create a new `date` instances is to 
    # use the `replace()` method of an existing date
    d1 = datetime.date(2020, 8, 13)
    print('d1:', d1.ctime())
    d2 = d1.replace(year=2021)
    print('d2:', d2.ctime())
    return

@addBreaker
def datetime_date_minmax():
    print('Earliest  :', datetime.date.min)
    print('Latest    :', datetime.date.max)
    print('Resolution:', datetime.date.resolution)
    return

@addBreaker
def datetime_timedelta():
    """
    how_many_days = future_date - past_date
    ! calculation methods
    a) future_date, past_date are both `datetime` objects
    b) combines `datetime` object with a `timedelta`
    """
    print('microseconds :', datetime.timedelta(microseconds=1))
    print('milliseconds :', datetime.timedelta(milliseconds=1))
    print('seconds      :', datetime.timedelta(seconds=1))
    print('minutes      :', datetime.timedelta(minutes=1))
    print('hours        :', datetime.timedelta(hours=1))
    print('days         :', datetime.timedelta(days=1))
    print('weeks        :', datetime.timedelta(weeks=1))
    return

@addBreaker
def datetime_timedelta_total_seconds():
    deltas = [
        datetime.timedelta(microseconds=1),
        datetime.timedelta(milliseconds=1),
        datetime.timedelta(seconds=1),
        datetime.timedelta(minutes=1),
        datetime.timedelta(hours=1),
        datetime.timedelta(weeks=1),
    ]
    for delta in deltas:
        print('{:15} = {:8} seconds'.format(str(delta), delta.total_seconds()))
    return
    
@addBreaker
def datetime_date_math():
    """
    how_many_days = future_date - past_date
    ! calculation methods
    a) future_date, past_date are both `datetime` objects
    b) combines `datetime` object with a `timedelta`
    """
    today     = datetime.date.today()
    one_day   = datetime.timedelta(days=1)
    yesterday = today - one_day
    tomorrow  = today + one_day
    # display
    print('Today    :', today)
    print('One Day  :', one_day)
    print('Yesterday:', yesterday)
    print('Tomorrow :', tomorrow)
    # 
    print()
    print('tomorrow - yesterday = ', tomorrow - yesterday)
    print('yesterday - tomorrow = ', yesterday - tomorrow)
    return

@addBreaker
def datetime_timedelta_math():
    # smart ass .. 
    # you may do arithmetic operations on timedelta obj
    one_day = datetime.timedelta(days=1)
    print('1 day       :', one_day)
    print('5 day       :', one_day * 5)
    print('1.5 day     :', one_day * 1.5)
    print('1/4 day     :', one_day / 4)
    # assume an hour for lunch
    work_day    = datetime.timedelta(hours=7)
    meeting_len = datetime.timedelta(hours=1)
    print('\nmeetings per day :', work_day / meeting_len)
    return

@addBreaker
def datetime_comparing():
    print('Times Comparison:')
    # bingo! just like datetime.date() constructs an instance
    t1 = datetime.time(12, 55, 0)
    t2 = datetime.time(13, 5, 0)
    print('     t1:', t1)
    print('     t2:', t2)
    print('     t1 < t2:', t1 < t2)
    print()
    print('Dates Comparison:')
    d1 = datetime.date.today()
    d2 = datetime.date.today() + datetime.timedelta(days=1)
    print('     d1:', d1)
    print('     d2:', d2)
    print('     d1 > d2:', d1 > d2)
    return

@addBreaker
def datetime_datetime_getattr():
    print('Now      :', datetime.datetime.now())
    print('Today    :', datetime.date.today())
    print('UTC Now  :', datetime.datetime.utcnow())
    print()
    FIELDS = 'year month day hour minute second microsecond'.split()
    d = datetime.datetime.now()
    for attr in FIELDS:
        # my guess: built-in getattr() is using sake API as operator.attrgetter()
        # as two complements, operator.getitem() is also provided 
        print('{:15}: {}'.format(attr, getattr(d, attr)))
    return

@addBreaker
def datetime_datetime_strptime():
    # default format is ISO-8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)
    # ? wtf is 'T' insidef DDTHH tho? my guess: whitespace/tab?

    # ! `datetime.strptime()` parses formatted strings to `datetime instances`
    # * str-->parse-->time
    # ! `datetime_instance.strftime()` formats `datetime instance` to string
    # * str<--format<--time
    fmt   = '%a %b %d %H:%M:%S %Y'
    today = datetime.date.today()
    s     = today.strftime(fmt)
    d     = datetime.datetime.strptime(s, fmt)
    print('ISO      :', today)
    print('strftime :', s)
    print('strptime :', d.strftime(fmt))
    return

@addBreaker
def datetime_timezone():
    min6 = datetime.timezone(datetime.timedelta(hours=-6))
    pls6 = datetime.timezone(datetime.timedelta(hours=6))
    d    = datetime.datetime.now(min6)
    print(min6, ':', d)
    print(datetime.timezone.utc, ':', d.astimezone(datetime.timezone.utc))
    print(pls6, ':', d.astimezone(pls6))
    # converts to the current system timezone
    d_sys = d.astimezone()
    print(d_sys.tzinfo, '         :', d_sys)
    return

if __name__ == "__main__":
    ### ! datetime.time
    # datetime.time
    datetime_time()
    # datetime min and max
    datetime_time_minmax()
    # datetime resolution
    datetime_time_resolution()
    ### ! datetime.date
    datetime_date()
    # constructs date fromordianl() or fromtimestamp()
    datetime_date_fromordinal_vs_fromtimestamp_vs_replace()
    # datetime min and max
    datetime_date_minmax()
    ### ! datetime.timedelta
    datetime_timedelta()
    # datetime.timedelta.total_seconds()
    datetime_timedelta_total_seconds()
    ### ! datetime date math
    datetime_date_math()
    ### ! datetime timedelta math
    datetime_timedelta_math()
    ### ! datetime comparison
    datetime_comparing()
    ### ! combines date and time
    datetime_datetime_getattr()
    ### ! formatting and parsing
    datetime_datetime_strptime()
    ### ! timezone
    datetime_timezone()