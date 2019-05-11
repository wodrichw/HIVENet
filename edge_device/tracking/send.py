import requests 
import tarfile
import subprocess
import json
from flask import jsonify
import os
import pickle

# Note, this all assumes only 2 connected devices

def sendPickle(ip, RD, contents):
   try:
      r = requests.post('http://' + ip + ':5000/update_names', files = contents)
      print ip, "sent successfully"
   except:
      print ip, "failed to send files"
   # try:
   #      classifierF = open(RD+'/assets/classifier.pkl','r')
   #      namesF = open(RD+'/assets/names.txt','r')
   #      try:
   #          files = {"classifier":classifierF,"names":namesF}
   #          r = requests.post('http://'+ip+':5000/update_classifier', files=files)
   #          print(ip, "sent successfully")
   #      except: 
   #          print(ip, "failed to send files")
   #      finally: 
   #          classifierF.close()
   #          namesF.close()
   #  except: 
   #      print("Files not found: " + RD + '/assets/names.txt or ' + RD+'/assets/classifier.pkl')

def sendToEdgeDevices(RD=os.path.dirname(os.path.realpath(__file__))):
   print RD
   SD = os.path.dirname(RD)
   SD = SD + '/communication/client/scripts'
   # Get the IP of edge device
   p = subprocess.Popen(SD + '/getIPs.sh', shell=True, stdout=subprocess.PIPE)
   IPaddr = str(p.communicate()[0]).split(',')
   print IPaddr

   PD = RD + '/pickles/send_pkg.pkl'
   f = open(PD, 'r')
   contents = pickle.load(f)
   f.close()

   print contents[0]
   print contents[1]

   x = 0
   for ip in IPaddr:
      sendPickle(ip, RD, contents[x])
      x += 1

if __name__ == "__main__":
    sendToEdgeDevices()