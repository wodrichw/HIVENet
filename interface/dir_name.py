import pickle
import os

RD = os.path.dirname(os.path.realpath(__file__))
ED  = os.path.dirname(RD)
FP = ED + "/tracking/test.pkl"

print(RD)
print(ED)
print(FP)

f = open(FP, 'w')
stuff = "Hello World"
pickle.dump(stuff, f)
f.close()

f = open(FP, 'r')
stuff_two = pickle.load(f)
print("pickle: ", stuff_two)
f.close()