# comment
exec { 'killmenow':
  path    => '/usr/bin',
  command => 'pkill killmenow'
}
