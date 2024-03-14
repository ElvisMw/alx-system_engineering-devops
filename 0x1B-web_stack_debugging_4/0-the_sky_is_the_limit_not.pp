# Puppet manifest to optimize Nginx configuration

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Manage Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  source  => 'puppet:///modules/nginx/nginx.conf',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Manage Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define Nginx site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}