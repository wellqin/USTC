import calendar, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def calendar_textcalendar():
    c = calendar.TextCalendar(calendar.SUNDAY)
    c.prmonth(2020, 8)

@addBreaker
def calendar_yeardays2calendar():
    import pprint
    cal         = calendar.Calendar(calendar.SUNDAY)
    cal_data    = cal.yeardays2calendar(2020, 3)
    top_months  = cal_data[0]
    first_month = top_months[0]
    print('len(cal_data)        :', len(cal_data))
    print('len(top_months)      :', len(top_months))
    print('first_month          :', len(first_month))
    pprint.pprint(first_month, width=65)
    return

@addBreaker
def calendar_formatyear():
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatyear(2020, 5, 1, 1, 3))
    return

@addBreaker
def calendar_locale():
    try:
        c = calendar.LocaleTextCalendar(locale='en_US')
        c.prmonth(2020, 7)
        print()
        c = calendar.LocaleTextCalendar(locale='fr_FR')
        c.prmonth(2020, 8)
    except:
        pass
    return

### ! P275


if __name__ == "__main__":
    # ! TextCalendar.prmonth() shorts for print month
    # ! HTMLCalendar.formatmonth() is similar
    calendar_textcalendar()
    calendar_yeardays2calendar()
    calendar_formatyear()
    # locale
    calendar_locale()