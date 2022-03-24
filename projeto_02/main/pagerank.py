from ast import arg
from http.server import ThreadingHTTPServer
import networkx as nx
from requests import get
from bs4 import BeautifulSoup
import concurrent.futures
from threading import Thread
from main.threads_tes import scrapin, scrap, scrap1
from multiprocessing import Pool, Process


#FUNÇÃO QUE RASPA OS LINKS DO URL DE ENTRADA NO FORMS 
def pageRank(u):
    lista1 = []
    
    resposta = get(u)
    tags = BeautifulSoup(resposta.text, 'html.parser')
    titulo = tags.findAll('a')
    for links in titulo:
        link = links.get('href')
        if not link[0:4] == 'http':
            continue
        else:
            lista1.append(link)
    return lista1

#FUNÇÃO QUE RANKEIA OS LINKS E PEGA OS CINCO PRIMEIROS USANDO A BIBLIOTECA NETWORKX.    
def func(lista):
    G = nx.Graph()
    x = []
    for lin in lista:
        if lin == None:
            continue
        else:
            G.add_node(lin)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future = executor.submit(scrapin, lin)
            return_value = future.result()
            #x.append(return_value)
            for i in return_value:
                for v3 in lista:
                    if v3 == None or i == None:
                        continue
                    else:
                        if v3 == i:
                            G.add_edge(lin, i)
    
    dic = dict(nx.degree_centrality(G))
    dic_sor = sorted(dic, key = dic.get,reverse = True)
    n = dic_sor[0:5]

    #ppr1 = nx.pagerank(G)
    #x = ppr1.keys()
    
    return n


#FUNÇÃO QUE RASPA OS LINKS DE CADA UM DOS CINCO URLS
def links_of_links(l):
    x = []
    x.clear()
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
    

#FUNÇÃO QUE RANKEIA OS LINKS DE CADA UM DOS CINCO URLS USANDO A BIBLIOTECA NETWORKX,
# E PEGA O PRIMEIRO URL DE CADA.
def testan(l):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            FUTURE = executor.submit(links_of_links, l)
            RETURN = FUTURE.result()

    G = nx.Graph()
    for lin in RETURN:
        if lin == None:
            continue
        else:
            G.add_node(lin)
        #t = Thread(target=scrapin, args=(lin,))
        #t.start()        #lista_u.append(link)
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future = executor.submit(scrapin, lin)
            return_value = future.result()
            #x.append(return_value)
            for i in return_value:
                for v3 in RETURN:
                    if v3 == None or i == None:
                        continue
                    else:
                        if v3 == i:
                            G.add_edge(lin, i)
    
    dic = dict(nx.degree_centrality(G))
    dic_sor = sorted(dic, key = dic.get,reverse = True)
    n = dic_sor[0:1]
    
    return n



if __name__ == '__main__':
    p = Process(target=func, args=(arg,))
    p.start()
    p.join

if __name__ == '__main__':
    p = Process(target=links_of_links, args=(arg,))
    p.start()
    p.join