from googlesearch import search 
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup



def linkSplit(url):        
    return url.split('/')[2]


def readArq(arqTxt):
    stringSplit = open(arqTxt, 'r')
    return stringSplit.split(',')



listSiteNoCompre = readArq("listBanidos.txt")
listSiteCompre = readArq("listaSitesCompra.txt")

#listSiteNoCompre = ["youtube.com", "facebook.com"]

#listSiteCompre = ["www.amazon.com", "www.casasbahia.com", "www.magazine.com",
#"www.mercadolivre.com", "www.shoppe.com", "www.aliexpress.com"]




while (True):
    query= input("Search: ")

    if(query == "exit"):
        break

    cont = 0 
    for i in  search(''+ query+' adverts google', num=10,  stop=10, pause=2):
            if (listSiteCompre.index(linkSplit(i))):
                print(i)
                url = i
                response = urllib.request.urlopen(url)
                webContent = response.read().decode('UTF-8')
                soup = BeautifulSoup(webContent[0:300], 'html.parser')
                print(soup.find_all('a'))
                
                for link in soup.find_all('a'):
                    if(link.get_text().find("R$")):
                        print(link.get_text())


            else:
                cont += 1
            
    if (cont > 0 ):
       search(''+ query+' google', num=(10+cont),  stop=10, pause=2)

