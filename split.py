
stringText = "https://www.youtube.com/"

def linkSplit(url):
    return url.split('/')[2]


print(linkSplit(stringText))