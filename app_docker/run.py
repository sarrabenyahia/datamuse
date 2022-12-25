import os
import sys



#Step 2 : On importe avec le data_getter


#Step 3 : On effectue la recherche 
search = sys.argv[1]
command_recherche = f'python reco.py ./data.csv {search}'
os.system(command_recherche)
#subprocess.call([command_recherche, search])




#Step 1 : On effectue la recherche 
#search = sys.argv[1]
#command_recherche = f'python reco.py ./datamuse/app_docker/data.csv {search}'
#os.system(command_recherche)
