#!/bin/env bash
# Install ufw
# configuring ufw firewall to block incoming traffic
# allow ports 22, 443, and 80

apt-get install ufw
ufw default deny incoming
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable

# Configure port forwarding from 8080 to 80
ufw allow 8080/tcp
echo "
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
" >> /etc/ufw/before.rules

# Reload UFW to apply changes
ufw reload
