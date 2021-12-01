#!/bin/bash

cat open-ports.txt | grep "Host" | awk '{print $2}' | sort -u > cleaned-ports.txt 

for ip in $(cat cleaned-ports.txt);

do

        echo "nmap $ip -T3 -sV -oX $ip.xml -p" > $ip.txt
        cat open-ports.txt | grep "Host" | awk '{print $2,$5}' | sed 's/[open/tcp]//g' | grep "$ip" | awk '{print $2}' | xargs | sed 's/ /,/g' |  sort -u >> $ip.txt
        cat $ip.txt  | xargs > $ip
        rm $ip.txt 

done
