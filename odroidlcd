#!/bin/sh

### BEGIN INIT INFO
# Provides:          odroidlcd
# Required-Start:    $remote_fs $all
# Required-Stop:     $remote_fs $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: odroidlcd init script
# Description:       initscript by djjproject
### END INIT INFO


DESC="odroidlcd"
NAME=odroidlcd
PIDFILE=/var/run/$NAME.pid
COMMAND="/usr/bin/python3 /home/odroidlcd/hello_world.py"
RUN_AS=root

d_start() {
    start-stop-daemon --start --quiet --background --make-pidfile --pidfile $PIDFILE --chuid $RUN_AS --exec $COMMAND
}

d_stop() {
    start-stop-daemon --stop --quiet --pidfile $PIDFILE
    if [ -e $PIDFILE ]
        then rm $PIDFILE
    fi
    /usr/bin/python3 /home/odroidlcd/lcdoff.py
}

case $1 in
    start)
    echo -n "Starting $DESC: $NAME"
    d_start
    echo "."
    ;;
    stop)
    echo -n "Stopping $DESC: $NAME"
    d_stop
    echo "."
    ;;
    restart)
    echo -n "Restarting $DESC: $NAME"
    d_stop
    sleep 1
    d_start
    echo "."
    ;;
    *)
    echo "usage: $NAME {start|stop|restart}"
    exit 1
    ;;
esac

exit 0
