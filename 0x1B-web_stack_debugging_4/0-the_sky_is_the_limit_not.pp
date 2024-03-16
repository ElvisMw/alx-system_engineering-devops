# Puppet manifest to optimize Nginx configuration for handling increased traffic load.

# Adjust the ULIMIT setting to increase Nginx's file descriptor limit
exec { 'adjust-nginx-ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Nginx service restart to apply the configuration changes
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
