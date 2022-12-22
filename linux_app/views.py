from django.views.generic import View
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'index.html', context)

 # Create your views here.
def index(request):
    return render(request,'index.html')

import importlib
import model.reco as reco
from model.reco import running
#importlib.reload(running)

def predict(request):
    if request.method == "POST":
        get_cherche  = request.POST.get("cherche_moi_ca_stp")
        #cherche_CA = HttpResponse(get_cherche) # ça ne marche pas
        recommandation = reco.running('./model/data.csv',f"{get_cherche}")
        return render(request,'/Users/sarrabenyahia/Downloads/app/templates/result.html',{'result' : recommandation })

import os
import sys
import subprocess

# def predict(request):
#     command_dataget = 'bash data_getter.sh data.csv'
#     os.system(command_dataget)

#     get_cherche  = request.POST.get("cherche_moi_ca_stp")
#     search = HttpResponse(get_cherche)
#     command_recherche = f'python reco.py ./data.csv {search}'
#     recommandation = os.system(command_recherche)
#     (out, err) = recommandation.communicate()
#     return render(request,'/Users/sarrabenyahia/Downloads/app/templates/result.html',{'result' : recommandation })

