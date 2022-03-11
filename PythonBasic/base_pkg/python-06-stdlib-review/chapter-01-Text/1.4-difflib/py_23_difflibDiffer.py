import difflib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker
from py_22_difflibData import text1_lines, text2_lines

@addBreaker
def difflib_differ():
    # initializes a differ obj
    d    = difflib.Differ()
    # prefabrications: split texts into lines
    # [...]
    # compares difference using differ.compare()
    diff = d.compare(text1_lines, text2_lines)
    # markup data and symbols are prerequisited, like - + ?
    print('\n'.join(diff))

@addBreaker
def difflib_ndiff():
    diff = difflib.ndiff(text1_lines, text2_lines)
    print('\n'.join(diff))

@addBreaker
def difflib_unified():
    # *lineterm* is used to tell difflib.unified_diff() to skip appending newlines to the control lines that it returns 
    # because the input lines do not include them
    # newlines are added to all of the lines when they are printed
    # the output should look familiar to **version control**
    diff = difflib.unified_diff(text1_lines, text2_lines, lineterm='')
    print('\n'.join(diff))

@addBreaker
def difflib_contextDiff():
    diff = difflib.context_diff(text1_lines, text2_lines, lineterm='')
    print('\n'.join(diff))


def main():
    ### difflib.differ().compare() == difflib.ndiff();
    ### difflib.unified_diff() == difflib.context_diff();

    # compare bodies of texts
    difflib_differ()
    # difflib.ndiff() essentially produces the same output
    # difflib.ndiff() is specifically tailored for working with text data and eliminating "noise" in the input
    difflib_ndiff()
    # difflib.unified_diff() provide other report format ..
    difflib_unified()
    # difflib.context_diff() ..
    difflib_contextDiff()

if __name__ == "__main__":
    main()