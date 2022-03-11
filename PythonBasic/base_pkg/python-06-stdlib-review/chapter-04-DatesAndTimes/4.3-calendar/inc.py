bonus  = 42_500
gjj    = 2518 + 1800
months = 12
y19 = [13752, 14341, 11762, 12692, 13072, 12868, 17036, 12596, 14318, 15177, 15427, 15427]
y20 = [22785, 16298, 14004, 16298, 16298, 18064, 17200, 17200]

def average(seq: list):
    return sum(seq) / len(seq)

ave19 = average(y19)
ave20 = average(y20)
ttl20  = (ave20 + gjj) * months + bonus

print('ave20 - ave19           = {:,.2f}'.format(ave20 - ave19))
print('(ave20 - ave19) / ave19 = {:.2%}'.format((ave20 - ave19) / ave19))
print('total20                 = {:,.2f}'.format(ttl20))