import model.reco as reco
from model.reco import running
from django.views.generic import View
from django.shortcuts import render
import pandas as pd
import json
import random
import os


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'index.html', context)

def home(request):
    if request.method == "POST":
        get_cherche  = request.POST.get("cherche_moi_ca_stp")
        df = reco.running('./model/data.csv',f"{get_cherche}")
        df = df.reset_index()

        df_random = pd.read_csv('./model/data.csv', sep=";")
        random_number = random.randrange(df_random.shape[0])
        df_random = df_random.loc[[random_number], ['title','lead_text','date_start','date_end','address_street','price_type','url']]

        json_records = df.to_json(orient ='records')
        arr = []
        arr = json.loads(json_records)

        json_records_random = df_random.to_json(orient ='records')
        arr_random = []
        arr_random = json.loads(json_records_random)

        contextt = {
            'd': arr,
            'r': arr_random,
            }

        return  render(request, 'result.html', contextt)
        
 # Create your views here.
def index(request):
    return render(request,'index.html')
