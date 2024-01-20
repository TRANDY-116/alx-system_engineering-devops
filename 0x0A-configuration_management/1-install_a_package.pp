# Install a package "flask" in this case
package { 'python3.8':
ensure => '3.0.10',
}

package { 'python3-pip':
ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
ensure   => '2.2.2',
require  => Package['python3-pip'],
provider => 'pip',
}
