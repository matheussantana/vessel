#!/usr/bin/env bash

# core cleanup
rm -r /tmp/secure*
rm ./snapshot/*.img

docker-compose down -v
docker-compose -f docker-compose.yml -f docker-compose.yml.portainer -f docker-compose.yml.owncloud down -v

docker system prune -a
docker rm -vf $(docker ps -a -q)
docker rmi -f $(docker images -a -q)

rm -r ./stdio/var/*


# app cleanup
rm ./bin/webserver/www/wp/wp-config.php


#rm -r sec-info/

echo 'DOCUMENT_ROOT=./stdio/www
VHOSTS_DIR=./stdio/config/vhosts
APACHE_LOG_DIR=./stdio/var/logs/apache2
PHP_INI=./stdio/config/php/php.ini

# If you want to use mariadb instead of mysql use "mariadb"
DATABASE=mysql

MYSQL_DATA_DIR=./stdio/var/data/mysql
MYSQL_LOG_DIR=./stdio/var/logs/mysql

# If you already has the port 80 in use, you can change it (for example if you have Apache)
HOST_MACHINE_UNSECURE_HOST_PORT=80
HOST_MACHINE_SECURE_HOST_PORT=443

# If you already has the port 3306 in use, you can change it (for example if you have MySQL)
HOST_MACHINE_MYSQL_PORT=3306

# If you already has the port 6379 in use, you can change it (for example if you have Redis)
HOST_MACHINE_REDIS_PORT=6379


# MySQL root user password
MYSQL_ROOT_PASSWORD=mysqladm

# Database settings: Username, password and database name
MYSQL_USER=docker
MYSQL_PASSWORD=docker
MYSQL_DATABASE=docker



OWNCLOUD_VERSION=10.7
OWNCLOUD_DOMAIN=127.0.0.1:8081
OWNCLOUD_ADMIN_USERNAME=admin
OWNCLOUD_ADMIN_PASSWORD=admin
OWNCLOUD_HTTP_PORT=8081



REDIS_PASSWORD=redis111

VNC_PASSWORD=vncvnc' > ./sec-info/.env