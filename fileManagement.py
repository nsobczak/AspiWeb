"""
#######
# TP2 #
#######

@author: Nicolas Sobczak
"""

# %% TODO : finir la fonction qui remplace les url d'un fichier html
#  ____________________________________________________________________________________________________
#  Config

# Import
import os


# %% ____________________________________________________________________________________________________
#   ____________________________________________________________________________________________________
#   Fonctions

def fileWrite(path, fileName, chaineAEcrire):
    """
    fonction qui ecrit une chaine de caracteres dans un fichier
    :return: void
    """

    # %% Repertoire             # os.path.join(path, fileName) si besoin
    os.chdir(path)

    # %% Creation et Ecriture
    f = open(fileName, 'w')
    f.writelines(chaineAEcrire)
    f.close()


# %%___________________________________________________________________________________________________
def searchStringInString(stringAAnalyser, stringARechercher):
    """
    Fonction qui remplace les noms de domaines externes d'un fichier html par un un nom de domaine interne
    :return: une liste contenant le nombre de <href="> puis le nombre de <src=">
    """

    result = stringAAnalyser.count(stringARechercher)
    print("nombre d'iterations de " + stringARechercher + " = " + str(result))
    return result


def fileReplace(fileName):
    """
    Fonction qui remplace les noms de domaines externes d'un fichier html par un un nom de domaine interne
    :return: void
    """

    # %% Repertoire             # os.path.join(path, fileName) si besoin
    path = os.getcwd()

    # %% Lecture
    f = open(fileName, 'r')
    html = f.readlines()
    f.close()

    # %% Remplacement
    longueur = len(html)
    i = 0
    """
    while (i < longueur):

        i+=1
    """

    searchStringInString(html, "href")

    return html
