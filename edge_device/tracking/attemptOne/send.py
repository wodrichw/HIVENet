import requests 
import tarfile
import subprocess
import json
from flask import jsonify
import os
import pickle

# Note, this all assumes only 2 connected devices

def sendPickle(ip, RD, PD):
   try:
      name_file = open(PD, 'r')
      contents = pickle.load(name_file)
      try:
         files = {"names": name_file}
         r = request.post('http://'+ip+':5000/update_names', files=files)
         print ip, " sent successfully"
      except:
         print ip, " Failed to send files"
      finally:
         name_file.close()
   except:
      print ip, "failed to send files"
   # try:
   #    files = {"content": contents}
   #    r = requests.post('http://' + ip + ':5000/update_names', files = files)
   #    print ip, "sent successfully"
   # except:
   #    print ip, "failed to send files"

def sendToEdgeDevices(RD=os.path.dirname(os.path.realpath(__file__))):
   print RD
   SD = os.path.dirname(RD)
   SD = SD + '/communication/client/scripts'
   # Get the IP of edge device
   p = subprocess.Popen(SD + '/getIPs.sh', shell=True, stdout=subprocess.PIPE)
   IPaddr = str(p.communicate()[0]).split(',')
   print IPaddr

   PD = RD + '/pickles/send_pkg.pkl'
   print PD
   # f = open(PD, 'r')
   # contents = pickle.load(f)
   # f.close()

   # print contents[0]
   # print contents[1]

   for ip in IPaddr:
      sendPickle(ip, RD, PD)

if __name__ == "__main__":
    sendToEdgeDevices()