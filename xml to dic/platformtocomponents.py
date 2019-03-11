from collections import OrderedDict

import glob, os

import xmltodict

os.chdir('C:/Users/sbardugo/Desktop/ChangePassword Platform')
f = open("C:/Users/sbardugo/Desktop/ChangePassword Platform/demofile.txt", "a")

def xml_to_dict(path) -> OrderedDict:
    with open(path, 'r+') as fd:
        doc = xmltodict.parse(fd.read())
        return doc


ordered_dict = xml_to_dict(r'C:/Users/sbardugo/Desktop/ChangePassword Platform/ChangePassword Platform.xml')
#print(ordered_dict)

# Why do you need glob? you already have the XML in ordered_dict
for filename in glob.glob("*.xml"):
    for key, value in ordered_dict['Component']['ComponentsSon'].items():
         print(filename)
         f.write(filename + "\n" )
         # attributes can be accessed more easily like: value['@Name'] instead of doing a for loop
         for attr_dictionary in value:
             for k,v in attr_dictionary.items():
                  if k == "@Name":
                        f.write(v + "\n")
                        print(v)



