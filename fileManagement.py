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
def needLinkToBeReplace(stringAAnalyser):
    """
    Fonction qui examine un lien et determine s'il doit etre remplace par un lien locale ou ignore s'il s'agit d'un lien externe
    :return: booleen true si le lien doit etre remplace,
                    false sinon
    """

    if ((stringAAnalyser[0] == 'w') and (stringAAnalyser[1] == 'w') and (stringAAnalyser[2] == 'w') ):
        result = False
    else:
        result = True
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

    # Test
    # On recupere: images/code-couleur.gif
    print ( needLinkToBeReplace('images/code-couleur.gif') )
    print ( needLinkToBeReplace('www.images.com/code-couleur.gif') )

    return html
