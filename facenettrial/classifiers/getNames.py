
import os
nodenum=os.environ['NODENUM']
mynames = open("names",'w')
for mydir in os.listdir('../datasets/data'):
    mynames.write(mydir)
    mynames.write(',')
mynames.seek(mynames.tell() - 1, os.SEEK_SET)
mynames.write('.')
mynames.close()
#print [name for name in os.listdir(".") if os.path.isdir(name)]

nodenum=os.environ['NODENUM']
directory="node"+nodenum+"/"
filename = "newnames"
cfile = open(filename,'r')
names = cfile.readline()
names = names.split(',')
print(names[0])
