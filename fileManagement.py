"""
#######
# TP2 #
#######

@author: Nicolas Sobczak
"""

#%% TODO : fonction qui ecrit une chaine de caracteres dans un fichier
#  ____________________________________________________________________________________________________
#  Config

# Import
import os


#%% ____________________________________________________________________________________________________
#   ____________________________________________________________________________________________________
#   Fonctions
def fileWrite(path, fileName, chaineAEcrire):
    """
    fonction qui ecrit une chaine de caracteres dans un fichier
    :return: void
    """

    #%% Repertoire             # os.path.join(path, fileName) si besoin
    os.chdir(path)

    #%% Creation et Ecriture
    f = open(fileName, 'w')
    f.writelines(chaineAEcrire)
    f.close()


def fileReplace(fileName):
    """
    Fonction qui remplace les noms de domaines externes d'un fichier html par un un nom de domaine interne
    :return: void
    """

    #%% Repertoire             # os.path.join(path, fileName) si besoin
    path = os.getcwd()

    #%% Lecture et remplacement
    f = open(fileName, 'r')
    test = f.readlines()
    f.close()

    return test
