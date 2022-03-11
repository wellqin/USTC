import sys, pickle
sys.path.append('.')
from pkg.breaker import addBreaker
import pprint

@addBreaker
def pickle_string():
    data = [{'a':'A', 'b':2, 'c':3.0}]
    print('DATA     :', end=' ')
    pprint.pprint(data)
    data_string = pickle.dumps(data)
    print('PICKLE   : {!r}'.format(data_string))

@addBreaker
def pickle_unpickle():
    data1 = [{'a':'A', 'b':2, 'c':3.0}]
    print('BEFORE   :', end=' ')
    pprint.pprint(data1)
    data1_string = pickle.dumps(data1)
    data2 = pickle.loads(data1_string)
    print('AFTER    :', end=' ')
    pprint.pprint(data2)

    print('SAME?    :', (data1 is data2))
    print('EQUAL?   :', (data1 == data2))


if __name__ == "__main__":
    # ? using what algorithm to serialize?
    pickle_string()
    # unpickle
    pickle_unpickle()