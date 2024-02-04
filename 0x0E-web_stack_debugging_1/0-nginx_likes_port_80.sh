#!/usr/bin/env bash
# This sets port 80
sed -i "s/listen 8080 default_server;/listen 80 default_server;/" /etc/nginx/sites-enabled/default
sed -i "s/listen \[::\]:8080 default_server ipv6only=on;/listen \[::\]:80 default_server;/" /etc/nginx/sites-enabled/default
sed -i "s/ ipv6only=on//" /etc/nginx/sites-available/default
service nginx restart
