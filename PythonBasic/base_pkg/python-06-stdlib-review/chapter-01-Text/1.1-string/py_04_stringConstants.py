import inspect
import string

def is_str(value):
    return isinstance(value, str)

def main():
    for name, value in inspect.getmembers(string, is_str):
        if name.startswith('_'):
            continue
        print('%s=%r\n' % (name, value))

if __name__ == "__main__":
    main()