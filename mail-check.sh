#!/bin/bash

OFFLINEIMAP=$(which offlineimap)
while true; do
  MBOX=$( timeout --signal=KILL 35m python /home/valentin/bin/mail-idle.py ) || {
      echo "idle timed out" >&2;
      MBOX="TIMEOUT";
    }
  echo "wait result: $MBOX"
  if [ "TIMEOUT" == $MBOX ];
  then
    echo "performing full offlineimap sync"
    CMD=$OFFLINEIMAP
  else
    DIR=$(echo $MBOX | cut -d ',' -f 1)
    ACCOUNT=$(echo $MBOX | cut -d ',' -f 2)
    CMD="$OFFLINEIMAP -a $ACCOUNT -f $DIR"
    notify-send "New mail for account $ACCOUNT in folder $DIR"
  fi
  echo "running $CMD"
  timeout --signal=KILL 1m $CMD || {
     echo "offlineimap timed out" >&2;
     continue;
  }
  notmuch new
  pkill -SIGTERM+12 i3blocks
done
