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

# name = "Andrew-Davis_node_192.168.0.116"
# underscore = 0
# count_num = False
# real_pos = 0
# underscore = 0    # Counts number of underscore
# count_num = False # Skips final loop when necessary
# real_pos = 0      # Final position to parse
# for x in range(len(name)):
#    if underscore != 2:
#       underscore += 1
#    if underscore == 2:
#       real_pos = x + 1
#       break
# print real_pos
# ip = name[-real_pos:]
# print ip
# # real_pos = len(name) - pos
# ip = name[-real_pos:]
# print "ip: ", ip


names = [[],[]]
names[0].append('andrew_1')
names[1].append(1)

print names

if 'andrew' not in names[0]:
   names[0].append('andrew')
   names[1].append(1)
else:
   pos = names[0].index('andrew')
   names[1][pos] += 1
print names