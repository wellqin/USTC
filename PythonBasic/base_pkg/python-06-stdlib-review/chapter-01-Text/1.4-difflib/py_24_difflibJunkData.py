import difflib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker
from py_22_difflibData import text1_lines, text2_lines

@addBreaker
def difflib_junk():
    def show_results(match):
        print('  a = {}'.format(match.a))
        print('  b = {}'.format(match.b))
        print('  size = {}'.format(match.size))
        i, j, k = match
        print('  A[a:a+size] = {!r}'.format(A[i:i + k]))
        print('  B[b:b+size] = {!r}'.format(B[j:j + k]))

    A = " abcd"
    B = "abcd abcd"
    print('A = {!r}'.format(A))
    print('B = {!r}'.format(B))
    print('\nWithout junk detection:')
    s1      = difflib.SequenceMatcher(None, A, B)
    match1  = s1.find_longest_match(0, len(A), 0, len(B))
    show_results(match1)
    print('\nTreat spaces as junk:')
    s2      = difflib.SequenceMatcher(lambda x: x==" ", A, B)
    match2  = s2.find_longest_match(0, len(A), 0, len(B))
    show_results(match2)

def main():
    # customed *junk data* using difflib.sequenceMatcher().find_longest_match() ..
    # difflib.Differ() doesn't ignore anything explicitly
    # difflib.ndiff() ignores *space* and *tab* by default
    # now, raise my new *noise* detector: difflib.sequenceMatcher() .. 
    difflib_junk()

if __name__ == "__main__":
    main()