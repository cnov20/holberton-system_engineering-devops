# This manifest creates a puppet file, to execute a command
# Specifically, that modifies the U_LIMIT on an nginx web server'
exec { 'sed; sudo service nginx restart':
  path    => ['/etc/default/nginx'],
  command => 'sed s/15/4096/g',
  returns => '0'
}
