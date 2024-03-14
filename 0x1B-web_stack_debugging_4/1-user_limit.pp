# Puppet manifest to increase file descriptor limit for the holberton user

# Execute a command to increase file descriptor limit for the holberton user
exec { 'increase-file-limit-for-holberton':
  command     => 'ulimit -n 65535',
  user        => 'holberton',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'test "$(id -u)" = "$(id -u holberton)" && ulimit -n < 65535',
  refreshonly => true,
}

# Execute a command to increase file descriptor limit system-wide
exec { 'increase-file-limit-system-wide':
  command     => 'echo "* hard nofile 65535" >> /etc/security/limits.conf && echo "* soft nofile 65535" >> /etc/security/limits.conf',
  path        => ['/bin', '/usr/bin'],
  unless      => 'grep -E "^\s*\*\s+hard\s+nofile\s+65535\s*$" /etc/security/limits.conf && grep -E "^\s*\*\s+soft\s+nofile\s+65535\s*$" /etc/security/limits.conf',
  refreshonly => true,
}
