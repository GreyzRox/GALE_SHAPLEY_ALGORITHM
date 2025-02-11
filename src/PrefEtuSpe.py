#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:12:30 2025

@author: 28710554
"""
#Question 1

def PrefEtu(s):
    monFichier = open(s, "r")                            # On créer une variable "monFichier" qui sert à ouvrir un fichier "s", et à le passer en mode "lecture" -> "r"
    contenu = monFichier.readlines()                     # La variable "contenu" creer une liste sur chaque ligne de "MonFichier", si le nombre de ligne de "MonFichier" = 5, alors len(contenu) = 5
    monFichier.close()                                   # On oublie pas de refermer le fichier, car on a stocké le contenu dans "contenu"
    for i in range(len(contenu)):                        # On parcourt dans une boucle la longueur de la liste de "contenu"
        contenu[i]=contenu[i].split()                    # Pour chaque element de "contenu", on split() afin de decouper en liste chaque mot de la ligne, le separateur etant " " par défaut
    res = [[0]*9 for i in range(int(contenu[0][0]))]     # On récupere le nombre d'etudiant, et on créer une matrice correspondant a nb_spe*nb_etu
    for i in range(int(contenu[0][0])):                  # On parcourt chaque ligne de contenu
        for j in range (9):                              # chaque colonne de cette ligne
            res[i][j] = int(contenu[i+1][j+2])           # On affecte la valeur associé a notre matrice précédemment créer
    return res                                           # On retourne cette matrice
   
def PrefSpe(s):
    monFichier = open(s, "r")                            # On créer une variable "monFichier" qui sert à ouvrir un fichier "s", et à le passer en mode "lecture" -> "r"
    contenu = monFichier.readlines()                     # La variable "contenu" creer une liste sur chaque ligne de "MonFichier", si le nombre de ligne de "MonFichier" = 5, alors len(contenu) = 5
    monFichier.close()                                   # On oublie pas de refermer le fichier, car on a stocké le contenu dans "contenu"
    for i in range(len(contenu)):                        # On parcourt dans une boucle la longueur de la liste de "contenu"
        contenu[i]=contenu[i].split()                    # Pour chaque element de "contenu", on split() afin de decouper en liste chaque mot de la ligne, le separateur etant " " par défaut
    res = [[0]*int(contenu[0][1]) for i in range(9)]     # On récuperer le nombre d'etudiant, puis créer une matrice de nb_etu*nb_spe
    for i in range(9):                                   # Pour chaque ligne
        for j in range (int(contenu[0][1])):             # Pour chaque colonne
            res[i][j] = int(contenu[i+2][j+2])           # On affecte le contenu de "contenu" a notre matrice résultat, avec un décalage de +2 (a cause du contenu inutile)
    return res                                           # On retourn la matrice resultat

def Capacite_spe(s):                                    
    monfichier = open(s, "r")                            # On créer une variable "monFichier" qui sert à ouvrir un fichier "s", et à le passer en mode "lecture" -> "r"
    contenu = monfichier.readlines()                     # La variable "contenu" creer une liste sur chaque ligne de "MonFichier", si le nombre de ligne de "MonFichier" = 5, alors len(contenu) = 5
    monfichier.close()                                   # On oublie pas de refermer le fichier, car on a stocké le contenu dans "contenu"

    for ligne in contenu:                                # Pour chaque ligne précedemment créer
        if ligne.startswith("Cap"):                      # startswith sert a analyser les lignes qui commence par "..." en tant que condition 
                                                            #(c'est Patrick (pratique) merci le chat de m'avoir donné l'idée) 
            capacites = list(map(int, ligne.split()[1:]))# On split chaque element du 1er au dernier element (en skippant l'element 0), puis on map pour convertir en int, 
                                                            # qu'on met dans une li