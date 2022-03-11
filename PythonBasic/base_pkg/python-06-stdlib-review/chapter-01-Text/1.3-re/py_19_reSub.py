import re, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

text = 'Make this **bold**. This **too**.'

@addBreaker
def re_sub(text):
    bold = re.compile(r'\*{2}(.*?)\*{2}')
    print('Text:', text)
    print('Bold:', bold.sub(r'<b>\1<b>', text)) # \num index referencing in the substitution. max index referencing is 99

@addBreaker
def re_sub_named_groups(text):
    bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')
    print('Text:', text)
    print('Bold:', bold.sub(r'<b>\g<bold_text><b>', text)) # \g<name> name referencing in the substitution.

@addBreaker
def re_sub_count(text):
    bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')
    print('Text:', text)
    print('Bold:', bold.sub(r'<b>\1<b>', text, count=1)) # passing a value to *count* in the sub to limit the number of substitutions performed

@addBreaker
def re_subn(text):
    bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')
    print('Text:', text)
    print('Bold:', bold.subn(r'<b>\1<b>', text)) # subn

def main():
    # \num referencing in the sub
    re_sub(text=text)
    # \g<name> referencing in the sub
    re_sub_named_groups(text=text)
    # using *count* in the sub to limit the number of substitutions performed
    re_sub_count(text=text)
    # using re.subn() to substitute. it behaves as similar as re.sub(), but it returns both modified string and the count of substitutions made.
    re_subn(text=text)

if __name__ == "__main__":
    main()