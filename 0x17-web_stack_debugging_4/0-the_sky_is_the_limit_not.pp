# This manifest automates web server / web stack debugging
# By finding and replacing erroneously named Wordpress filename in WP settings

exec { 'Modify a line of /etc/default/nginx':
  path    => ['/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i 's/15/4096/g' /etc/default/nginx; sudo service nginx restart"
}
