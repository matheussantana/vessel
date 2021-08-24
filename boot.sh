#!/usr/bin/env bash

ls ~/.ssh/

ln -s ./sec-info/.env .env

sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io

yum -y install git
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
#sudo yum -y install docker
sudo service docker start
sudo docker run hello-world
sudo systemctl enable docker

ls -la

sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose
docker-compose --version

cd applet/
sh init.sh

docker ps

# Keep Alive SSH Connection
echo 'ClientAliveInterval 3600' | sudo tee --append /etc/ssh/sshd_config
echo 'ClientAliveCountMax 3' | sudo tee --append /etc/ssh/sshd_config

cat /etc/ssh/sshd_config
sudo service sshd restart

