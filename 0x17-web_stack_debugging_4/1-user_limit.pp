# This manifest automates web server / web stack debugging
# By finding and replacing user file open (process) limits for given user (holberton)

exec { 'Modify a line of /etc/security/limits.conf':
  path    => ['/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i -e 's/4/4096/g' -e 's/5/8000/g' /etc/security/limits.conf"
}
