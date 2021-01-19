def organizar_listas_por_tamanho(listas):
  n_comparacoes = len(listas)-1
  index_de_comparacao = 0
  for lista in listas:
    while index_de_comparacao < n_comparacoes:
      elemento = listas[index_de_comparacao]
      vizinho = listas[index_de_comparacao+1]
      if len(elemento) < len(vizinho):
        del listas[index_de_comparacao+1]
        listas.insert(index_de_comparacao,vizinho)
      index_de_comparacao+=1
    index_de_comparacao = 0
  return listas