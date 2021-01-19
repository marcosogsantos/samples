import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import ast
import random

def funcao_lista_db():
  try: db = open('db_trends.txt','r').read()
  except:
    open('db_trends.txt','w').write('[]')
    db = open('db_trends.txt','r').read()
  db = eval(db)
  return db

def atualizar_objeto_do_db(obj_novo,db):
  pesquisa = obj_novo['pesquisa']
  for obj_no_db in db:
    if obj_no_db['pesquisa'] == pesquisa:
      for chave in obj_no_db.keys():
        obj_no_db[chave] = obj_novo[chave]
  open('db_trends.txt','w').write(str(db))

def adicionar_obj_ao_db(objeto):
  l_db = funcao_lista_db()
  pesquisas_no_db = []
  for obj_db in l_db:
    pesquisas_no_db.append(obj_db['pesquisa'])
  if objeto['pesquisa'] not in pesquisas_no_db:
    l_db.append(objeto)
    open('db_trends.txt','w').write(str(l_db))
  else:
    atualizar_objeto_do_db(objeto,funcao_lista_db())

def lista_de_objetos_em_ordem_descrescente_segundo_valor_de_uma_chave(listas,chave):
  n_comparacoes = len(listas)-1
  index_de_comparacao = 0
  for lista in listas:
    while index_de_comparacao < n_comparacoes:
      elemento = listas[index_de_comparacao]
      vizinho = listas[index_de_comparacao+1]
      if elemento[chave] < vizinho[chave]:
        del listas[index_de_comparacao+1]
        listas.insert(index_de_comparacao,vizinho)
      index_de_comparacao+=1
    index_de_comparacao = 0
  return listas

def imprimir_resultados(db):
  for objeto in db:
    print(objeto['pesquisa'],objeto['quantia'],objeto['fonte'])

def procurar_trends():
  global driver
  print('N. objetos no DB: {} '.format(len(funcao_lista_db())))
  print('Defindo elementos Trends...')
  elemento_trend = driver.find_elements_by_tag_name('md-list')
  l_de_obj_trends = []
  if len(elemento_trend) > 0:
    for elem in elemento_trend:
      l_textos = elem.text.split('\n')
      if len(l_textos) > 5:
        obj_trend = {
          'pesquisa': None,
          'manchete': None,
          'fonte':None,
          'quantia':None,
          'link': None,
          'img': None,
        }
        obj_trend['pesquisa'] = l_textos[1]
        obj_trend['manchete'] = l_textos[2]
        obj_trend['fonte'] = l_textos[3]
        str_quantia = l_textos[4].replace('+','').replace('de','').split(' ')
        str_quantia2 = []
        for x in str_quantia:
          if len(x)>0:
            str_quantia2.append(x)
        str_quantia = str_quantia2
        n_quantia = int(str_quantia[0])
        str_quantia = str_quantia[1].replace(' ','')
        if str_quantia == 'mil':
          n_quantia = n_quantia * 1000
        elif str_quantia == 'mi':
          n_quantia = n_quantia * 1000000
        obj_trend['quantia'] = n_quantia
        parentes = elem.find_elements_by_tag_name('a')
        if obj_trend['link'] == None:
          obj_trend['link'] = parentes[0].get_attribute('href')
        imagens = elem.find_elements_by_tag_name('img')
        if obj_trend['img'] == None:
          try:
            obj_trend['img'] = imagens[0].get_attribute('src')
          except:pass
        l_de_obj_trends.append(obj_trend)
        adicionar_obj_ao_db(obj_trend)
  return l_de_obj_trends

def iniciar_navegador():
  global driver
  print('Iniciando navegador...')
  chrome_options = webdriver.ChromeOptions()
  prefs = {"profile.default_content_setting_values.notifications" : 2,'profile.managed_default_content_settings.images':2}
  chrome_options.headless = True
  chrome_options.add_argument("log-level=3")
  chrome_options.add_experimental_option("prefs",prefs)
  driver = webdriver.Chrome(options=chrome_options,service_log_path=None)
  print('Acessando o Google Trends...')
  driver.get('https://trends.google.com.br/trends/trendingsearches/daily?geo=BR')
  time.sleep(3)
  trends = procurar_trends()
  driver.quit()
  print('Navegador finalizado.')

#INICIAR FUNÇÕES
iniciar_navegador()
objetos_em_ordem_descrescente = lista_de_objetos_em_ordem_descrescente_segundo_valor_de_uma_chave(funcao_lista_db(),'quantia')
for obj in objetos_em_ordem_descrescente:
  print(obj['pesquisa'],obj['quantia'])