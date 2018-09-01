#!/bin/bash
BASEPATH=`dirname $0`/../input_T1215_KernelModulesAndExtensions/output_test
monitoring_scripts/monitoring.sh $BASEPATH
sleep 5
docker exec -it ubuntu-test-mitre bash -c "sudo apt-get -y install kmod && sudo modinfo maliciousKernelModule"
sleep 5
monitoring_scripts/killmonitoring.sh $BASEPATH
