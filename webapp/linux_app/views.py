import model.reco as reco
from model.reco import running
from django.views.generic import View
from django.shortcuts import render
import pandas as pd
import json


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
        json_records = df.to_json(orient ='records')
        arr = []
        arr = json.loads(json_records)
        contextt = {
            'd': arr
            }

        return  render(request, 'result.html', contextt)

 # Create your views here.
def index(request):
    return render(request,'index.html')
