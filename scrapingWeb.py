"""
###########
# AspiWeb #
###########

@author: Vincent Reynaert
"""

import requests as req
from bs4 import BeautifulSoup

# %%___________________________________________________________________________________________________
def affiche(url):
    """
    Affiche le code html pour une url
    :return: hrefs = c'est quoi ? liste des liens ?
    """
    try :
        r = req.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        prettiSoup = soup.prettify()
        #print(prettiSoup + "\n")
        links = soup.find_all('a')
        #print(links + "\n")

        # Creation de la liste
        hrefs = []
        for link in links :
            hrefs += [link.get('href')]
        print(hrefs)
        return(hrefs)

    except :
        print("\nVeuillez entrer une url valide.\n")
        pass

# Test
url = "http://localhost/EatMVC/index.php?action=accueil"
affiche(url)
url1 = ""
affiche(url1)
url2 = "https://www.youtube.com/watch?v=3xQTJi2tqgk"
#affiche(url2)

# %%___________________________________________________________________________________________________

