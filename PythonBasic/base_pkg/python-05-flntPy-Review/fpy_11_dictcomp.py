DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

# list -> dict, example 01
dict1 = dict(DIAL_CODES)
print(dict1)
# or list comprehesion, example 02
dict2 = {country:code for (code, country) in DIAL_CODES}
print(dict2)
# example 03
dict3 = dict(zip((86, 91, 1, 62, 55, 92, 880, 234, 7, 81),
            ('China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Russia', 'Jappan')))
print(dict3)
# example 04
dict4 = dict(
    a=1,
    b=2
)
print(dict4)
# update
dict4.update(a=3, b=4)
print(dict4)
dict4.update(a=5, c=6)
print(dict4)

# enum
for index, item in enumerate(list("hello world!"), start=1):
    print(index, item)

# default dictionary
import collections
dd = collections.defaultdict(list)
print(dd[1])
print(dd.get(1, 1))