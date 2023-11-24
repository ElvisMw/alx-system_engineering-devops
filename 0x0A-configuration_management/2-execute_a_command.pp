#!/bin/bash/pup
# 2-execute_a_command.pp

exec { 'killmenow':
command => 'pkill -f killmenow',
onlyif  => 'pgrep -f killmenow',
path    => '/usr/bin:/bin', # Specify the path to the pkill and pgrep commands
}
