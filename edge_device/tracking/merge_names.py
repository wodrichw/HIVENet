import pickle
import subprocess
import re

def add_to_local(pos, name, LND):
   f = open(LND, 'rb')
   name_list = pickle.load(f)
   name_list.append(name)
   f.close()

   f = open(LND 'wb')
   pickle.dump(name_list, f)
   f.close()

def merge(MTD, LND):
   # Open merge_these.pkl file
   f = open(MTD, 'rb')
   received_names = pickle.load(f)
   f.close()

   f = open(LND, 'rb')
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
   ips = [re.findall(r'[0-9]+(?:\.[0-9]+){3}', nameDict['name'] )[0] for nameDict in received_names]

   # Find the corresponding name in local_names list that belongs to this computer's ip addr
   #     Just compare ip list to computer's ip (IPaddr)
   pos = ip.index(IPaddr)
   
   # Take that position, and append it into the local_names.pkl
   add_to_local(pos, received_names[pos], LND)

   #     Get just the name of any element from received_names
   for x in range(len(local_names)):
      if local_names[x]['name'] == received_names[0]['name']:
         print "Yaaas"
         print received_names[0]['name']
         print local_names[x]['name']
   #     Iterate through the local_names until you get a match with the received name
   # Add to local_names.pkl

# merge()