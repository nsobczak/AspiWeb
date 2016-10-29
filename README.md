# Aspirateur
Python course - TP02

## SuperAspirateur ?
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
    fonction qui ecrit une chaine de caracteres dans un fichier

- fileReplace(fileName):
    Fonction qui remplace les noms de domaines externes d'un fichier html par un un nom de domaine interne
    
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
