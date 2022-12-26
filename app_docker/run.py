import os
import sys


search = sys.argv[1]
command_recherche = f'python reco.py ./data.csv {search}'
os.system(command_recherche)



