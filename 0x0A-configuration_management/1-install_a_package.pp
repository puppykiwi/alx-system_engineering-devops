# install puppet-lint

# Install Python
package { 'python3':
  ensure => installed,
}

# Install Pip
package { 'python3-pip':
  ensure => installed,
  require => Package['python3'],
}

# Install a Python module using Pip
package { 'requests':
  ensure   => installed,
  provider => 'pip3',
  require  => Package['python3-pip'],
}
