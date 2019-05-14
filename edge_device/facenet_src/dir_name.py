import os
from os.path import dirname

RD = os.path.dirname(os.path.realpath(__file__))
ED  = os.path.dirname(RD)

print "os.path.dirname(os.path.realpath(__file__)) ", RD
print "os.path.dirname(RD) ", ED
print (dirname(dirname(os.path.realpath(__file__)))+'/tracking')
