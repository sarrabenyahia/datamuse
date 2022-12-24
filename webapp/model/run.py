#!/bin/bash
import os
import sys
import subprocess


command_dataget = 'bash data_getter.sh data.csv'
os.system(command_dataget)
    
search = sys.argv[1]
command_recherche = f'python reco.py ./data.csv {search}'
os.system(command_recherche)


