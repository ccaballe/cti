#!/bin/bash
BASEPATH=`dirname $0`/../input_T1168_LocalJobScheduling_at/output_test
monitoring_scripts/monitoring.sh $BASEPATH
sleep 5
docker exec -it ubuntu-test-mitre sudo bash -c 'atd'
docker exec -it ubuntu-test-mitre sudo bash -c 'echo "echo malicious_payload" | at tomorrow'
sleep 5
monitoring_scripts/killmonitoring.sh $BASEPATH
