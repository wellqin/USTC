import sys
sys.path.append('.')
from xml.etree import ElementTree
from pkg.breaker import addBreaker
import pprint

PODCAST = r'chapter-07-DataPersistenceExchange\7.5-xlm\podcasts.opml'
@addBreaker
def xml_ElementTree_dump_opml():
    with open(PODCAST, 'rt') as f:
        tree = ElementTree.parse(f)
    for node in tree.iter():
        pprint.pprint(node)
    pass

@addBreaker
def xml_ElementTree_show_feed_urls():
    with open(PODCAST, 'rt') as f:
        tree = ElementTree.parse(f)
    for node in tree.iter('outline'):
        name = node.attrib.get('text')
        # 'xmlUrl' vs 'xmlUrl', case-sensitive. it matters
        url  = node.attrib.get('xmlUrl')
        if name and url:
            print(' %s' % name)
            print('   %s' % url)
        else:
            print(name)

if __name__ == "__main__":
    xml_ElementTree_dump_opml()
    xml_ElementTree_show_feed_urls()