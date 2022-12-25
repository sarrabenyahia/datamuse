#!/bin/bash

echo "### STEP 1: creating target directory"
bash create_target.sh

echo "### STEP : creating docker image"
sudo docker build -t datamuse .
