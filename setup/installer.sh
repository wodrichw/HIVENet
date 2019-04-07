#Install for HIVENet
#python
#pip
#requirements.txt
#nmap
#openssh-server
#python-tk

sudo apt install python

sudo apt-get install python-pip

#for line in $(cat requirements.txt -)
#do
#	pip install $line
#	pip3 install $line
#done

pip install tensorflow==1.7
pip install scipy
pip install scikit-learn
pip install opencv-python
pip install h5py
pip install matplotlib
pip install Pillow
pip install requests
pip install psutil
pip install flask

#Communication
sudo apt install net-tools
sudo apt install openssh-server
sudo apt install nmap
sudo apt install python-tk
