#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:12:30 2025

@author: 28710554
"""

def PrefEtu(s):
    monFichier = open(s, "r")
    contenu = monFichier.readlines()
    monFichier.close()
    for i in range(len(contenu)):
        contenu[i]=contenu[i].split()
    res = [[0]*9 for i in range(int(contenu[0][0]))]
    for i in range(int(contenu[0][0])):
        for j in range (9):
            res[i][j] = int(contenu[i+1][j+2])
    return res
   
def PrefSpe(s):
    monFichier = open(s, "r")
    contenu = monFichier.readlines()
    monFichier.close()
    for i in range(len(contenu)):
        contenu[i]=contenu[i].split()
    res = [[0]*int(contenu[0][1]) for i in range(9)]
    for i in range(9):
        for j in range (int(contenu[0][1])):
            res[i][j] = int(contenu[i+2][j+2])
    return res

def Capacite_spe(s):
    monfichier = open(s, "r")
    contenu = monfichier.readlines()
    monfichier.close()

    for ligne in contenu:
        if ligne.startswith("Cap"):  # startswith sert a analyser les lignes qui commence par "..." en tant que condition (c'est Patrick (pratique) merci le chat de m'avoir donné l'idée) 
            capacites = list(map(int, ligne.split()[1:]))  # on split chaque element du 1er au dernier element (en skippant l'element 0), puis on map pour convertir en int, qu'on met dans une liste nommée "capacité"
            return capacites

    return []
    