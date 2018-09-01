#!/bin/bash
OUTPUT_DIR=$1
mkdir -p $OUTPUT_DIR
sysdig-probe-loader
sysdig -w $OUTPUT_DIR/testcontainer.scap.gz container.name=ubuntu-test-mitre &
echo $! > $OUTPUT_DIR/.sysdig-pid.file
tcpdump -idocker0 -nn -w $OUTPUT_DIR/testcontainer.pcap &
echo $! > $OUTPUT_DIR/.tcpdump-pid.file
