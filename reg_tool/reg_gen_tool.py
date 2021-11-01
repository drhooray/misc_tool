
import lxml
import lxml.builder
import sys

from lxml import objectify
from lxml import etree as E


print 'number of arg:', len(sys.argv), 'arg'
print 'arg list:', str(sys.argv)
inputfile = str(sys.argv[1])

def fillobjectFile_101(root,var1, var2 ):
	regroot=E.Element("regSetting")
	E.SubElement(regroot, "registerAddr").text= var2
	E.SubElement(regroot, "registerData").text= var1
	E.SubElement(regroot, "regAddrType", range="[1,4]").text="2"
	E.SubElement(regroot, "regDataType", range="[1,4]").text="1"
	E.SubElement(regroot, "operation").text="WRITE"
	E.SubElement(regroot, "delayUs").text="0x00"
	root.append(regroot)

root = E.Element("resSettings")

# read register table and parse it
files=open(inputfile)
files_l=files.readlines()
var = [[0] * 2 for i in range(len(files_l))]

''' 
store the list,
hard code, TBD
'''

for i in range(len(files_l)):
        for j in range(2):
                if j==1:
                        var[i][j]=files_l[i][1:7]
                else:
                        var[i][j]=files_l[i][9:13]

print(var)

count=0
for i in range (len(files_l)):
	fillobjectFile_101(root,var[count][0],var[count][1])
	count+=1

print(E.tostring(root,pretty_print=True))
with open("gen_result.xml",'wb') as doc:
        doc.write(E.tostring(root, pretty_print=True))

