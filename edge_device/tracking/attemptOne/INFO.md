# /Tracking

Directory contains code for tracking system of HIVENet

## Files
- check_pickles.py: 
   - Opens the .pkl files in <em>/tracking/pickles<em> and prints the content
- name.txt: 
   - The newly inputted name from interface.py
- new_name.py:
   - Process the data when a new name is inputted from interface.py
   - Reads names.txt
   - Saves data to <em> /tracking/pickles/send_pkg.pkl <em>
- rcvd_name.py
   - Unwritten
- send.py:
   - Acts as client, sends information to a server that is listening on the same port
- prompt_riddle.py:
   - This takes the name from rec_py_face.pkl and prints the corresponding riddle
- setup.py:
   - Initializes the riddle list
   - Initializes the local names stored on the machine to prevent error when possibly reading from empty list
- test.py:
   - random stuff
- isolated_version:
   - Directory for reference
- pickels -- directory that contains needed .pkl files
   - local_names.pkl:
      - all the names stored on "this" machine
   - rec_py_face.pkl:
      - the face listened from recognize.py
   - riddle_list.pkl
      - Directory with the riddles
      - This is the same across all machines
   - send_pkg.pkl:
      - This is populated then sent to the other nodes