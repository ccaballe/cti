#!/bin/bash
BASEPATH=`dirname $0`/../input_T1158_HiddenFiles/output_test
mkdir -p $BASEPATH
monitoring_scripts/monitoring.sh $BASEPATH
sleep 5
docker exec -it ubuntu-test-mitre bash -c "echo 'malicious payload' >> /home/developer/.hiddenFile"
sleep 5
monitoring_scripts/killmonitoring.sh $BASEPATH
