#!/bin/sh

### BEGIN INIT INFO
# Provides:          odroidlcd
# Required-Start:    $local_fs
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start odroidlcd service by djjproject
### END INIT INFO


PATH=/sbin:/bin:/usr/sbin:/usr/bin

DAEMON="/home/odroidlcd/run.sh"


# See if the daemon is there
test -x $DAEMON || exit 0

case "$1" in
	start)
		echo "## START ODROIDLCD SERVICE..."
		start-stop-daemon --start --quiet --oknodo --exec $DAEMON
		;;

	stop)
		echo "## STOP ODROIDLCD SERVICE..."
		start-stop-daemon --stop --quiet --oknodo --exec $DAEMON
		;;

	restart|force-reload)
		$0 stop && sleep 2 && $0 start
		;;

	*)
		echo "## USAGE : service odroidlcd start & stop & restart"
		exit 1
		;;
esac

