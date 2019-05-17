import pickle
import os

RD = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/edge_device/tracking/local_names.pkl"
ED  = os.path.dirname(RD)
FP = RD + "/edge_device/tracking/local_names.pkl"

RRD = os.path.dirname(os.path.realpath(__file__)) + '/name.txt'

print("RD: ", RD)
print("ED: ", ED)
print("FP: ", FP)
print("RRD: ", RRD)

f = open(RD, 'w')
stuff = "Hello World"
pickle.dump(stuff, f)
f.close()

f = open(RD, 'r')
stuff_two = pickle.load(f)
print("pickle: ", stuff_two)
f.close()
