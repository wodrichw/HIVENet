git clone --recursive https://github.com/cmusatyalab/openface.git ~/openface
sudo -i 
apt-get update && apt-get install -y \
    curl \
    git \
    graphicsmagick \
    libssl-dev \
    libffi-dev \
    python-dev \
    python-pip \
    python-numpy \
    python-nose \
    python-scipy \
    python-pandas \
    python-protobuf \
    python-openssl \
    wget \
    zip \
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

