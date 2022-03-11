# example 01
# no difference when dislaying numeric objects
print("I am %d years old." % 22)
print("I am %s years old." % 22)
print("I am %r years old." % 22)

# example 02
text = "I am %d years old." % 22
print("I said: %s." % text)
print("I said: %r." % text) # %r displays ' '

# example 03
import datetime
today = datetime.datetime.today()
print("%s" % today)
print("%r" % today) # %r repeats its object
# why?
print(str(today))
print(repr(today))