import os
from os.path import dirname

RD = dirname(os.path.realpath(__file__))
ED = dirname(dirname(RD))
classifiersDir = ED+"/classifiers"
u = dirname(dirname(dirname(os.path.realpath(__file__))))

# /HIVENet/edge_device/tracking/pickles
ND = ED + '/tracking/merge_these.pkl'

print "RD: ", RD
print "ED: ", ED
print "ND: ", ND
print "u: ", u
