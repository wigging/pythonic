"""
Example of parsing an XML file named sample.xml and printing the parsed data
to the screen.
"""

import xml.etree.ElementTree as ET

with open('sample.xml') as file:
    tree = ET.parse(file)
    root = tree.getroot()

for rt in root:
    testid = rt.attrib['TestId']
    testtype = rt.attrib['TestType']
    name = rt[0].text
    cmdline = rt[1].text
    enput = rt[2].text
    output = rt[3].text

    print(
        '---\n'
        f'TestId        {testid}\n'
        f'TestType      {testtype}\n'
        f'Name          {name}\n'
        f'CommandLine   {cmdline}\n'
        f'Input         {enput}\n'
        f'Output        {output}\n'
        '---\n')
