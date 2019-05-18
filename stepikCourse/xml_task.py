# from xml.etree.ElementTree import XMLParser
# XMLParser.feed()
from xml.etree import ElementTree



tree = ElementTree.parse('data/xml_task_data.xml')
root = tree.getroot()

def get_attr(root, depth=2
             , color_dict={'red': 0, 'green': 0, 'blue': 0}):
    for child in root:
        color_dict[child.attrib['color']] += depth
        get_attr(child, depth - 1, color_dict)
    return color_dict

color_dict = get_attr(root)
color_dict[root.attrib['color']] += 3

