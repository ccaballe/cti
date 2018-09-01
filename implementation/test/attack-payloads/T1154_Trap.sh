#!/bin/bash
# WORKAROUND: trap does not work in containers
BASEPATH=`dirname $0`/../input_T1154_Trap/output_test
mkdir -p $BASEPATH
sysdig-probe-loader
sysdig -w $BASEPATH/testcontainer.scap.gz &
echo $! > $BASEPATH/.sysdig-pid.file
sleep 5
trap '/payload.sh' SIGTERM
sleep 5
monitoring_scripts/killmonitoring.sh $BASEPATH
