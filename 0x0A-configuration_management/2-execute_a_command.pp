#!/bin/bash/pup
# 2-execute_a_command.pp.

exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1]
}

