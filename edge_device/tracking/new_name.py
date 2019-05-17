import copy
import random
import math
import pickle
import os
import subprocess
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from communication.client.client import sendTrackingDataToEdgeDevices

#Node example
# "name", [node 1 flag, node 2 flag, node 2 flag, riddle number]
# test = {"Andrew": [1, 0, 0, 4]}
#Printing '4' from test
# print(test["Andrew"][3])
# ----------------------------------------
# ----------------------------------------
def truncate(number, digits):
   step = pow(10.0, digits)
   return math.trunc(step * number) / step

# ----------------------------------------
# Assume only 3 nodes max
# ----------------------------------------
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
      temp_name = temp_name + "_" + str(ipAddrs[x])

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

# ----------------------------------------
# adds to the file that contains the local names
# ----------------------------------------
def add_to_local(node, fname):
   f = open(fname, 'rb')
   contents = pickle.load(f)
   contents.append(node)
   f.close()

   f = open(fname, 'wb')
   pickle.dump(contents, f)
   f.close()

   print "--ADDED TO LOCAL--"
# ----------------------------------------
# ----------------------------------------
def add_to_transfer(node):
   f = open("pickles/send_pkg.pkl", 'wb')
   pickle.dump(node, f)
   f.close()

# ----------------------------------------
# Checks for repeats of names to avoid incorrect riddles
# If there is a repeat of a name (same name different person) append counter at end of name
# Can assume that having to do this on local computer means you have to on all computers
#     So, append counter to all nodes
# ----------------------------------------
def check_repeats(node_list):
   # Open local name list
   f = open('local_names.pkl', 'rb')
   ln_list = pickle.load(f)
   f.close()

   # Iterate through local_names list looking for similar names
   ctr = 0

   for x in range(len(ln_list)):
      print "\n\n------ ", ln_list[x]['name']
      for y in range(len(node_list)):
         if node_list[y]['name'] == ln_list[x]['name']:
            # Name is present in list, update node_list[y]['name'] and increment counter
            #  Issue -- deletes last two chars assumnig it is _x, need to iterate looking for _ 
            #  Iterate through ln_list
            underscore = 0
            for z in range(len(node_list[y]['name'])):
               if node_list[y]['name'][z] == '_':
                  underscore += 1
                  print "---z: ", z
            if underscore == 3:
               node_list[y]['name'] = node_list[y]['name'][:-2] + '_' + str(ctr)
            else:
               node_list[y]['name'] = node_list[y]['name'] + '_' + str(ctr)
            ctr += 1
   return node_list         


# ----------------------------------------
# Main function
# ----------------------------------------
def create(name, LND, CD):

   # Need to get names of nodes in correct directory and send accordingly
   RD = os.path.dirname(os.path.realpath(__file__))
   ED = os.path.dirname(RD)
   # Final path is the directory that contains
   #  list of connected nodes
   # CD = ED + '/classifiers'

   print "Directories: "
   print "RD: ", RD
   print "ED: ", ED
   print "CD: ", CD
   print "LND", LND

   # Get the names of the nodes
   #     Use getIPs.sh
   p = subprocess.Popen(ED+'/communication/client/scripts/getIPs.sh', shell=True, stdout=subprocess.PIPE)
   IPaddr = str(p.communicate()[0]).split(',')
   print "ips: ", IPaddr

   # Note: non_empty is the list of ip addresses
   node_list = prep_nodes(name, len(IPaddr), IPaddr)
   print "Node List: ", node_list

   # Check if the name already exists in local_names.pkl
   #     No need, just have people put first and last names
   # node_list = check_repeats(node_list)

   # Add new name to local node's list   
   add_to_local(node_list[0], LND)

   # Prep transfer node list for sending
   transfer_nodes = []
   for x in range(len(node_list)):
      if x == 0:
         continue
      else:
         print "here"
         transfer_nodes.append(node_list[x])
   
   # Send to server
   print "---:transfer_nodes: ", transfer_nodes
   return transfer_nodes
   
# create('hivenet-face', 'local_names.pkl')