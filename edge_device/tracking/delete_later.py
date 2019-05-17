# import pickle
# f = open('merge_these.pkl', 'w')
# listt = [{'name': 'sven_node_192.168.0.116', 'node1': 1, 'node2': 0, 'node3': 0, 'riddle': 1.1},
#          {'name': 'sven_node_255.255.2.255'},
#          {'name': 'sven_node_123.123.123.1'}]
# pickle.dump(listt, f)
# f.close()

# f = open('riddle_list.pkl', 'r')
# riddle = pickle.load(f)
# f.close()

# print riddle

name = "Andrew Davis_node_192.168.0.116"
underscore = 0
count_num = False
real_pos = 0
for x in range(len(name)):
   if underscore == 0 or underscore == 1 and not count_num:
      if name[x] == "_":
         underscore += 1
         print "underscore found"
   elif underscore == 2 and not count_num:
      count_num = True  
      pos = x
      print "pos: ", pos
      print name[pos]      #right after second _
      # name[pos] == _
      for y in range(pos, len(name)):
         real_pos += 1

# real_pos = len(name) - pos
ip = name[-real_pos:]
print "ip: ", ip