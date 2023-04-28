from googlesearch import search 
import requests
from lxml import html 

# print("Anuncios")
# for link in search('"drones preço" adverts', stop=10):
#     adverts = link
#     print(link)

# for i in link

print("Pesquisas")
for link in search('"relogio inteligente preço" google', stop=10):
    result = link
    print(link)


for i in link :
  url= i 
  req = requests.get(url)
  tree = html.fronstring(req.text)
  titulo = tree.xpath("body.div.name$") 










    


# // sincronização de fornecedor e anuncio 
# // 

# // precificação minima no mercado livre 
# // precificação minima no facebook
# // precificação minima do shoppe
# // precificação minima no alieexpress

# //calcular valor do mercado 
# // preço medio 
# // clientes fornecedores (- preço) (+ confiavel)

# // valor custo+lucro ser  abaixo do preço medio (vale a pena)
# // listar produtos que valem a pena a revenda.

#  produto| modelo| preço| oferta media| custo| lucro | vale a pena? | link

# Pegar produtos para mineração
# Produto | modelo| preço| oferta media| custo| link

# Listar Valores por webscrapper


