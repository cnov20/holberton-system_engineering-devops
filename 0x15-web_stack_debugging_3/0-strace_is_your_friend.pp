# This manifest automates web server / web stack debugging
# By finding and replacing erroneously named Wordpress filename in WP settings

exec {
  command => 'puppet module install puppetlabs-stdlib'
}

file { '/var/www/html/wp-settings.php':
  include stdlib
  ensure => present,
}

file_line { 'Append a line to /var/www/html/wp-settings.php':
  path  => '/var/www/html/wp-settings.php',
  line  => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' )",
  match => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' )"
}
