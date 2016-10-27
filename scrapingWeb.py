import requests as req
from bs4 import BeautifulSoup

def affiche(url):
    """Affiche le code html pour une url"""
    try :
        r = req.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        prettiSoup = soup.prettify()
        print(prettiSoup)
        print("\n")
        links = soup.find_all('a')
        print(links)
        print("\n")
        hrefs = []
        for link in links :
            hrefs += [link.get('href')]
        print(hrefs)
        return(hrefs)
    except :
        print("\nVeuillez entrer une url valide.\n")
        pass

url = "http://localhost/EatMVC/index.php?action=accueil"
affiche(url)
url1 = ""
affiche(url1)
url2 = "https://www.youtube.com/watch?v=3xQTJi2tqgk"
#affiche(url2)
