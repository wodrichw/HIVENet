import os
import pickle
import copy

# This will be a dictionary
#  x.0 = question
#  x.1 = hint 1
#  x.2 = hint 2
# How will this be stored so it is accessible to all nodes?
#  Store individually on each node as a .pkl file
riddle_list = {1.0: "Riddle 1", 1.1: "Hint 1", 1.2: "Hint 2",
               2.0: "Riddle 2", 2.1: "Hint 1", 2.2: "Hint 2",
               3.0: "Riddle 3", 3.1: "Hint 1", 3.2: "Hint 2"}

# add riddle list to .pkl file
file = open('riddle_list.pkl', 'w')
pickle.dump(riddle_list, file)
file.close()

# initialize node name pickle files to prevent empty error
path1 = os.path.dirname(os.path.realpath(__file__))
path2 = os.path.dirname(path1)
final_path = path2 + '/data'

folder_names = []
for _, dirnames, _ in os.walk(final_path):
   folder_names.append(dirnames)

# Delete empty lists
# Need temp to avoid indexing error
non_empty_list = []
for x in range(len(folder_names)):
   print folder_names[x]
   if folder_names[x] != []:
      non_empty_list.append(folder_names[x])

print non_empty_list

name_list = [{'name': 'andrew_node_10.248.63.164', 'node1': 1, 'node2': 1, 'node3': 1, 'riddle': 1.0}]
file = open("pickles/local_names.pkl", 'w')
pickle.dump(name_list, file)
file.close()

# ----------------