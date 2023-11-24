#!/bin/bash
#Using Puppet, install flask from pip3.
file { '/tmp/school':
ensure  => present,
content => 'I love Puppet',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
}
