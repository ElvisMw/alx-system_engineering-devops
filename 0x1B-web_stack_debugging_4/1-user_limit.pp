# Puppet manifest to increase file descriptor limit for the holberton user

# Execute a command to increase hard file descriptor limit for the holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

# Execute a command to increase soft file descriptor limit for the holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
