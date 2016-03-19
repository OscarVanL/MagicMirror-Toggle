#!/bin/sh
# /etc/init.d/pingPhone

### BEGIN INIT INFO
# Provides:		pingPhone
# Required-Start:	$remote_fs $syslog
# Required-Stop:	$remote_fs $syslog
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	MagicMirror on/off
# Description:		A script to turn MagicMiror on/off dependent on phone status
### END INIT INFO
PATH=/bin:/usr/bin:/sbin:/usr/sbin

python /home/pi/Documents/mirrorManagement.py
