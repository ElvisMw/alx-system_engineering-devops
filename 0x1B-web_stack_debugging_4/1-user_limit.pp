# Puppet manifest to increase file descriptor limit for the holberton user

# Execute a command to increase file descriptor limit for the holberton user
exec { 'increase-file-limit-for-holberton':
  command     => 'ulimit -n 65535',
  user        => 'holberton',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'test "$(id -u)" = "$(id -u holberton)" && ulimit -n < 65535',
  refreshonly => true,
}
