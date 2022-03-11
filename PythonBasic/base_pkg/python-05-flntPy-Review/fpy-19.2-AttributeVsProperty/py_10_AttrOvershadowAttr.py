
"""
### lets check attribute between obj vs Class
>>> obj = Class()
>>> vars(obj)
{}
>>> obj.data
'the class data attr'
>>> obj.data = 'bar'
>>> vars(obj)
{'data': 'bar'}
>>> obj.data
'bar'
>>> Class.data
'the class data attr'

### now lets see property between obj vs Class
>>> obj.prop
'the property value'
>>> obj.prop = 'foo'
Traceback (most recent call last):
    ...
AttributeError: can't set attribute
>>> obj.__dict__.update(prop='foo')
>>> vars(obj)
{'data': 'bar', 'prop': 'foo'}
>>> obj.prop
'the property value'
>>> Class.prop = 'baz'
>>> Class.prop
'baz'
>>> obj.prop
'foo'
"""

class Class:
    data = 'the class data attr'
    @property
    def prop(self):
        return 'the property value'

if __name__ == "__main__":
    import doctest
    doctest.testmod()