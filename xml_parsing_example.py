'''You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element.
 For any element, the score is equal to the number of attributes it has.

Input Format

The first line contains , the number of lines in the XML document.
The next lines follow containing the XML document.

Output Format

Output a single line, the integer score of the given XML document.

Sample Input

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output

5

Explanation

The feed and subtitle tag have one attribute each - lang.
The title and updated tags have no attributes.
The link tag has three attributes - rel, type and href.

So, the total score is  5

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    root_length=node.attrib
    count=0
    #count=len(root_length)
    #all_links=node.findall()
    #print len(all_links)
    for child in node.iter():
        a=child.attrib
        #print a
        count=len(a)+count
        #for child
        #print count
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    #print get_attr_number(root)