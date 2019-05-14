import subprocess
import pickle
import os

# f = open("test.pkl", 'r')
# string = pickle.load(f)
# f.close()

# print(string["Andrew"][3])

folers = []

for _, dirnames, filenames in os.walk('.'):
   folers.append(dirnames)

for x in range(len(folers)):
   print folers[x]

path = os.path.dirname(os.path.realpath(__file__))
path2 = os.path.dirname(path)
final_path = path2 + '/classifiers'

print(path)
print(path2)
print(final_path)

folders = []
x = 0

for _, dirnames, _ in os.walk(final_path):
   print x
   x += 1
   folders.append(dirnames)

print folders

for x in range(len(folders)):
   print folders[x]

   if folders[x] == []:
      print "none"
      del folders[x]

print folders[0]
string = str(folders[0])
name = "andrew" + "_" + str(folders[0])
print name

print "\n\n"
p = subprocess.Popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'", shell=True, stdout=subprocess.PIPE)
IPaddr = p.communicate()[0].strip()
nodedir = '../classifiers/node_' + IPaddr 

print("IP: ", IPaddr)