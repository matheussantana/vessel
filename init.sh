#!/usr/bin/env bash

#docker-compose up -d
#docker-compose up --build -d
sudo docker-compose  -f docker-compose.yml.owncloud  -f docker-compose.yml.portainer -f docker-compose.yml -f docker-compose.webserver-ssl.yml up --build -d



yum -y install epel-release htop
yum -y install python-pip
pip install boto3
#echo "0 0 * * 1-5 root python /applet/bin/ci_cd-jenkins/scripts/snapshot.py create >/dev/null 2>&1" >> /etc/crontab
#echo "0 7 * * 0 root python /applet/bin/ci_cd-jenkins/scripts/snapshot.py delete >/dev/null 2>&1" >> /etc/crontab