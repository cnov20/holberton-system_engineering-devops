# This manifest automates web server / web stack debugging
# By finding and replacing erroneously named Wordpress filename in WP settings

file { '/var/www/html/wp-settings.php':
  ensure => present,
}->
file_line { 'Append a line to /var/www/html/wp-settings.php':
  path => '/var/www/html/wp-settings.php',
  line => '.php',
  match   => ".phpp"
