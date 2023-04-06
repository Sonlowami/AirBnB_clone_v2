#!/usr/bin/env bash
# This script sets the environment for deployment on my web servers
#
# Step 1: Install nginx if not present
apt-get update
apt-get upgrade -y
apt install nginx

# Step 2: Set up required directories and files
mkdir -p /data/web_static/releases/test
mkdir /data/web_static/shared
printf "Welcome to my AirBnB\n" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown --recursive ubuntu:ubuntu /data
sed -i '^\tserver_name.*/a \n\\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\ttry_files $uri $uri/ =404;\n}' /etc/nginx/sites-enabled/default
service nginx restart
