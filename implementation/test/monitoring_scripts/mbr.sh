#!/bin/bash
> $1/mbr.sha
while [ 1 ]
do
	dd if=/dev/sda of=$1/.mbr.bin bs=512 count=1
	sha256sum $1/.mbr.bin | cut -d " " -f 1  >> $1/mbr.sha
	rm $1/.mbr.bin
	sleep $2
done
