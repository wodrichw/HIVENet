import copy
import random
import math
import pickle
import os
import subprocess

#Node example
# "name", [node 1 flag, node 2 flag, node 2 flag, riddle number]
# test = {"Andrew": [1, 0, 0, 4]}
#Printing '4' from test
# print(test["Andrew"][3])

def truncate(number, digits):
   step = pow(10.0, digits)
   return math.trunc(step * number) / step


# Assume only 3 nodes max
def prep_nodes(name, num_nodes, ipAddrs):
   # Generate random number for riddle
   riddle = random.randint(1,3)
   riddle = float(riddle)

   node_pkgs = {}
   return_list = []

   for x in range(num_nodes):
      # Copy name for untouched reference
      temp_name = copy.deepcopy(name)

      print ipAddrs

      # 'andrew_1', 'andrew_2', ...
      temp_name = temp_name + "_" + str(ipAddrs[0][x])

      if x == 0:
         node = {'name': temp_name, 'node1': 1, 'node2': 0, 'node3': 0, 'riddle': riddle}
      elif x == 1:
         node = {'name': temp_name, 'node1': 0, 'node2': 1, 'node3': 0, 'riddle': riddle}
      elif x == 2:
         node = {'name': temp_name, 'node1': 0, 'node2': 0, 'node3': 1, 'riddle': riddle}
      else:
         sys.exit("Error in new_name: prep_nodes(): Line 46")

      # Truncate to avoid decimal error
      riddle = riddle + 0.1
      riddle = truncate(riddle, 1)
    
      return_list.append(node)

   return return_list


def add_to_local(node, fname):
   f = open(fname, 'r')
   contents = pickle.load(f)
   contents.append(node)
   f.close()

   f = open(fname, 'w')
   pickle.dump(contents, f)
   f.close()

def add_to_transfer(node):
   f = open("pickles/send_pkg.pkl", 'w')
   pickle.dump(node, f)
   f.close()

def create():

   # Need to get names of nodes in correct directory and send accordingly
   RD = os.path.dirname(os.path.realpath(__file__))
   ED = os.path.dirname(RD)
   # Final path is the directory that contains
   #  list of connected nodes
   CD = ED + '/classifiers'

   print "Directories: "
   print "RD: ", RD
   print "ED: ", ED
   print "CD: ", CD
   # Get the names of the nodes
   folders = []
   for _, dirnames, _ in os.walk(CD):
      folders.append(dirnames)
   # Remove empty element
   non_empty = []
   for x in range(len(folders)):
      if folders[x] != []:
         non_empty.append(folders[x])
   
   print "Final Folders: ", non_empty

   name = open("name.txt", 'r').read()
   node_list = prep_nodes(name, len(non_empty[0]), non_empty)
   print node_list

   # Add new name to local node's list   
   add_to_local(node_list[0], "pickles/local_names.pkl")
   

   # Add new name to other nodes list for transfer
   # ----------- ASSUMES THREE NODES IN CLASSIFIERS -------------
   transfer_nodes = [node_list[1], node_list[2]]
   add_to_transfer(transfer_nodes)
  
   # Create a single name instance -- Needed?
   p = subprocess.Popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'", shell=True, stdout=subprocess.PIPE)
   IPaddr = p.communicate()[0].strip()
   nodedir = '../classifiers/node_' + IPaddr 

   print("IP: ", IPaddr)
   print "name: ", name

create()