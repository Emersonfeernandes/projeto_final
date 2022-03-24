from django.http import request
from requests import get
from threading import Thread
from multiprocessing import Pool, Process
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect


import requests
from .models import Url_Scraper
from .forms import UserForm
import concurrent.futures
from .pagerank import pageRank, func, testan


lista = [] #LISTA QUE VAI RECEBER OS URLS

#FUNÇÃO DA VIEW QUE RETORNA O ARQUIVO HOME.HTML NA PASTA TEMPLATES
#ESSE IMPRIME O FORMULARIO NA TELA, E VEREFICA SE É VALIDO
def home(request):
    form = UserForm(request.POST or None)
    submitbutton = request.POST.get("submit")
    

#mudei aqui    
    URL = str    
    var = []
    if form.is_valid():
        lista.clear()
        URL = form.cleaned_data["URL"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future = executor.submit(pageRank, URL)
            return_value = future.result()
        
        var = func(return_value)
        n = var[0:5]
    
       
        for x in var:
            i = testan(x)
            lista.append(x)
            for h in i:
                lista.append(h)
            lista.append(i)
        print(var)

    context = {"form":form, "lista_rank":lista, "submitbutton":submitbutton}

    return render(request=request, template_name="home.html", context=context)



def resultado(request):
    return render(request=request, template_name="resultado.html", context={"lista":lista})
    #return render(request=request, template_name="home.html", context={"URL_save" : Url_Scraper.objects.all})

if __name__ == '__main__':
    processes = Process(target=home, args=(request,))
    processes.start()
    processes.join()