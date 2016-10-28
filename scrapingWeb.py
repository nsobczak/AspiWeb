"""
###########
# AspiWeb #
###########

@author: Vincent Reynaert
"""

# %% TODO :
#  ____________________________________________________________________________________________________
#  Config

import requests as req
from bs4 import BeautifulSoup


# %% ____________________________________________________________________________________________________
#   ____________________________________________________________________________________________________
#   Fonctions

def listOfLinks(url):
    """
    Renvoie la liste des liens contenus dans une page html pour une url
    :param url: url du code html a afficher
    :type url: str
    :return: return content of an html page and its list of links
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
        #print(hrefs)
        return (prettiSoup, hrefs)

    except:
        print("\nVeuillez entrer une url valide.\n")
        pass

# %%___________________________________________________________________________________________________

def listOfImages(url):
    """
    Renvoie la liste des images contenues dans une page html pour une url
    :param url: url du code html a afficher
    :type url: str
    :return: return list of images contained in html page
    :rtype: list
    """
    try:
        r = req.get(url)  # recuperation de l'url
        soup = BeautifulSoup(r.content, "html.parser")  # recuperation du contenu de l'url
        prettiSoup = soup.prettify()  # mise en forme du contenu de l'url
        # print(prettiSoup + "\n")
        images = soup.find_all('img')
        # print(links + "\n")

        # Creation de la liste
        srcs = []
        for img in images:
            srcs += [img.get('src')]
        #print(srcs)
        return (srcs)

    except:
        print("\nVeuillez entrer une url valide.\n")
        pass

# %% Test
url = "http://localhost/EatMVC/index.php?action=accueil"
print(listOfImages(url))
print(listOfLinks(url))
# url1 = ""
# listOfImages(url1)
# listOfLinks(url1)
# url2 = "https://www.youtube.com/watch?v=3xQTJi2tqgk"
# listOfImages(url2)
# listOfLinks(url2)

# %%___________________________________________________________________________________________________
