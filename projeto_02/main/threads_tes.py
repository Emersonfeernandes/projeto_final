from ast import arg
from requests.sessions import Session
from threading import Thread,local
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
from django.core.validators import URLValidator
from requests import get
from bs4 import BeautifulSoup
from multiprocessing import Pool




def scrapin(l):
    #T = nx.Graph()
    x = []
    if l[0:4] == 'http':
        #T.add_node(l)
        respos= get(l)
        taga = BeautifulSoup(respos.text, 'html.parser')
        urls = taga.findAll('a')
        for linka in urls:
            linke = linka.get('href')
            x.append(linke)
            
    return x


def scrap(l):
    x = []
    val = URLValidator()
    try:
        if val(l):
            resposta = get(l)
            tags = BeautifulSoup(resposta.text, 'html.parser')
            titulo = tags.findAll('a')
            for links in titulo:
                link = links.get('href')
                if not link[0:4] == 'http':
                    continue
                else:
                    x.append(link)
    except:
        pass
    return x


def scrap1(l):
    x = []
    #val = URLValidator()
    try:
        if l[0:4] == 'http':
            resposta = get(l)
            if resposta.status_code == 200:
                tags = BeautifulSoup(resposta.text, 'html.parser')
                titulo = tags.findAll('a')
                for links in titulo:
                    link = links.get('href')
                    if not link[0:4] == 'http':
                        continue
                    else:
                        x.append(link)
        else:
            x.append('não_link')
    except:
        pass
    
            
    return x