#!/bin/bash

bash data_getter.sh ./target/data.csv

echo "Recommendation system computing"
sudo docker run --mount type=bind,source="$(pwd)"/target,target=/app datamuse $1 $2 
echo "Hacking Nasa"
sleep 2s
echo "..."
sleep 2s 
echo "Just kidding, end of recommendation system"
