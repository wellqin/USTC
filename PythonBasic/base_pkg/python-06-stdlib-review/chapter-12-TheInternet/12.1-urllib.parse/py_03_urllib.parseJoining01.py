from urllib.parse import urljoin
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def urllib_parse_urljoin():
    """
    yeah, i recalled os.path.join() or str.join(List)
    """
    part1 = 'http://www.example.com/path/file.html'
    part2 = 'anotherfile.html'
    logging.debug(f'{urljoin(part1, part2)}')
    part1 = 'http://www.example.com/path/file.html'
    part2 = '../anotherfile.html'   # ! this line is different via using relative portion of the part
    logging.debug(f'{urljoin(part1, part2)}')

def urllib_parse_urljoin_with_path():
    """
    this urljoin(), nice 69
    """
    part1 = 'http://www.example.com/path/'
    part2 = '/subpath/file.html'
    logging.debug(f'{urljoin(part1, part2)}')
    part1 = 'http://www.example.com/path/'
    part2 = 'subpath/file.html'
    logging.debug(f'{urljoin(part1, part2)}')
    ...

if __name__ == "__main__":
    urllib_parse_urljoin()
    print()
    urllib_parse_urljoin_with_path()