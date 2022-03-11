import sys
sys.path.append('.')
from pkg.breaker import addBreaker
from xml.etree import ElementTree

@addBreaker
def xml_ParseElementTree():
    podcast = r'chapter-07-DataPersistenceExchange\7.5-xlm\podcasts.opml'
    with open(podcast, 'r') as f:
        tree = ElementTree.parse(f)
    print(tree)
    pass

if __name__ == "__main__":
    # <xml.etree.ElementTree.ElementTree object at 0x01461690>
    xml_ParseElementTree()