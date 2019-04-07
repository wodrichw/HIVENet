#Install for HIVENet
#python
#pip
#requirements.txt
#nmap
#openssh-server
#python-tk

sudo apt install python
sudo apt install python-pip

for line in $(cat requirements.txt -)
do
	pip install $line
	pip3 install $line
done


#Communication
sudo apt install openssh-server
sudo apt install nmap
sudo apt install python-tk
