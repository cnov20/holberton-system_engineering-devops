# This manifest creates a puppet file, to execute a command
# Specifically, that kills a process - name 'killmenow'
exec { 'killmenow':
  path    => ['/usr/bin'],
  command => 'pkill -f killmenow',
  returns => '0',
  onlyif => 'pgrep -f killmenow'
}
