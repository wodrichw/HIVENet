
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

apt install curl
apt install gcc
apt install openssh-server
apt install nmap
apt install python-tk
apt install net-tools
apt install python-dev 

# Install openface requirements and facenet requirements
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

for line in $(cat requirements.txt)
do
	pip install $line
done

