#!/bin/bash

if [ -d ./target ];
then
    echo "target directory exists."
    echo "Removing target directory"
    rm -Rf ./target
    echo "Creating target directory"
    mkdir ./target
    echo "Target directory created successfully"
else
    echo "target directory does not exist."
  echo "Creating target directory"
  mkdir ./target
  echo "Target directory created successfully"
fi
