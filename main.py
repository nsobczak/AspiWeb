"""
###########
# AspiWeb #
###########

@author: Julien Vermeil and Vincent Reynaert and Nicolas Sobczak
"""

# %%TODO : Loop function
#  ____________________________________________________________________________________________________
#  Config

# Import
import logging
import logging.config
import argparse
import fileManagement as fM
import os
import sys
import urllib
import urllib3

import requests as req
from bs4 import BeautifulSoup


# %%____________________________________________________________________________________________________
#  ____________________________________________________________________________________________________
#  Fonctions d'initialisation

def initLog():
    """
    log format
    logging.basicConfig(datefmt='', format='%asctime', level=logging.INFO)    :param fileName: nom du fichier dans lequel remplacer les liens
    :return: MAIN_LOGGER
    :rtype: log
    """
    logging.config.fileConfig("AspiWebLog.conf")
    # definition du handler
    MAIN_LOGGER = logging.getLogger("test_log")

    MAIN_LOGGER.info("Programme lance")
    # MAIN_LOGGER.critical("Ceci est une erreur critique !")
    # MAIN_LOGGER.warning("Ceci est un message de debogage !")
    return MAIN_LOGGER


def initVariables(logger):
    """
    Fonction qui initialise les variables en fonction de ce que l'utilisateur a entre.
    La fonction genere une info recapitulant la liste des parametres entres.
    :param logger: logger
    :type logger: log
    :return: ARGS
    :rtype: list ?
    """
    PARSER = argparse.ArgumentParser(description='Aspirateur de site avec "AspiWeb"')
    # obligatoire
    PARSER.add_argument("savePath", type=str, help="path where to stock the website on the computer")
    PARSER.add_argument("url", type=str, help="url of the website to download")
    PARSER.add_argument("logConf", type=str, help="path to the configuration file of the logger")
    # optionnel
    PARSER.add_argument("-d", "--depth", type=int, default=2, help="depth of the tree, default = 2")
    PARSER.add_argument("-sf", "--sizeFile", type=int, default=10, help="max size of a downloadable file")
    PARSER.add_argument("-sd", "--sizeDirectory", type=int, default=100,
                        help="size max of the directory where to download the website")

    # affichage des arguments rentres dans le log
    ARGS = PARSER.parse_args()
    logger.info(
        ":\npath to the directory where to save the downloaded website: %s\n" + \
        "url of the website to download: %s \npath to the configuration file of the logger: %s\n" + \
        "depth of the tree: %d\nmax size of a downloadable file: %d\nsize max of the directory where to download the website: %d\n",
        ARGS.savePath, ARGS.url, ARGS.logConf, ARGS.depth, ARGS.sizeFile, ARGS.sizeDirectory)

    return ARGS


# %%___________________________________________________________________________________________________
#  Fonctions principales

def loop(logger, args):
    """
    Fonction principale
    :param logger: logger
    :param args: arguments entres en ligne de commande
    :type logger: log
    :type args: list
    :return: 1
    :rtype: int
    """
    logger.info(
        ":\nLoop end if directory size reach: %d\n", args.sizeDirectory)

    # Recuperation du contenu de la page html et enregistrement dans un fichier
    r = req.get(args.url)  # recuperation de l'url
    soup = BeautifulSoup(r.content, "html.parser")  # recuperation du contenu de l'url
    prettiSoup = soup.prettify()  # mise en forme du contenu de l'url
    fM.fileWrite(args.savePath, "index.html", prettiSoup)

    # Recuperation du contenu du fichier precedemment enregistre, analyse de ses liens et remplacement si necessaire
    logger.info(
        ":\nFichier lu: %s\n", fM.fileReplace("index.html", args.url))

    # Test
    # On recupere les liens sous la forme: images/code-couleur.gif
    print("needLinkToBeReplace: 'images/code-couleur.gif' -> ",
          fM.needLinkToBeReplace('images/code-couleur.gif', args.url))
    print("needLinkToBeReplace: 'www.images.com/code-couleur.gif' -> ",
          fM.needLinkToBeReplace('www.images.com/code-couleur.gif', args.url))
    print("needLinkToBeReplace: 'https://github.com/nsobczak/AspiWeb/projects/1?fullscreen=true' -> ",
          fM.needLinkToBeReplace('https://github.com/nsobczak/AspiWeb/projects/1?fullscreen=true', args.url))
    print("needLinkToBeReplace: 'https://www.youtube.com/watch?v=M6JpxDebokM' -> ",
          fM.needLinkToBeReplace('https://www.youtube.com/watch?v=M6JpxDebokM', args.url))

    return 1


# %%____________________________________________________________________________________________________
#  ____________________________________________________________________________________________________
def monMain():
    MAIN_LOGGER = initLog()
    ARGS = initVariables(MAIN_LOGGER)
    loop(MAIN_LOGGER, ARGS)


if __name__ == "__main__":
    monMain()
