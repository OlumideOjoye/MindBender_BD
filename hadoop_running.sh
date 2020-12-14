#!/bin/bash

results=$(jps)

echo "${results}"
if [[ "${results}" == *"NameNode"* ]]; then
echo "Hadoop is Running"
else
echo "Hadoop is not running, now starting hadoop"
eval start-all.sh

fi
