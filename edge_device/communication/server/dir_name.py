import os
from os.path import dirname

RD = dirname(os.path.realpath(__file__))
ED = dirname(dirname(RD))
classifiersDir = ED+"/classifiers"

# /HIVENet/edge_device/tracking/pickles
namesDir = ED + '/tracking/pickles'

print RD
print ED
print namesDir