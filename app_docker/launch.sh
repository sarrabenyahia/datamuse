#!/bin/bash

bash data_getter.sh ./data.csv
ds=$(date)
echo 'Data updated on: ' ${ds}
docker run --mount type=bind,source="$(pwd)",target=/app datamuse $1
