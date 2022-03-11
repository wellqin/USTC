import string

### change default setting of string.Template
class MyTemplate(string.Template):
    """change default setting of string.Template by adjusting
    regular expression pattern it uses to find the variable names inside of template body.
    """
    delimiter = '%'
    idpattern = '[a-zA-Z]+_[a-zA-Z]+'

def str_tmp_safe_sub(s, val):
    t = MyTemplate(s)
    return t.safe_substitute(val)

# exameple 01
s = '''
    delimiter   :   %%
    Replaced    :   %with_Underscore
    Ignored     :   %Notunderscored
'''

d = {
    'with_underscore'   :   'replaced',
    'notunderscore'     :   'not replaced',
}

print(str_tmp_safe_sub(s, d))

### more complex change, it is possible to override the *pattern* attribute
### and define an entirely new regular expression
# here is how to display *pattern* aatribute
t = string.Template('$var')
print(t.pattern.pattern) # t.pattern is a compiled regular expression
# here is how to define an entirely new regex
import re
class MyTemplate2(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''
s = '''
{{{{
{{var}}
'''
t = MyTemplate2(s)
print('MATCHES:', t.pattern.findall(t.template))
print('SUBSTITUTED:', t.safe_substitute(var='replacement'))