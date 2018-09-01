#!/bin/bash
BASEPATH=`dirname $0`/../input_T1168_LocalJobScheduling_cron/output_test
monitoring_scripts/monitoring.sh $BASEPATH
sleep 5
docker exec -it ubuntu-test-mitre sudo bash -c 'echo "* * * * * /malicious_script.sh" >> /etc/crontab'
docker exec -it ubuntu-test-mitre sudo bash -c 'echo "* * * * * /malicious_script.sh" >> /etc/cron.d/malicious_job'
docker exec -it ubuntu-test-mitre sudo bash -c 'crontab -l'
sleep 5
monitoring_scripts/killmonitoring.sh $BASEPATH
