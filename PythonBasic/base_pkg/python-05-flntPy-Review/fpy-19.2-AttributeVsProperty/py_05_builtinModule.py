### retrieve all builtins functions/errors
import pprint
pprint.pprint(dir(__builtins__))

### retrieve all built-in modules
import sys
pprint.pprint(sys.builtin_module_names)