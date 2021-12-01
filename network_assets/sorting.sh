#!/bin/bash


grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' results_resolve_ip.txt > all_ipv4.txt
