"""
###########
# AspiWeb #
###########

@author: Nicolas Sobczak
"""

# %% TODO : finir la fonction qui remplace les url d'un fichier html
#  ____________________________________________________________________________________________________
#  Config

# Import
import os
import scrapingWeb as sW
import fileinput


# %% ____________________________________________________________________________________________________
#   ____________________________________________________________________________________________________
#   Fonctions

def fileWrite(path, fileName, chaineAEcrire):
    """
    Fonction qui ecrit une chaine de caracteres dans un fichier
    :param path: chemin du fichier dans lequel ecrire
    :param fileName: nom du fichier dans lequel ecrire
    :param chaineAEcrire: chaine de caracteres a ecrire dans le fichier
    :type path: str
    :type fileName: str
    :type chaineAEcrire: str
    :return: return nothing
    :rtype: void
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
    Fonction qui analyse si un lien est relatif ou pas
    :param link: lien a analyser
    :type link: str
    :return: return 1 booleen correspondant a la reponse
    :rtype: bool
    """
    result = True
    if ((link.find('www') != -1) or (link.find('http') != -1) or link.find('php') != -1):
        result = False
    return result


def getDomain(link):
    """
    Fonction qui recupere le nom de domaine du site a partir de son url
    Le site peut etre des formes suivantes: https://www.<domain> | https://<domain> | http://www.<domain> | http://<domain> | www.<domain>
    :param link: lien a analyser
    :type link: str
    :return: return le nom de domaine du site
    :rtype: str
    """

    # print("\nlink:", link," | isLinkRelativ: ", isLinkRelativ(urlSiteAAspirer))
    domain = link
    if not isLinkRelativ(link):
        if (link.find('www.') != -1):
            domain = link.split('www.')[-1]
            domain = domain.split('/')[0]
        elif (link.find('://') != -1):
            domain = link.split('://')[-1]
            domain = domain.split('/')[0]

        # # %% Comment traiter le cas suivant ?
        # # cas ou on a link = "http://localhost/EatMVC/index.php?action=accueil"
        # elif (link.find('.php')) != -1 :
        #     domain = link.split('.php')[0]
        #     domain = domain.split('/')[-1]

        else:
            domain = "ERROR" + domain

    # print("domaine: ", domain)
    return domain


def needLinkToBeReplace(stringAAnalyser, urlSiteAAspirer):
    """
    Fonction qui examine un lien et determine s'il doit etre remplace par un lien local ou ignore s'il s'agit d'un lien externe
    :param stringAAnalyser: lien a analyser
    :param urlSiteAAspirer: url du site a aspirer
    :type stringAAnalyser: str
    :type urlSiteAAspirer: str
    :return: True si le lien doit etre remplace, False sinon
    :rtype: bool
    """
    result = False
    if not isLinkRelativ(stringAAnalyser):
        # %% comparaison du domaine du lien a celui de l'url du site a aspirer
        refDomain = getDomain(urlSiteAAspirer)
        analyzedDomain = getDomain(stringAAnalyser)
        if (refDomain == analyzedDomain):
            result = True
    return result


# %%___________________________________________________________________________________________________

def fileLinksReplace(path, fileName, urlSiteAAspirer, htmlSoup):
    """
    Fonction qui remplace les noms de domaines externes d'un fichier html par un nom de domaine interne
    :param path: chemin du fichier dans lequel ecrire
    :param fileName: nom du fichier dans lequel remplacer les liens
    :param urlSiteAAspirer: url du site a aspirer
    :param htmlSoup: url du site a aspirer
    :type path: str
    :type fileName: str
    :type urlSiteAAspirer: str
    :type htmlSoup: BeautifulSoup
    :return: nothing
    :rtype: void
    """

    # %% Remplacement des liens autre que les images s'ils doivent l'etre.
    linkList = sW.listOfLinks(htmlSoup)
    for link in linkList:
        # print(link, needLinkToBeReplace(link, urlSiteAAspirer), "\n")
        if (needLinkToBeReplace(link, urlSiteAAspirer)):
            refDomain = getDomain(urlSiteAAspirer)
            analyzedDomain = getDomain(link)
            print("\nlink.replace: ",
                  link.replace(analyzedDomain, path))  # remplacement du lien dans la liste
            # remplacement du lien dans le fichier contenant le html
            with fileinput.FileInput(fileName, inplace=True) as file:
                for line in file:
                    print(line.replace(analyzedDomain, path), end='')


# %%___________________________________________________________________________________________________

def filePictureLinksReplace(path, fileName, urlSiteAAspirer, htmlSoup):
    """
    Fonction qui remplace les liens des images
    :param path: chemin du fichier dans lequel ecrire
    :param fileName: nom du fichier dans lequel remplacer les liens
    :param urlSiteAAspirer: url du site a aspirer
    :param htmlSoup: url du site a aspirer
    :type path: str
    :type fileName: str
    :type urlSiteAAspirer: str
    :type htmlSoup: BeautifulSoup
    :return: nothing
    :rtype: void
    """


    # %% Remplacement des liens autre que les images s'ils doivent l'etre.
    linkList = sW.listOfPictures(htmlSoup)
    print("\nlinkList : ", linkList)
    print("a remplacer\n")
    # for link in linkList:
    #     # print(link, needLinkToBeReplace(link, urlSiteAAspirer), "\n")
    #     if (needLinkToBeReplace(link, urlSiteAAspirer)):
    #         refDomain = getDomain(urlSiteAAspirer)
    #         analyzedDomain = getDomain(link)
    #         print("\nlink.replace: ",
    #               link.replace(analyzedDomain, path))  # remplacement du lien dans la liste
    #         # remplacement du lien dans le fichier contenant le html
    #         with fileinput.FileInput(fileName, inplace=True) as file:
    #             for line in file:
    #                 print(line.replace(analyzedDomain, path), end='')


# %%___________________________________________________________________________________________________

def fileReplace(path, fileName, urlSiteAAspirer):
    """
    Fonction qui remplace les liens
    :param path: chemin du fichier dans lequel ecrire
    :param fileName: nom du fichier dans lequel remplacer les liens
    :param urlSiteAAspirer: url du site a aspirer
    :type path: str
    :type fileName: str
    :type urlSiteAAspirer: str
    :return: nothing
    :rtype: void
    """

    # %%Recuperation du contenu de la page
    htmlSoup = sW.extractHTML(urlSiteAAspirer)

    # %% Enregistrement du fichier une fois le contenu de la page extrait
    fileWrite(path, fileName, htmlSoup.prettify())

    fileLinksReplace(path, fileName, urlSiteAAspirer, htmlSoup)

    filePictureLinksReplace(path, fileName, urlSiteAAspirer, htmlSoup)
