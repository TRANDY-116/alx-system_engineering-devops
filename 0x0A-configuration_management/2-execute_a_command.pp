# Executing a command
exec { 'kill_process':
command => 'pkill killmenow',
path    => '/bin:/usr/bin:/usr/localbin',
}
