import os
from os.path import dirname
import sys
import pickle
sys.path.append(dirname(dirname(os.path.realpath(__file__)))+'/communication/client')
from client import sendTrackingDataToEdgeDevices

# Assemble directory paths
RD = os.path.dirname(os.path.abspath(__file__)) 
ED  = os.path.dirname(RD)+"/edge_device"
communicationDir = ED+"/communication"
clientDir = communicationDir+"/client"

class People:
   def __init__(self):
      try:
         f = open(RD +"people.pkl", 'rb')
         self.people = pickle.load(f)
         f.close()
      except:
         self.people = dict()

   
   def __del__(self):
      self.save()

   def person_travel_log(self, key):
      if self.people:
         return self.people[key]['seen_at']
      return None

   def add_person(self, key):
      self.people[key] = {'seen_at': [], 'solved_riddle': False}   

   def add_location(self, key, location):
      try:
         self.people[key]
      except KeyError:
         self.add_person(key)

      if not location in self.people[key]['seen_at']:
         self.people[key]['seen_at'].append(location) 

   def save(self):
      f = open(RD + "/people.pkl", 'w')
      pickle.dump(self.people, f)
      print("\n\n\n\n\n\n\n")
      f.close()

   def check_face_for_update(self, key, location):
      if not location in self.person_travel_log(key):
         self.add_location(key, location)
         # Send updated info to other edge devices
         sendTrackingDataToEdgeDevices(key, location, clientDir)