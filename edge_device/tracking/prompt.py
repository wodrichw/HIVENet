import sys
import pickle

def open_file(fname):
   f = open(fname, 'r')
   ret = pickle.load(f)
   f.close()

   return ret

# Get rid of '_node_ip'
def get_just_name(name):
   underscore = 0
   count_num = False
   real_pos = 0
   for x in range(len(name[0])):
      if name[0][x] == '_':
         real_pos = x
         break
   ret_name = name[0][:real_pos]
   return ret_name

def get_og_num(riddle):
   str_riddle = str(riddle)
   str_riddle = str_riddle[:1]
   int_riddle = float(str_riddle)
   return int_riddle

def get_answer(riddle, riddle_list, riddle_num):
   for x in range(len(riddle_list)):
      if riddle in riddle_list[x]:
         pos = x
   return riddle_list[pos]['answer'], riddle_list[pos][riddle], riddle_list[pos][riddle_num]

def main(name, LND, RLD):
   # Open names list
   print "\n\n\n"
   name_list = open_file(LND)
   node_num_list = []

   # Open riddle list
   riddle_list = open_file(RLD)

   riddle_num = None

   for x in range(len(name_list)):
      if name[0] == name_list[x]['name']:
         riddle_num = name_list[x]['riddle']
         node_num_list.append(name_list[x]['node1'])
         node_num_list.append(name_list[x]['node2'])
         node_num_list.append(name_list[x]['node3'])
         break
   # Get just the name, without the ip address
   final_name = get_just_name(name)

   # Get the original riddle number
   og_riddle_num = get_og_num(riddle_num)

   # Get the original question from riddle_list list and answer
   riddle_answer, og_riddle, hint = get_answer(og_riddle_num, riddle_list, riddle_num)

   # Interact with the user
   print "\n\nHello %s! Welcome back to HIVENet\n\n" %(final_name)

   cont = True
   while cont:
      answer_riddle = raw_input("Would you like to attempt your riddle? y/n ")      # if yes, enter loop, if no, exit this portion
      if answer_riddle == 'y':
         cont = False
         cont_two = True
      elif answer_riddle == 'n': 
         sys.exit("\nSee you later %s...\n\n" %(final_name))
      else:
         print "Invalid input: y/n"

   while cont_two:
      print "\nYour original riddle was:", og_riddle
      cont_three = True
      while cont_three:
         hint_prompt = raw_input("\nDo you want a hint? y/n ")
         if hint_prompt == 'y':
            print "Hint:", hint
            cont_three = False
         elif hint_prompt == 'n':
            cont_three = False
         else:
            print "Invalid input: y/n"
      user_answer = raw_input("\nWhat is your answer? ")
      if user_answer in riddle_answer:
         print "\nWOOOHOOOOO!! YOU GOT IT! Check out another device."
         cont_two = False
      else:
         print "\nOooooooo that's wrong. Check out another device for another hint.\n"
         cont_two = False
   print "\nSee you later %s...\n\n" %(final_name)
   print "\n\n\n"

# main('sven-sven_node_10.248.63.164', 'local_names.pkl', 'riddle_list.pkl')