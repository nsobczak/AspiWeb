# Aspirateur
Python course - TP02

## AspiWeb
but = aspirer un site

### parametres

|Paramètre|Type|Variable|
|---|---|---|
|chemin où stocker le site sur notre pc|obligatoire|savePath|
|website à télécharger|obligatoire|url|
|nom de fichier de conf des logger|obligatoire|logConf|
|profondeur maxi de l'arbre à parcourir|optionnel|"-d", "--depth"|
|taille maxi du fichier que l'on peut télécharger|optionnel|"-sf", "--sizeFile"|
|taille maxi que le dossier dans lequel on met le site ne doit pas dépasser|optionnel|"-sd", "--sizeDirectory"|


### imposé

- module logging
- main

### piste

|Librairie|Disponibilité|
|---|---|
|urllib| python 2|
|urllib2| python 2|
|os|python 3|
|argpase|python 3|
|sys|python 3|
|bs4|python 3|


## Architecture

### liste de fonctions

- initVariables()

### module fileManagement

- fileWrite(path, fileName, chaineAEcrire):
    Fonction qui ecrit une chaine de caracteres dans un fichier

- isLinkRelativ(link):
    Fonction qui analyse si un lien est relatif ou pas
    
- getDomain(link):
    Fonction qui recupere le nom de domaine du site a partir de son url
    
- needLinkToBeReplace(stringAAnalyser, urlSiteAAspirer):
    Fonction qui examine un lien et determine s'il doit etre remplace par un lien local ou ignore s'il s'agit d'un lien externe
    
- fileLinksReplace(path, fileName, urlSiteAAspirer, htmlSoup):
    Fonction qui remplace les noms de domaines externes d'un fichier html par un nom de domaine interne
    
- filePictureLinksReplace(path, fileName, urlSiteAAspirer, htmlSoup):
    Fonction qui remplace les liens des images
    
- fileReplace(path, fileName, urlSiteAAspirer):
    Fonction qui remplace les liens
    
### module scrapingWeb

- extractHTML(url):
    Renvoie la liste des liens contenus dans une page html pour une url

- downloadFile(urlFile, fileRegisterPath):
    Renvoie le contenu d'une page html
    
- listOfLinks(soup):
    Renvoie la liste des liens contenus dans une page html pour une url

- listOfPictures(soup):
    Renvoie la liste des images contenues dans une page html pour une url

- downloadAllPictures(soup, destinationPath):
    telecharge toutes les images possibles du code html contenu dans soup


### Main

- initVariables()

- loop()

- main
	initVariables()
	loop()
