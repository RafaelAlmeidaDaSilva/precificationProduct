

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')



soup = BeautifulSoup(webContent[0:300], 'html.parser')





print(soup.prettify())  

