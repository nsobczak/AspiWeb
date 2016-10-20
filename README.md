# Aspirateur
Python course - TP02

## SuperAspirateur ?
but = aspirer un site

### parametres

- chemin où stocker le site sur notre pc
- website à télécharger
- nom de fichier de conf des logger
- profondeur maxi de l'arbre à parcourir
- taille maxi du fichier que l'on peut télécharger

- variable qui dit la taille maxi que le dossier dans lequel on met le site ne doit pas dépasser


### imposé

- module logging
- main

### piste
urllib 
urllib2
os
argpase
sys
bs4


## Architecture

### liste de fonctions

- initVariables()

### module fileManagement

- fileWrite(path, fileName, chaineAEcrire):
    fonction qui ecrit une chaine de caracteres dans un fichier

- fileReplace(fileName):
    Fonction qui remplace les noms de domaines externes d'un fichier html par un un nom de domaine interne

### Main

- initVariables()

- loop()

- main
	initVariables()
	loop()
