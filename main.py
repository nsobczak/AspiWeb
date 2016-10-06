#######
# TP2 #
#######

# TODO : Tout le programme
# ____________________________________________________________________________________________________
# Config

# Import
import logging
import logging.config
import argparse
import os
import sys
import urllib
import urllib3


# import bs4


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
# Fonctions d'initialisation

def initLog():
    """
    log format
    logging.basicConfig(datefmt='', format='%asctime', level=logging.INFO)
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


# ___________________________________________________________________________________________________
# Fonctions de creation de l'arbre du dossier et de comparaison


# ___________________________________________________________________________________________________
# Fonctions principales

def loop(logger, args):
    """
    fonction principale
    """
    logger.info(
        ":\nLoop end if directory size reach: %d\n", args.sizeDirectory)

    return 1


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
def monMain():
    MAIN_LOGGER = initLog()
    ARGS = initVariables(MAIN_LOGGER)
    loop(MAIN_LOGGER, ARGS)


if __name__ == "__main__":
    monMain()
