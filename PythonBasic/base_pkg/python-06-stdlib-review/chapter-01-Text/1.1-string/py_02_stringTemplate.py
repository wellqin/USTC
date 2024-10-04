### string.Template is an alternative of str object's interpolation (format(), %, +)
import string

def str_tmp(s, insert_val):
    t = string.Template(s)
    return t.substitute(insert_val)

def str_interplote(s, insert_val):
    return s % insert_val

def str_format(s, insert_val):
    return s.format(**insert_val)

def str_tmp_safe(s, insert_val):
    t = string.Template(s)
    try:
        return t.substitute(insert_val)
    except KeyError as e:
        print('ERROR:', str(e))
        return t.safe_substitute(insert_val)

val = {'var': 'foo'}

# example 01
s   = """
template 01: string.Template()
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
"""
print(str_tmp(s, val))

# example 02
s   = """
template 02: interpolation %%
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""
print(str_interplote(s, val))

# example 03
s   = """
template 03: format()
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""
print(str_format(s, val))

# example 04
s   = """
$var is here but
$missing is not provided
"""
print(str_tmp_safe(s, val))

"""
conclusion:
- any $ or % or {} is escaped by repeating itself TWICE.
- string.Template is using $var or ${var} to identify and insert dynamic values
- string.Template.substitute() won't format type of the arguments.. 
    -> using string.Template.safe_substitute() instead in this case
"""

