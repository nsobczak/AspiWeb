import urllib.request as ur
import os
import webbrowser
import zipfile
from bs4 import BeautifulSoup

def openPage(url):      #Ouvre une page WEB
    webbrowser.open(url)

def downloadFile(url, filename):        #telecharge un fichier WEB
    ur.urlretrieve(url, filename)

def soup(html):         #Lecture HTML avec recuperation des href
    soup = BeautifulSoup(html)
    print(soup)

def read(link):         #Lecture du HTML de la page
    page = ur.urlopen(link)
    strpage = page.read()
    print(strpage)

def monMain():
    lien = 'http://www.d8.tv/d8-series/pid6654-d8-longmire.html'
    link = 'http://python.org'
    url = "http://python.developpez.com/outils/PythonZope/images/cpython.gif"
    filename = "C:/Users/ISEN/Desktop/COURS/M1/Python/archive.gif"
    destinationPath = "C:/Users/ISEN/Desktop/COURS/M1/Python"
    #openPage(url)
    #downloadFile(url, filename)
    html = read(link)
    #soup(html)

if __name__ == "__main__":
    monMain()
