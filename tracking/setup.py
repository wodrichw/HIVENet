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

# ----------------

file = open('test.pkl', 'w')
pickle.dump(name_list, file)
file.close()
del name_list

# while True:
#    name = raw_input(": ")
#    f = open('test.pkl', 'r')
#    name_list = pickle.load(f)
#    f.close()

#    for x in range(len(name_list)):
#       print name_list[x]

#    name_list.append(name)

#    f = open('test.pkl', 'w')
#    pickle.dump(name_list, f)
#    f.close()

class test:
   def __init__(self, one):
      self.one = one

print ("----")
new = test(1)
temp = copy.deepcopy(new)

print(new.one)
print(temp.one)

temp.one = 2
print(new.one)
print(temp.one)

listt = ['a', 'b', 'c']
print(listt.index('b'))