# Install openface requirements and facenet requirements
sudo apt install python-pip

git clone git@github.com:davidsandberg/facenet.git
cd facenet
for line in $(printf "npyscreen\nflask\n" | cat requirements.txt -)
do
	pip install $line
	pip3 install $line
done


# Communication
sudo apt install openssh-server
sudo apt install nmap
sudo apt install python-tk
