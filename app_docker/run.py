import os
import sys
import subprocess

#Step 1 : On active l'environnement virutel
#command_venv = 'subprocess.run([source activate ven])'
#os.system(command_venv)

#Step 2 : On importe avec le data_getter
command_dataget = 'bash data_getter.sh data.csv'
os.system(command_dataget)


#Step 3 : On effectue la recherche 
search = sys.argv[1]
command_recherche = f'python reco.py ./data.csv {search}'
os.system(command_recherche)
#subprocess.call([command_recherche, search])

