import os
import pickle
import copy

# This will be a dictionary
#  x.0 = question
#  x.1 = hint 1
#  x.2 = hint 2
# How will this be stored so it is accessible to all nodes?
#  Store individually on each node as a .pkl file
# https://www.riddles.com/best-riddles
riddle_list = [{1.0: "What has a head, a tail, is brown, and has no legs?",
               1.1: "", 
               1.2: "Hint 2", 
               'answer': "penny"},
               {2.0: "What room do ghosts avoid?", 
               2.1: "Hint 1", 
               2.2: "Hint 2", 
               'answer': "living room"},
               {3.0: "What 8 letter word can have a letter taken away and it still makes a word. Take another letter away and it still makes a word. Keep on doing that until you have one letter left. What is the word?", 
               3.1: "Hint 1", 
               3.2: "Hint 2",
               'answer': "starting",
               'descript_3': "the word is starting; starting, staring, string, sting, sing, sin, in, I"}]

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

# Add the current machine's IP address to names for consistency in local.pkl
print non_empty_list
name_list = []
ipAddr = raw_input("Enter you IP address: ")
for x in range(len(non_empty_list[0])):
   print non_empty_list[0][x]
   non_empty_list[0][x] = str(non_empty_list[0][x]) + "_node_" + str(ipAddr)
   name_list.append({'name': non_empty_list[0][x], 'node1': 1, 'node2': 1, 'node3': 1, 'riddle': 1.0})
print non_empty_list
print name_list


file = open("local_names.pkl", 'w')
pickle.dump(name_list, file)
file.close()

# ----------------