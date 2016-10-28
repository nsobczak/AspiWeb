"""
###########
# AspiWeb #
###########

@author: Julien Vermeil and Vincent Reaynaert and Nicolas Sobczak
"""

# %%TODO : Tout le programme
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


# import bs4


# %%____________________________________________________________________________________________________
#  ____________________________________________________________________________________________________
#  Fonctions d'initialisation

def initLog():
    """
    log format
    logging.basicConfig(datefmt='', format='%asctime', level=logging.INFO)
    :return: MAIN_LOGGER
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
    :return: ARGS
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
#  Fonctions de creation de l'arbre du dossier et de comparaison


# %%___________________________________________________________________________________________________
#  Fonctions principales

def loop(logger, args):
    """
    fonction principale
    :return: 1
    """
    logger.info(
        ":\nLoop end if directory size reach: %d\n", args.sizeDirectory)
    chaineTest = """
    <!DOCTYPE html>

<html>
<head>

	<meta charset="UTF-8">
	<meta name="description" content="HelloWorld">
	<meta name="keywords" content="keyworld exemple">
	<meta name="author" content="Nicolas Sobczak">

	<title>Hello World</title>

	<link rel="stylesheet" type="text/css" href="firstStyle.css">

</head>
<body>

	<h1 id="Haut"> Hello World !! </h1>

	<p>blablabla</p>

	<h2> Listes </h2>

	<h3> Listes point </h3>
	<ul>
		<li>Coucou 1</li>
		<li>Coucou 2</li>
	</ul>


	<h3> Listes n° </h3>
	<ol>
		<li>Coucou n°1</li>
		<li>Coucou n°2</li>
		<li>Coucou n°3</li>
		<li>Coucou <b>ultime</b> </li>
		<li>Coucou n°4</li>
		<li>Coucou n°5</li>
		<li>Coucou n°6</li>
	</ol>


	<h2> Liens vers autres pages </h2>

		<h3>Hello world</h3>
		<p>
		<table width="20%"style="line-height: 20px; margin-left: 60px;" border="1">
			<tr>	<!-- table row -->
				<td>Vers page 2</td>	<!-- table data -->
				<td> <a href="hello world p02.html"> <img width="20px" src="Boutons/bouton_suivant.jpg"> </a> <br/> </td>
			</tr>
			<tr>
				<td>Vers page 3</td>
				<td> <a href="hello world p03.html"> <img width="20px" src="Boutons/bouton_suivant.jpg"> </a> <br/> </td>
			</tr>
			<tr>
				<td>Vers page 4</td>
				<td> <a href="hello world p04.html"> <img width="20px" src="Boutons/bouton_suivant.jpg"> </a> <br/> </td>
			</tr>
		</table>
		</p>

		<h3>Moteurs de recherche</h3>
		<p>
		<table width="20%"style="line-height: 20px; margin-left: 60px;" border="1">
			<tr>	<!-- table row -->
				<td>Go to startpage</td>	<!-- table data -->
				<td> <a target="_blank" href="https://www.startpage.com/"> <img width="20px" src="Boutons/bouton_suivant.jpg"> </a> <br/> </td>
			</tr>
			<tr>
				<td>Go to google </td>
				<td> <a target="_blank" href="https://www.google.com/"> <img width="20px" src="Boutons/bouton_suivant.jpg"> </a> </td>
			</tr>
		</table>
		</p>




	<h2> Chat </h2>
	<h6> Image </h6>

	<img src="coscat.jpeg">

	<h2> End </h2>

	Retour en haut de la page <a href="#Haut"> <img width="20px" src="Boutons/bouton_hautDePage.jpg"> </a>

</body>
</html>

    """
    fM.fileWrite(args.savePath, "page.html", args.url)

    logger.info(
        ":\nFichier lu: %s\n", fM.fileReplace("page.html", args.url))

    return 1


# %%____________________________________________________________________________________________________
#  ____________________________________________________________________________________________________
def monMain():
    MAIN_LOGGER = initLog()
    ARGS = initVariables(MAIN_LOGGER)
    loop(MAIN_LOGGER, ARGS)


if __name__ == "__main__":
    monMain()
