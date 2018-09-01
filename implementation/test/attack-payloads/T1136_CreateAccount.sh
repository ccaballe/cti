#!/bin/bash
BASEPATH=`dirname $0`/../input_T1136_CreateAccount/output_test
monitoring_scripts/monitoring.sh $BASEPATH
sleep 5
docker exec -it ubuntu-test-mitre bash -c "useradd attacker"
sleep 5
monitoring_scripts/killmonitoring.sh $BASEPATH
