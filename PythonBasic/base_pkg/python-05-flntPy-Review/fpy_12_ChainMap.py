import pprint
import collections
import builtins
pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
print("{0:-^20}".format("locals"))
pprint.pprint(locals())
print("{0:-^20}".format("globals"))
pprint.pprint(globals())
print("{0:-^20}".format("builtins"))
pprint.pprint(vars(builtins))
# pprint.pprint(pylookup)