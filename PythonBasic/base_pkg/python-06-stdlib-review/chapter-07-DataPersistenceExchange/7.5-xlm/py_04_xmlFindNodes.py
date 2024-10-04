import sys
sys.path.append('.')
from pkg.breaker import addBreaker
from xml.etree import ElementTree
from py_03_xmlTraverseParsedTree import PODCAST

@addBreaker
def xml_find_feeds_by_tag():
    with open(PODCAST, 'rt') as f:
        tree = ElementTree.parse(f)
    for node in tree.findall('.//outline'):
        # ? wtf? why node.get() works too?
        # ? then wtf do i need write longer version?
        url = node.attrib.get('xmlUrl')
        # url = node.get('xmlUrl')
        if url:
            print(url)
    pass

@addBreaker
def xml_find_feeds_by_structure():
    with open(PODCAST, 'rt') as f:
        tree = ElementTree.parse(f)
    for node in tree.findall('.//outline/outline'):
        url = node.attrib.get('xmlUrl')
        print(url)


if __name__ == "__main__":
    xml_find_feeds_by_tag()
    xml_find_feeds_by_structure()