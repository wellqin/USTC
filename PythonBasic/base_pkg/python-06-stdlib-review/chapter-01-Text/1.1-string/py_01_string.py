"""
std lib -- string

! why do I need it when I have tools like str class, format() function and % etc?
:: this lib provides other tools to make advanced text manipulation simple..

? hmm, advanced text manipulations
:: I'm not aware of these manipulations...

TODOS: learns advanced text manipulations.
string
|-- string.Template # alternative beyond the features of str objects. a good middle ground.
|-- string.textwrap # formats text from paragraphs by limiting the width of output, adding indentation, and inserting line breaks to wrap lines consistently.
|-- string.difflib  # computes the actual differences between sequences of text in terms of the parts add, removed, or changed.

history
|-- string module datas from the earliest versions of Python.
|-- Many of the functions previously implemented in the module have been moved to method of str objects.
|-- but the module retains several usefull constants and classes for working with str objects.

"""

### functions: string.capwords() == str.title()
def cap(s):
    """returns capitalized all of the words in a string
    """
    import string
    return string.capwords(s)

def cap2(s):
    """returns capitalized the first word of a string
    """
    return s.capitalize()

def cap3(s):
    return s.title()

s = "hello world"
print(cap(s))
print(cap2(s))
print(cap3(s))
assert cap(s) == cap3(s), "string capitalization successed.."
assert cap(s) == cap2(s), "string capitalization failed.."