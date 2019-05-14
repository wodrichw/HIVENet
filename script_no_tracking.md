# HIVENet Expo Script

## Introduction
This section covers everything up to right prior to the demonstration being started
- Introduce self 
- Very brief overview
   - In depth will be covered during demonstration
   - Points to cover:
      - Disseminated training of Neural Networks on distributed networks 
      - Shown through facial recognition across three devices
- Prompt for participation
- Yes: Outlint process
   - 30 Photos taken,
   - once done at current station, will move to next to be recognized
- No: ...move on

---

## Demonstration
This section covers the real demonstration during Expo. There are two sections. The first outlines a user who has never visited our booth, the second outlines a user who has had their face recognized at one node and is moving to another. Prompt user for their status -- "Have you been trained on another device?"

### First-Time User/Training
- Remind that 30 photos will be taken
   - If there is issue, reassure that data will be deleted post Expo
   - If no, ...move on
- Interface.py should be running, bring up this window
   - Have participant type their name (we need to standardize by lower case, first name only)
   - Begin training -- This is when in depth explanation will take place
- Explanation starts here during data alignment and classification. Extend as long as they maintain interest
   - "As stated, our 'project/______' aims to lighten the load on single devices for neural network training. Rather than collecting all data on a single device, we have three separate nodes working together. Once a new face is recognized by a device, the corresponding data and name is shared among the network. Once done, all receiving devices are then able to recognize the individual."
   - Key Points to hit:
      - Overview (above)
      - Facial recognition software used
         - Facenet -- Google developed
      - Network infrastructure
         - "Eager Synchronization System"
         - Nodes are ready to receive and send data at any point
      - 
- Once interface.py is finished, run recognize.py to test on individual
- Instruct to move to a different node, prompt for questions
   - "Before you move to another station, do you have any questions?"
   - No: Point to different stations
   - Yes: answer

### Returning User/Recognition
- Greet
- Open recognize.py
- Explain what has just happened
   - They were trained on a different node, that data was shared, and they are now recognizeable on all devices

--- 

## Follow-Up
- Emphasize purpose of project
   - Transmission of data vs. actual facial recognition
- Ask for questions again

---

## Key Points During Presentation
- There will be one person per computer, so do not take too long
- If facial recognition does not work at initial device, train again

