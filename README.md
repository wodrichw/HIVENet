# HIVENet

HIVENets is a research project that tackles Neural Network optimization. This project uses facial recognition software on a end-node that then informs a centralized node of its findings to be then shared across all other nodes. 

---

## Purpose

HIVENet aims to streamline data sharing between disjoint neural network systems (e.g. mobile devices, PCs). This is demonstrated through our project through facial recognition on multiple PCs.

The purpose can be more explicitly understood in reading the design and requirements documents under the "docs" folder on our Github repository.

---

## Requirements

#### System
- Ubuntu version 18.08

#### For Recognition
- python version 2.7.15
- tensorflow version 1.7 
- scipy
- scikit-learn
- opencv-python
- h5py
- matplotlib
- Pillow
- requests
- psutil

#### For Communication
- flask
- openssh-server
- nmap
- python-tk

#### For Execution
- Two computers
- Dedicated router - no internet connectivity

#### Web Browswer
- Google Chrome

---

## Installation
- Navigate to <em> /setup </em> directory
- Run <em> sudo installer.sh </em>
- Once ran, a <em> get-pip.py </em> should appear
- Run <em> sudo get-pip.py </em>
- The system is ready for use

---
## Setup
Do all of the following before moving on to Execution.

#### Both Computers

- Must be connected to router
- Need 2 separate terminal windows

- Terminal (1) - Setup First
    - Navigate to <em> /HIVENet/edge_device </em>
    - Run <em> ./run.sh </em>
        - Note 1: Keep track of the http addresses that appear on screen. The latter, is used for user interaction on a web browser. That is, <em> localhost:5052 </em> or the local host URL presented.
        - Note 2: This shell script should be ran any time the system is restart.

- Terminal (2) - Setup Second
    - Navigate to <em> /HIVENet/edge_device/facenet_src </em>
   
---

## Goal of Execution
Individual(s) running will be recognized on computer one, the after instructions are followed, you are now recognizable again on computer two

---

## Execution
<p> Execute the test in descending order of the instructions, from "Computer One" down.

#### Computer One
- Terminal (1) - Let Run

- Open Google Chrome
    - Navigate to the URL outlined above under the "Setup" section
    - Here, enter your name in the text box provided and press submit
    - Once the submit button is hit, the interface will immediately begin taking your pictures. Follow the text across the screen
    - After pictures are taken, wait for the page to refresh. The images you just took will appear on-screen. 
        - If any of them are bad (the back/side of your head, poor lighting, etc.), you have the option to retake them. 
        - If they are mostly of the front of your face with slight adjustments in angle, you may hit submit.
    - Wait for the web interface to redirect to the page you saw at the very beginning before moving to Terminal (2)
    - Note: You can view the terminal for actions take upon image capture if you wish

- Terminal (2) Interact after image capture
    - Run <em> python recognize.py </em>
    - Upon doing this, your face will be recognized on the system
    - This step is just to confirm you are who the computer thinks you are and is not necessary
    - Move on to the second computer to see full scope of project

### Computer Two
- Terminal (1) - Let Run

- Terminal (2) - Interact
    - After you have completed the above steps, run <em> python recognize.py </em>
    - In doing so, you should see yourself recognized by the computer

---

## Results
As stated in the purpose above, you will be recognized on computer two despite never having taken pictures on it. This is due to the sharing of data between the connected nodes.

---

## Additional Notes
If you are not correctly recognized, ensure you have good lighting that shines on as much of your face as possible. The project did not develop the facial recognition portion, so there may be issues with this if images are not of high enough quality.