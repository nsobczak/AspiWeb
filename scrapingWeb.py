"""
###########
# AspiWeb #
###########

@author: Vincent Reynaert
"""

# %% TODO :
#  ____________________________________________________________________________________________________
#  Config

import urllib.request as ur
import requests as req
from bs4 import BeautifulSoup


# %% ____________________________________________________________________________________________________
#   ____________________________________________________________________________________________________
#   Fonctions
def extractHTML(url):
    """
    Renvoie la liste des liens contenus dans une page html pour une url
    :param url: url du code html a afficher
    :type url: str
    :return: return content of an html page
    :rtype: bs4.BeautifulSoup
    """
    try :
        r = req.get(url)  # recuperation de l'url
        soup = BeautifulSoup(r.content, "html.parser")  # recuperation du contenu de l'url
        #prettiSoup = soup.prettify()  # mise en forme du contenu de l'url
        return soup
    except:
        print("\nVeuillez entrer une url valide.\n")
        return None
        pass

# %%___________________________________________________________________________________________________

def downloadFile(urlFile, fileRegisterPath):
    """
    Renvoie le contenu d'une page html
    :param urlFile: lien absolu vers l'image a telecharger
    :param fileRegisterPath: path where you want to register your file (end whit the name of the file)
    :type urlFile: str
    :type fileRegisterPath: str
    """
    ur.urlretrieve(urlFile, fileRegisterPath)


# %%___________________________________________________________________________________________________

def listOfLinks(soup):
    """
    Renvoie la liste des liens contenus dans une page html pour une url
    :param soup: url du code html a afficher
    :type : bs4.BeautifulSoup
    :return: return list of links of the html code
    :rtype: list
    """
    links = soup.find_all('a')

    # Creation de la liste
    hrefs = []
    for link in links:
        hrefs += [link.get('href')]
    return (hrefs)



# %%___________________________________________________________________________________________________

def listOfImages(soup):
    """
    Renvoie la liste des images contenues dans une page html pour une url
    :param soup: code html a traiter
    :type soup: bs4.BeautifulSoup
    :return: return list of images contained in html page
    :rtype: list
    """
    images = soup.find_all('img')

    # Creation de la liste
    srcs = []
    for img in images:
        srcs += [img.get('src')]
    return (srcs)


# %% Test
url = "http://localhost/TestPhpStorm/index.php"
soup = extractHTML(url)
print(listOfImages(soup))
print(listOfLinks(soup))
# url1 = ""
# listOfImages(url1)
# listOfLinks(url1)
# url2 = "https://www.youtube.com/watch?v=3xQTJi2tqgk"
# listOfImages(url2)
# listOfLinks(url2)

# %%___________________________________________________________________________________________________
