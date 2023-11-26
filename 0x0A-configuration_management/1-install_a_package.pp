#!/usr/bin/puppet
# 1-install_a_package

package { 'flask':
ensure   => '2.1.0',
provider => 'pip3',
}
