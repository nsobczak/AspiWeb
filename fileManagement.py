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
def isLinkRelativ(link):
    """
    fonction qui analyse si un lien est relatif ou pas
    :return: 1 booleen
    """
    result = True
    if ((link.find('www') != -1) or (link.find('http') != -1)):
        result = False
    return result


def getDomain(urlSiteAAspirer):
    """
    fonction qui recupere le nom de domaine du site a partir de son url
    :return: String = nom de domaine du site
    Le site peut etre des formes suivantes: https://www.<domain> | https://<domain> | http://www.<domain> | http://<domain> | www.<domain>
    """
    print("\nurlSiteAAspirer:", urlSiteAAspirer," | isLinkRelativ: ", isLinkRelativ(urlSiteAAspirer))
    domain = urlSiteAAspirer
    if not isLinkRelativ(urlSiteAAspirer):
        if (urlSiteAAspirer.find('www.') != -1):
            print(urlSiteAAspirer.split('www.'))
            domain = urlSiteAAspirer.split('www.')[-1]
            domain = domain.split('/')[0]
            print("domaine: ", domain)

    return domain


def needLinkToBeReplace(stringAAnalyser, urlSiteAAspirer):
    """
    Fonction qui examine un lien et determine s'il doit etre remplace par un lien local ou ignore s'il s'agit d'un lien externe
    :return: booleen true si le lien doit etre remplace,
                    false sinon
    """
    if isLinkRelativ(stringAAnalyser):
        result = False
    else:
        getDomain(stringAAnalyser) # <= a remplacer par : urlSiteAAspirer
        result = True
    return result


def fileReplace(fileName, urlSiteAAspirer):
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

    # %% Remplacement des liens s'ils doivent l'etre.
    longueur = len(html)
    i = 0
    """
    while (i < longueur):

        i+=1
    """

    # Test
    # On recupere: images/code-couleur.gif
    print ("needLinkToBeReplace: ", needLinkToBeReplace('images/code-couleur.gif', urlSiteAAspirer) )
    print ("needLinkToBeReplace: ", needLinkToBeReplace('www.images.com/code-couleur.gif', urlSiteAAspirer) )

    return html
