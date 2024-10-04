"""
! what?
CLI

! why?
most of time, i use CLI from other programs.
i wanna build my own CLI.

! how?

using argparse to build CLI
- import `argparse`
- create parser
- add optional and positional arguments to the parser
- execute `.parse_args()`

"""

### w/o argparse
# import os, sys
# if len(sys.argv) > 2:
#     print('You have specified to many arguments')
#     sys.exit()

# if len(sys.argv) < 2:
#     print('You need to specified the path to be listed')
#     sys.exit()

# input_path = sys.argv[1]
# if not os.path.isdir(input_path):
#     print('the path specified does not exist')
#     sys.exit()
# print('\n'.join(os.listdir(input_path)))

### with argparse
# myls.py
import argparse
import os, sys

# creates parser
parser = argparse.ArgumentParser(description='List the content of a folder')
# adds arguments
parser.add_argument(
    'Path',
    metavar='path',
    type=str,
    help='the path to list',
)
# executes the parse_args() method
args = parser.parse_args()
input_path = args.Path
if not os.path.isdir(input_path):
    sys.exit('the path specified does not exist')
print('\n'.join(os.listdir(input_path)))