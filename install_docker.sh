sudo apt-get update

sudo apt-get install -y \
    apt-transport-https \
        ca-certificates \
	    curl \
        software-properties-common

sudo curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

sudo add-apt-repository \
	   "deb [arch=amd64] https://download.docker.com/linux/debian \
	      $(lsb_release -cs) \
	         stable"

sudo apt-get update

sudo apt-get install -y docker-ce

sudo docker run hello-world
