---
title: XML
date: November 8, 2022
---

There are several XML parsers available in the Python standard library. Below is an example of using the ElementTree module.

```xml
<!-- Example XML file named sample.xml -->

<?xml version="1.0"?>
<Tests xmlns="http://www.adatum.com">
  <Test TestId="0001" TestType="CMD">
    <Name>Convert number to string</Name>
    <CommandLine>Examp1.EXE</CommandLine>
    <Input>1</Input>
    <Output>One</Output>
  </Test>
  <Test TestId="0002" TestType="CMD">
    <Name>Find succeeding characters</Name>
    <CommandLine>Examp2.EXE</CommandLine>
    <Input>abc</Input>
    <Output>def</Output>
  </Test>
  <Test TestId="0003" TestType="GUI">
    <Name>Convert multiple numbers to strings</Name>
    <CommandLine>Examp2.EXE /Verbose</CommandLine>
    <Input>123</Input>
    <Output>One Two Three</Output>
  </Test>
  <Test TestId="0004" TestType="GUI">
    <Name>Find correlated key</Name>
    <CommandLine>Examp3.EXE</CommandLine>
    <Input>a1</Input>
    <Output>b1</Output>
  </Test>
  <Test TestId="0005" TestType="GUI">
    <Name>Count characters</Name>
    <CommandLine>FinalExamp.EXE</CommandLine>
    <Input>This is a test</Input>
    <Output>14</Output>
  </Test>
  <Test TestId="0006" TestType="GUI">
    <Name>Another Test</Name>
    <CommandLine>Examp2.EXE</CommandLine>
    <Input>Test Input</Input>
    <Output>10</Output>
  </Test>
</Tests>
```

```python
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
```

Running the above example in the terminal prints the following:

```
---
TestId        0001
TestType      CMD
Name          Convert number to string
CommandLine   Examp1.EXE
Input         1
Output        One
---

---
TestId        0002
TestType      CMD
Name          Find succeeding characters
CommandLine   Examp2.EXE
Input         abc
Output        def
---

---
TestId        0003
TestType      GUI
Name          Convert multiple numbers to strings
CommandLine   Examp2.EXE /Verbose
Input         123
Output        One Two Three
---

---
TestId        0004
TestType      GUI
Name          Find correlated key
CommandLine   Examp3.EXE
Input         a1
Output        b1
---

---
TestId        0005
TestType      GUI
Name          Count characters
CommandLine   FinalExamp.EXE
Input         This is a test
Output        14
---

---
TestId        0006
TestType      GUI
Name          Another Test
CommandLine   Examp2.EXE
Input         Test Input
Output        10
---
```

## Further reading

See the resources below for more information about XML parsing in Python.

- [A Roadmap to XML Parsers in Python](https://realpython.com/python-xml-parser/#choose-the-right-xml-parsing-model)
- [XML Processing Modules](https://docs.python.org/3/library/xml.html)
