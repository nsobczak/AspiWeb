#######
# TP2 #
#######

# TODO : Tout le programme
# ____________________________________________________________________________________________________
# Config

# Import
import logging
import argparse
import os
import sys
import urllib
import urllib3
#import bs4


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________


# ____________________________________________________________________________________________________
# Fonctions d'initialisation

def initLog():
    """
    log format
    logging.basicConfig(datefmt='', format='%asctime', level=logging.INFO)
    """
    logging.basicConfig(
        filename="AspiWeb.log", \
        datefmt="%d/%m/%Y-%H:%M:%S", \
        format="%(asctime)s %(levelname)s %(funcName)s %(message)s", \
        level=logging.INFO)  # 'filename': '/path/to/DirectorySupervisor.debug.log',
    logging.info("Programme lance")


def initVariables():
    """
    Fonction qui initialise les variables en fonction de ce que l'utilisateur a entre.
    La fonction genere une info recapitulant la liste des parametres entres.
    """
    parser = argparse.ArgumentParser(description='Aspirateur de site avec "AspiWeb"')
    # obligatoire
    parser.add_argument("savePath", type=str, help="path where to stock the website on the computer")
    parser.add_argument("url", type=str, help="url of the website to download")
    parser.add_argument("logConf", type=str, help="path to the configuration file of the logger")
    # optionnel
    parser.add_argument("-d", "--depth", default=2, help="depth of the tree, default = 2")
    parser.add_argument("-sf", "--sizeFile", default=10, help="max size of a downloadable file")
    parser.add_argument("-sd", "--sizeDirectory", default=100,
                        help="size max of the directory where to download the website")

    # affichage des arguments rentres
    args = parser.parse_args()
    logging.info(
        ":\npath to the directory where to save the downloaded website: %s\n" + \
        "url of the website to download: %s \npath to the configuration file of the logger: %s\n" + \
        "depth of the tree: %d\nmax size of a downloadable file: %d\nsize max of the directory where to download the website: %d\n",
        args.savePath, args.url, args.logConf, args.depth, args.sizeFile, args.sizeDirectory)


# ___________________________________________________________________________________________________
# Fonctions de creation de l'arbre du dossier et de comparaison


# ___________________________________________________________________________________________________
# Fonctions principales

def loop():
    """
    fonction principale
    """

    return 1


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
def monMain():
    initVariables()
    initLog()
    loop()


if __name__ == "__main__":
    monMain()
