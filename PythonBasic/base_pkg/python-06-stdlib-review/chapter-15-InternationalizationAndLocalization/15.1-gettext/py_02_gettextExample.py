import gettext
# set up message catalog access

t = gettext.translation(
    'example_domain',
    'locale',
    fallback=True,
)

"""
The usual pattern is to bind the appropriate lookup function
to the name _ (a single underscore character) 

so that the code is not cluttered with multiple
calls to functions with longer names

hmmm, doesnt readability matter?
special cases are not sepcial enough to break the rules

the Zen of Python
beautiful is better than ugly
explicit is better than implicit
simple is better than complex
complex is btter than complicated
flat is better than nested
sparse is better than dense

readability counts
special cases are not special enough to break the rules

althou practicality beats purity

errors should never pass silently
unless explicitly silenced

...

"""
_ = t.gettext

print(_('this msg is in the script'))