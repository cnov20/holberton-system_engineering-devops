# This manifest creates a puppet file, to install a package
# Specifically, puppet-lint - which ensures proper syntax / readability
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem'
}
