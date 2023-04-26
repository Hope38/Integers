import xml.etree.ElementTree as ET

# parse the XML file
tree = ET.parse('GaryPaulsen.xml')

# get the root element of the XML tree
root = tree.getroot()

# iterate over the book elements
for book in root.findall('book'):
    # print the year and summary of each book
    title = book.find('title').text
    year = book.find('year').text
    summary = book.find('summary').text
    print('title: ', title)
    print('Year:', year)
    print('Summary:', summary)
