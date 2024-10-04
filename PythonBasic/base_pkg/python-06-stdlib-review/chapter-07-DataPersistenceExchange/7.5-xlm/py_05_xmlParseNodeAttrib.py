import sys
sys.path.append('.')
from pkg.breaker import addBreaker
from xml.etree import ElementTree

DATA = r'chapter-07-DataPersistenceExchange\7.5-xlm\data.xml'

@addBreaker
def xml_node_attribute():
    with open(DATA, 'rt') as f:
        tree = ElementTree.parse(f)
    node = tree.find('./with_attributes')
    print(node.tag)
    for name, value in sorted(node.attrib.items()):
        print(' %-4s = "%s"' % (name, value))
    pass

@addBreaker
def xml_node_text():
    with open(DATA, 'rt') as f:
        tree = ElementTree.parse(f)
    for path in ['./child', './child_with_tail']:
        node = tree.find(path)
        print(node.tag)
        print(' child node text:', node.text)
        print(' and tail text  :', node.tail)

@addBreaker
def xml_entity_references():
    with open(DATA, 'rt') as f:
        tree = ElementTree.parse(f)
    node = tree.find('entity_expansion')
    print(node.tag)
    print('  in attribute:', node.attrib['attribute'])
    print('  in text     :', node.text.strip())
    
    pass


if __name__ == "__main__":
    # friends, this is superb familiar concepts, like BS4
    # web scraping technicals
    xml_node_attribute()
    xml_node_text()
    xml_entity_references()