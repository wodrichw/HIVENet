import pickle
import subprocess

def conc_ip(name):
   # Parse name to get just ip address
   #     IP addr == 13 chars
   #     look for third _ and move from ther
   #     Example: andrew_node_123.123.1.123_xx
   underscore = 0    # Counts number of underscore
   count_num = False # Skips final loop when necessary
   real_pos = 0      # Final position to parse
   for x in range(len(name)):
      if underscore == 0 or underscore == 1 and not count_num:
         if name[x] == '_':
            underscore += 1
      elif underscore == 2 and not count_num:
         count_num = True
         pos = x
         for y in range(pos, len(name)):
            real_pos += 1
   ip = name[-real_pos:]

   return ip

def add_to_local(pos, name):
   f = open('local_names.pkl', 'r')
   name_list = pickle.load(f)
   name_list.append(name)
   f.close()

   f = open('local_names.pkl', 'w')
   pickle.dump(name_list, f)
   f.close()

def merge():
   # Open merge_these.pkl file
   f = open('merge_these.pkl', 'r')
   received_names = pickle.load(f)
   f.close()

   f = open('local_names.pkl', 'r')
   local_names = pickle.load(f)
   f.close()

   print "--: ", received_names[0]['name']
   # Just need to put the corresponding IP name into local names file
   # Find right name according to IP
   # Determine which name from received_names belongs to this device
   #     Get IP of this address    
   p = subprocess.Popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'", shell=True, stdout=subprocess.PIPE)
   IPaddr = p.communicate()[0].strip()

   # Get just the ip of each name in file
   ip = []
   for x in range(len(received_names)):
      ip.append(conc_ip(received_names[x]['name']))
   print "ip: ", ip

   # Find the corresponding name in local_names list that belongs to this computer's ip addr
   #     Just compare ip list to computer's ip (IPaddr)
   pos = ip.index(IPaddr)
   
   # Take that position, and append it into the local_names.pkl
   add_to_local(pos, received_names[pos])

   #     Get just the name of any element from received_names
   for x in range(len(local_names)):
      if local_names[x]['name'] == received_names[0]['name']:
         print "Yaaas"
         print received_names[0]['name']
         print local_names[x]['name']
   #     Iterate through the local_names until you get a match with the received name
   # Add to local_names.pkl

merge()