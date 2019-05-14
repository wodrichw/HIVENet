import pickle
import os

diction = {'1.0': 'hello'}

def main():
   # Open the pickle file
   f = open('pickles/rec_py_face.pkl', 'r')
   name = pickle.load(f)
   f.close()

   # Open local names list

   # Open riddles list
   f = open('pickles/riddle_list.pkl', 'r')
   riddles = pickle.load(f)
   f.close()

   f = open('pickles/local_names.pkl', 'r')
   name_list = pickle.load(f)
   f.close()
   
   # Check if the name is in name_list (local_names.pkl)
   if name in name_list:
      print "Yes"
   else:
      print "No"

   for x in range

   print riddles
   print diction['1.0']
   print riddles[1.0]
   print name  
   print name_list
   print name_list['name']



main()