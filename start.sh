#!/usr/bin/env bash

#docker-compose up --build -d
#mkdir -p /applet/stdio/var/logs/mysql
#mkdir -p /applet/stdio/var/data/mysql
#mkdir -p /applet/stdio/var/logs/apache2
sudo docker-compose  -f docker-compose.yml.owncloud  -f docker-compose.yml.portainer -f docker-compose.yml -f docker-compose.webserver-ssl.yml up --build -d
