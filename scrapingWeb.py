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
    :param url: url du code html a afficher
    :type url: str
    :return: return description
    :rtype: list
    """
    try:
        r = req.get(url)  # recuperation de l'url
        soup = BeautifulSoup(r.content, "html.parser")  # recuperation du contenu de l'url
        prettiSoup = soup.prettify()  # mise en forme du contenu de l'url
        # print(prettiSoup + "\n")
        links = soup.find_all('a')
        # print(links + "\n")

        # Creation de la liste
        hrefs = []
        for link in links:
            hrefs += [link.get('href')]
        print(hrefs)
        return (hrefs)

    except:
        print("\nVeuillez entrer une url valide.\n")
        pass

# %% Test
# url = "http://localhost/EatMVC/index.php?action=accueil"
# affiche(url)
# url1 = ""
# affiche(url1)
# url2 = "https://www.youtube.com/watch?v=3xQTJi2tqgk"
# affiche(url2)

# %%___________________________________________________________________________________________________
