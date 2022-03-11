import re, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

text = '''Paragraph one
on two lines.

Paragraph two.

    
Paragraph three.'''

@addBreaker
def re_paragraphs_findall(text):
    pattern = r'(.+?)\n{2,}'
    for num, para in enumerate(re.findall(pattern, text, flags=re.DOTALL)):
        print(num, repr(para))
        print()

@addBreaker
def re_split(text):
    match_findall = re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL)
    match_split   = re.split(r'\n{2,}', text, flags=re.DOTALL)

    print('with re.findall()..')
    for num, para in enumerate(match_findall):
        print(num, repr(para))
        print()
    print()
    print('with re.split()..')
    for num, para in enumerate(match_split):
        print(num, repr(para))
        print()

@addBreaker
def re_split_groups(text):
    print('with re.split()..')
    for num, para in enumerate(re.split(r'(\n{2,})', text)):
        print(num, repr(para))
        print()


def main():
    ### re.findall() vs re.split()
    # re.findall() ..
    re_paragraphs_findall(text=text)
    # re.split() ..
    re_split(text=text)
    # re.split() ..
    re_split_groups(text=text)

if __name__ == "__main__":
    main()
