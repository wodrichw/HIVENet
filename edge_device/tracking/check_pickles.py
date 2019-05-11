import pickle

f1 = open("pickles/send_pkg.pkl", 'r')
f2 = open("pickles/local_names.pkl", 'r')

foreign = pickle.load(f1)
local = pickle.load(f2)

f1.close()
f2.close()

print "\n"
print foreign
print "\n"
print local
print "\n"

# Prints dictionary in element
print local[0]

# Prints specific position in dictionary
print local[0]['name']