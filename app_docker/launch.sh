#!/bin/bash

bash data_getter.sh ./target/data.csv

echo "Recommendation system computing"
sudo docker run --mount type=bind,source="$(pwd)"/target,target=/app datamuse $1 $2 
echo "     "
sleep 1s
echo "Hacking Nasa"
sleep 1s
echo "Loading ..."
sleep 0.2s
echo "20%"
sleep 0.2s
echo "40%"
sleep 0.2
echo "60%"
sleep 0.2
echo "80%"
sleep 0.2
echo "99%"
sleep 2s
echo "Nasa hacked"
sleep 1s
echo "..."
sleep 2s 
echo "Just kidding, end of recommendation system"
