"""
! why textwrap?
:: in situation where pretty-printing is desired. pprint
:: it offers programmatic functionality similar to the *paragraph* wrapping
:: or filling features found in many text editors and word processors.

textwrap
|-- filling paragraphs
|-- removing existing indentation
|-- combing dedent and fill
|-- indenting blocks
|-- hanging indents
|-- truncating long text

"""
import textwrap
from py_01_textSample import sample_text

FMT = "\n{:-^60}"
# filling paragraphs: textwrap.fill()
def fill_paragraphs():
    # ugly
    print(FMT.format("original"))
    print(sample_text)
    # ugly as well
    print(FMT.format("textwrap.fill()"))
    print(textwrap.fill(sample_text, width=50))
    
# removing existing indentation: textwrap.dedent()
def dedent_paragraphs():
    print(FMT.format("original"))
    print(sample_text)
    print(FMT.format("textwrap.dedent()"))
    print(textwrap.dedent(sample_text))

# combining dedent and fill
def dedent_and_fill_paragraphs():
    print(FMT.format("textwrap.fill(textwrap.dedent(paragraphs))"))
    t = textwrap.dedent(sample_text).strip()
    for width in [45, 60]:
        print('{} Columns:\n'.format(width))
        print(textwrap.fill(t, width))
        print()

# indenting blocks. wow, just like outlook email forward formatting
def indent_blocks():
    dedent_Text = textwrap.dedent(sample_text)
    wrap_text   = textwrap.fill(dedent_Text, width=50)
    wrap_text   += '\n\nSecond paragraph after a blank line.'
    final       = textwrap.indent(wrap_text, '> ')
    print(FMT.format('textwrap.indent()'))
    print(final)

# passing a callable as *predicate* argument to textwrap.indent()
def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0

def passing_callable_to_indent():
    print(FMT.format("passing callable to textwrap.indent()"))
    dedent_text = textwrap.dedent(sample_text)
    wrap_text   = textwrap.fill(dedent_text, width=50)
    final       = textwrap.indent(wrap_text, 'EVEN ', predicate=should_indent)
    print('\nQuoted block:\n')
    print(final)

# hanging indents
def hanging_indents():
    print(FMT.format("hanging indents by passing arguments to textwrap.fill()"))
    dedent_text = textwrap.dedent(sample_text)
    hang_text   = textwrap.fill(dedent_text,
                                initial_indent='',
                                subsequent_indent=' ' * 4,
                                width=50,)
    print(hang_text)

# truncating long text
def truncate_long_text():
    print(FMT.format("truncating long text with textwrap.shorten()"))
    dedent_text = textwrap.dedent(sample_text)
    wrap_text   = textwrap.fill(dedent_text, width=50)
    print('wrap_text: \n')
    print(wrap_text)
    short_text = textwrap.shorten(wrap_text, 100)
    short_wrap = textwrap.fill(short_text, width=50)
    print('\nShortened:\n')
    print(short_wrap)

def main():
    # filling
    fill_paragraphs()
    # dedenting
    dedent_paragraphs()
    # combining dedent and fill
    dedent_and_fill_paragraphs()
    # indenting blocks
    indent_blocks()
    # passing a callable as the *predicate* argument to textwrap.indent()
    passing_callable_to_indent()
    # hanging indents
    hanging_indents()
    # truncating long text
    truncate_long_text()

if __name__ == "__main__":
    main()