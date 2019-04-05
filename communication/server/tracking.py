import sys
import numpy as np
import os

class tracking_system:
    def __init__(self):
        self.identified_people = {
        }
    def add_identified_person(self,name,ip,location):
        self.identified_people[name] = {ip:location}

    def add_location_of_person(self,name,ip,location):
        if self.identified_people[name] is not None:
            if self.identified_people[name][ip] is None:
                self.identified_people[name][ip] = location
        else:
            self.add_identified_person(name,ip,location)

    def get_person_locations(self,name)
        if name in self.identified_people.keys():
            locations = ''
            for key , value in self.identified_people[name]:
                locations += value + '\n'
            locations = locations[:-1]
            return locations
        else:
            return "Welcome to your first station!"