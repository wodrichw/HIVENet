import math
import datetime
import random
import pickle
import copy

node_one = []
node_two = []
node_three = []

class package:
   # name = name of individual
   # node1 = 
   # riddle = the part of the riddle to print
   #     if source riddle = 1.0, next node = 1.1, next node = 1.2
   # source = original node created at
   #     This will always print the original question
   # 
   def __init__(self, user_name, node1_flag, node2_flag, node3_flag, riddle, source):
      self.name = user_name
      self.node1 = node1_flag
      self.node2 = node2_flag
      self.node3 = node3_flag
      self.riddle = riddle
      self.source = source
   
# simulates sending the node, but does setup first
#  the setup will have nothing to do with the sending and will be in the main program
def server(class_obj, node_num):
   
   print("Sending")

# simulates receiving the node
def client():
   print("Receiving")

# simulates process the information
def process():
   print("Processing")

# -------------------------------------------------------------------------------

#  simulates getting user input for recognition
#  This portion is synonymous to the user putting their name into the interface
#  For this function, it is assumed that the person already put their name in -- "name"
#  "node_num" acts as a placeholder to the name of the node the user is at
#     This will be handled differently
def get_face(name, node_num):
   # Next part will be the same on every node, but for the purposes of this simulation,
   #     it will be split up between 3 if statements
   # Each statement will represent 1 node
   # This code will be implemented in execution

   # If you are at node 1,
   if node_num == '1':
      # First, the node name should be appended to the name to uniquely identify it
      name = name + "_one"

      # Once the name has been associated with a node, store the name in the source node's 
      #     already recognized name list
      #     Input this from a pkl file everytime. It will just be a list
      #              -- Note, cannot load empty pkl file, so initialize with something in setup.py

      # Load names for appending
      f = open('node1_name.pkl', 'r')
      names_list = pickle.load(f)  
      f.close()
      names_list.append(name)
      # dump names back into .pkl file
      f = open('node1_name.pkl', 'w')
      pickle.dump(names_list, f)
      f.close()

      # Next, generate random number for riddle
      riddle_num = random.randint(1,3)
      riddle_num = float(riddle_num)
      print("random number: ", riddle_num)

      # Next, create a new object
      #  This object will be passed to the other nodes
      #  The first bool = node 1, second = node 2, third = node 3
      new_obj = package(name, True, False, False, riddle_num, 1)

      # Next, for now, the objects will be stored in a list. Bump this to pickle files later
      node_one.append(new_obj)
      temp_one = copy.deepcopy(new_obj)
      temp_two = copy.deepcopy(new_obj)

      num_one = temp_one.riddle + 0.1
      num_two = temp_two.riddle + 0.2
      num_one = truncate(num_one, 1)
      num_two = truncate(num_two, 1)

      # Simulate sending to through servers
      # Node 2 first, wait a couple seconds to ensure transmission, then node 3
      temp_one.node1 = False
      temp_one.node2 = True
      # Increment riddle_num at source to deconflict similar numbers
      temp_one.riddle = num_one
      print("node 2 temp_one: ", temp_one.riddle)
      node_two.append(temp_one)

      # Node 3
      temp_two.node1 = False
      temp_two.node3 = True
      temp_two.riddle = num_two
      print("node 3 temp_two: ", temp_two.riddle)
      node_three.append(temp_two)

      print_node(node_one, node_two, node_three)

      del temp_one
      del temp_two
      del new_obj
      # Now, all the nodes should be updated with the new person and a corresponding riddle

   # If you are at node 2
   if node_num == '2':
      name = name + "_two"

      f = open('node2_name.pkl', 'r')
      names_list = pickle.load(f)  
      f.close()
      names_list.append(name)

      f = open('node2_name.pkl', 'w')
      pickle.dump(names_list, f)
      f.close()

      riddle_num = random.randint(1,3)
      riddle_num = float(riddle_num)
      print("random number: ", riddle_num)

      new_obj = package(name, False, True, False, riddle_num, 2)

      node_two.append(new_obj)

      # Copy strictly for incrementing riddle trackers
      temp_one = copy.deepcopy(new_obj)
      temp_two = copy.deepcopy(new_obj)

      num_one = temp_one.riddle + 0.1
      num_two = temp_two.riddle + 0.2
      num_one = truncate(num_one, 1)
      num_two = truncate(num_two, 1)

      temp_one.node1 = True
      temp_one.node2 = False

      temp_one.riddle = num_one
      node_one.append(temp_one)

      temp_two.node2 = False
      temp_two.node3 = True
      temp_two.riddle = num_two
      node_three.append(temp_two)

      print_node(node_one, node_two, node_three)

      del temp_one
      del temp_two
      del new_obj

   # If you are at node 3
   if node_num == '3':
      name = name + "_three"

      f = open('node3_name.pkl', 'r')
      names_list = pickle.load(f)  
      f.close()
      names_list.append(name)

      f = open('node3_name.pkl', 'w')
      pickle.dump(names_list, f)
      f.close()

      riddle_num = random.randint(1,3)
      riddle_num = float(riddle_num)
      print("random number: ", riddle_num)


      new_obj = package(name, False, False, True, riddle_num, 3)

      node_three.append(new_obj)

      # Copy strictly for incrementing riddle trackers
      temp_one = copy.deepcopy(new_obj)
      temp_two = copy.deepcopy(new_obj)

      num_one = temp_one.riddle + 0.1
      num_two = temp_two.riddle + 0.2
      num_one = truncate(num_one, 1)
      num_two = truncate(num_two, 1)

      # 1
      temp_one.node1 = True
      temp_one.node3 = False

      temp_one.riddle = num_one
      node_one.append(temp_one)

      # 2
      temp_two.node3 = False
      temp_two.node2 = True
      temp_two.riddle = num_two
      node_one.append(temp_two)

      print_node(node_one, node_two, node_three)

      del temp_one
      del temp_two
      del new_obj


def old_person(user, node_num):
   print("Welcome back _____. Your riddle/hint is ______")
   # When the person is recognized, trigger a riddle hint/question, depending on which node you are at.
   if node_num == '1':
      user = user + "_one"
      for x in range(len(node_one)):
         name = node_one[x].name
         if name == user:
            pos = x
            break
      
      name = node_one[pos].name
      riddle = node_one[pos].riddle

      print("name: ", name)
      # get corresponding riddle from pickle file
      file = open('riddle_list.pkl', 'r')
      riddles = pickle.load(file)
      file.close()
      print("riddle number: ", riddle)
      print("Actual riddle: ", riddles[riddle])
   
   if node_num == '2':
      user = user + "_two"
      for x in range(len(node_two)):
         name = node_two[x].name
         if name == user:
            pos = x
            break
      
      name = node_two[pos].name
      riddle = node_two[pos].riddle

      print("name: ", name)
      # get corresponding riddle from pickle file
      file = open('riddle_list.pkl', 'r')
      riddles = pickle.load(file)
      file.close()
      print("riddle number: ", riddle)
      print("Actual riddle: ", riddles[riddle])
   
   if node_num == '3':
      user = user + "_three"
      for x in range(len(node_three)):
         name = node_three[x].name
         if name == user:
            pos = x
            break
      
      name = node_three[pos].name
      riddle = node_three[pos].riddle

      print("name: ", name)
      # get corresponding riddle from pickle file
      file = open('riddle_list.pkl', 'r')
      riddles = pickle.load(file)
      file.close()
      print("riddle number: ", riddle)
      print("Actual riddle: ", riddles[riddle])

# Main will encompass the entire HIVENet system
def main():
   # Two options when interacting with project
   # Number 1: input new name - train on new face
   #     This option triggers on user inputting name through interface
   # Number 2: recognize face
   #     This option triggers on opening recognition.py, getting name from it,
   print("Starting")
   while True:
      option = raw_input("Are you a new person (1)? Or are you being recognized (2)? ")
      if option == '1':
         name = raw_input("Enter name for first time processing: ")
         node = raw_input("Enter which node you are at: ")
         get_face(name, node)
      elif option == '2':
         name = raw_input("Enter name for recognition purposes: ")
         node = raw_input("Enter which node you are at: ")
         old_person(name, node) 

# -- utility functions
def truncate(number, digits):
   stepper = pow(10.0, digits)
   return math.trunc(stepper*number) / stepper

def print_node(node1, node2, node3):
   print("Here is the newly created object on node 1: ")
   print(node1[-1].name)
   print(node1[-1].node1)
   print(node1[-1].node2)
   print(node1[-1].node3)
   print(node1[-1].riddle)

   print("Here is the newly created object on node 2: ")
   print(node2[-1].name)
   print(node2[-1].node1)
   print(node2[-1].node2)
   print(node2[-1].node3)
   print(node2[-1].riddle)

   print("Here is the newly created object on node 3: ")
   print(node3[-1].name)
   print(node3[-1].node1)
   print(node3[-1].node2)
   print(node3[-1].node3)
   print(node3[-1].riddle)

main()
