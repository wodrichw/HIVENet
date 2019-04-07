# HIVENet

HIVENets is a research project that tackles Neural Network optomization. This project uses facial recognition software on a end-node that then informs a centralized node of its findings to be then shared across all other nodes. 

---

## Purpose

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
- Run <em> installer.sh </em>

---
## Setup

#### Both Computers
- Must be connected to router
- Need 3 separate terminal windows
- Terminal (1) - Setup First
    - Navigate to <em> /HIVENet/communication/server </em> directory
    - Run <em>python server.py</em>
- Terminal (2) - Setup second
    - Move to <em> /HIVENet/edge_device </em> directory
    - Run command <em> python interface.py </em>
        - Note the IP address produced after "Running on" in terminal. This should be the fourth *

- Terminal (3) - Setup third
    - Navigate to <em>/HIVENet/edge_device</em> directory
        
---

## Goal of Execution
Recognized on computer one, the after instructions are followed, you are now recognizable again on computer two

---

## Execution
<p> Execute the test in descending order of the instructions, from "Computer One" down.

#### Computer One
- Terminal (1) - Let Run

- Terminal (2) - Let Run

- Terminal (3) - Interact
    - Open Google Chrome
        - Redirect to IP address outlined above under Setup -> Both Computers -> Bullet 4 -> Sub-Bullet 2
        - Enter name in textbox under <em>Help Us Recognize Your Face</em>
        - Press submit
        - Follow text moving across screen and wait once it stops
            - Note: your picture is being taken here. Please use a small variety of different facial expressions
        - Once photos load on screen, you can either retake them or submit. Submit will continue the process

    - To see completed recognition on the same computer, do the following:
        - Navigate to <em> /HIVENet/edge_device </em>
        - Run <em> recognition.py </em>
        - Observe that the system now recognizes you.
    - Otherwise, continue
#### Computer Two
- Terminal (1) - Let Run

- Terminal (2) - Let Run

- Terminal (3) - Interact with <u>after</u> steps taken on Computer One

    - Navigate to <em> /HIVENet/edge_device </em>
    - Run <em> recognition.py </em>
    - Observe that the system now recognizes you.

---

## Results
As stated in the purpose above, between 

---

## Additional Notes