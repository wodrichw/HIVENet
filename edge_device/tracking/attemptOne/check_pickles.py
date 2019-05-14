import pickle

f1 = open("pickles/send_pkg.pkl", 'r')
f2 = open("pickles/local_names.pkl", 'r')
f3 = open("pickles/rec_py_face.pkl", 'r')

foreign = pickle.load(f1)
local = pickle.load(f2)
faces = pickle.load(f3)

f1.close()
f2.close()
f3.close()

print "\n"
print foreign
print "\n"
print local
print "\n"
print "faces: ", faces
print "\n"

# Prints dictionary in element
print local[0]

# Prints specific position in dictionary
print local[0]['name']