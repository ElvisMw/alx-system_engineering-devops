# 3-nginx_puppet_manifest.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
                listen 80;
                server_name _;
                
                location / {
                    return 301 /redirect_me;
                }
                
                location /redirect_me {
                    return 301 http://$hostname/;
                }
                
                location / {
                    add_header X-Served-By $hostname;
                    return 200 'Hello World!';
                }
            }",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  hasrestart => true,
}
