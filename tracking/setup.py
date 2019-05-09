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
name_list = ['andrew']
file = open('node1_name.pkl', 'w')
pickle.dump(name_list, file)
file.close()

name_list = ['andrew']
file = open('node2_name.pkl', 'w')
pickle.dump(name_list, file)
file.close()

name_list = ['andrew']
file = open('node3_name.pkl', 'w')
pickle.dump(name_list, file)
file.close()

# ----------------