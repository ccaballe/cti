#!/bin/bash
BASEPATH=`dirname $0`/../input_T1067_Bootkit/output_test
mkdir -p $BASEPATH
monitoring_scripts/mbr.sh $BASEPATH 2 &
echo $! > $BASEPATH/.mbr-pid.file
sleep 10
# Random sha256 to simulate mbr has been altered
echo $RANDOM | sha256sum  | cut -d " " -f 1  >> $BASEPATH/mbr.sha >> $BASEPATH/mbr.sha
kill -15 `cat $BASEPATH/.mbr-pid.file`
