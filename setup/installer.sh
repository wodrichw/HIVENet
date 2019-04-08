# Install openface requirements and facenet requirements
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py


git clone git@github.com:davidsandberg/facenet.git
cd facenet
for line in $(cat requirements.txt)
do
	pip install $line
	pip3 install $line
done


# Communication
sudo apt install openssh-server
sudo apt install nmap
sudo apt install python-tk
