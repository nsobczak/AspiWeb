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

# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________


# ____________________________________________________________________________________________________
# Fonctions d'initialisation

def initLog(logPath):
    """
    log format
    logging.basicConfig(datefmt='', format='%asctime', level=logging.INFO)
    """
    logging.basicConfig(
        filename=logPath + "/AspiWeb.log", \
        datefmt="%d/%m/%Y-%H:%M:%S", \
        format="%(asctime)s %(levelname)s %(funcName)s %(message)s", \
        level=logging.INFO)     # 'filename': '/path/to/DirectorySupervisor.debug.log',
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
    parser.add_argument("-s", "--sizeFile", default=10, help="size max of a downloadable file")
    parser.add_argument("-s", "--sizeDirectory", default=100, help="size max of the directory where to download the website")

    #parser.add_argument("-st", "--supervisionTime", default=60, help="add supervision time (in sec), default = 60 sec")

    # initialisation des parametres globaux
    args = parser.parse_args()
    dp = args.dp
    lp = args.lp
    depth = int(args.depth)
    frequence = int(args.frequence)
    supervisionTime = int(args.supervisionTime)
    startinglevel = dp.count(os.sep)        # indique le niveau de profondeur initiale
    arbrePrecedent = createSurveyList(list(os.walk(dp)))


def afficheArgument():
    """affichage des arguments rentres"""
    logging.info(
        ":\npath to the directory : %s \npath where to generate log : %s \ndepth of the directory : %s \nfrequency : %s hz \nsupervision time : %s sec\n",
        dp, lp, depth, frequence, supervisionTime)


# ___________________________________________________________________________________________________
# Fonctions de creation de l'arbre du dossier et de comparaison


# ___________________________________________________________________________________________________
# Fonctions principales

def loop():
    """
    si stop() => arret
	sinon
		compareArbre()
    """
    global arbrePrecedent
    totalTime = 0
    oldTime = time.time()
    newTime = time.time()
    while totalTime < (supervisionTime*frequence):
        newTime = time.time()
        if (newTime - oldTime) > (1 / frequence):
            # logging.info(str(totalTime / frequence) + " sec depuis lancement du programme")
            oldTime = time.time()
            nouvelArbre = createSurveyList(list(os.walk(dp)))
            M, A, D = comparateSurveyList(arbrePrecedent, nouvelArbre)
            if len(M) or len(A) or len(D):
                arbrePrecedent = nouvelArbre
                logTheMADLists(M, A, D)
            totalTime += 1
    return 1


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
def monMain():
    initVariables()
    initLog()
    afficheArgument()
    loop()


if __name__ == "__main__":
    monMain()
