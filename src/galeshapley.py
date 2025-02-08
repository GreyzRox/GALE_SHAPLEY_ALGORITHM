#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:19:01 2025

@author: 28710554
"""
import PrefEtuSpe
import heapq
import time
import random

def convertisseur_liste_dico(liste):
     return {i: prefs for i, prefs in enumerate(liste)}

def recherche_classement_spe(dico,i,spe):
    if spe not in dico:  # Vérifie que la spécialité existe bien
            return -1  # Un très grand nombre pour éviter les erreurs
        
    for rang, etu in enumerate(dico[spe]):
        if etu == i:
            return rang
    return -1

liste_etu = PrefEtuSpe.PrefEtu("./data/PrefEtu.txt")
dico_etu = convertisseur_liste_dico(liste_etu)

liste_spe = PrefEtuSpe.PrefSpe("./data/PrefSpe.txt")
dico_spe = convertisseur_liste_dico(liste_spe)

capacite = PrefEtuSpe.Capacite_spe("./data/PrefSpe.txt")

# dico_etu ==== {0: [5, 7, 6, 8, 3, 2, 0, 1, 4], 1: [6, 5, 0, 4, 7, 2, 8, 3, 1], 2: [4, 0, 7, 2, 8, 3, 1, 6, 5], 3: [6, 5, 7, 0, 8, 4, 3, 1, 2], 4: [1, 6, 7, 5, 0, 2, 4, 8, 3], 5: [0, 7, 4, 2, 8, 3, 1, 6, 5], 6: [5, 7, 6, 2, 8, 3, 0, 1, 4], 7: [7, 0, 4, 2, 8, 3, 1, 6, 5], 8: [5, 7, 6, 2, 8, 3, 0, 1, 4], 9: [2, 6, 5, 8, 3, 1, 4, 7, 0], 10: [6, 4, 0, 8, 3, 1, 5, 2, 7]}
# dico_spe ==== {0: [7, 9, 5, 4, 3, 1, 0, 10, 6, 8, 2], 1: [7, 5, 9, 4, 3, 1, 0, 10, 8, 6, 2], 2: [3, 9, 5, 4, 7, 6, 1, 0, 10, 8, 2], 3: [7, 9, 5, 4, 3, 1, 0, 6, 10, 8, 2], 4: [10, 3, 0, 4, 5, 6, 7, 8, 9, 1, 2], 5: [1, 0, 3, 4, 5, 6, 7, 2, 9, 10, 8], 6: [0, 1, 3, 4, 5, 6, 7, 2, 8, 10, 9], 7: [7, 6, 9, 5, 4, 3, 1, 0, 10, 8, 2], 8: [1, 0, 3, 4, 5, 6, 7, 2, 9, 10, 8]}
# capacite  ==== [2, 1, 1, 1, 1, 1, 1, 1, 2]                                                                                                                                                                                # C'etait un enfer à coder

#Question 3

def galeshapley_etu(dico_etu,dico_spe,capacite):
    etu_libre = list(dico_etu.keys())                                                                       # liste des etudiants libres
    heapq.heapify(etu_libre)                                                                                # On trie pour avoir le min le plus a gauche
    couple_etu_spe =  {}                                                                                    # dico des couple etudiant-spe
    files_spe = {spe: [] for spe in dico_spe}                                                               # Dictionnaire contenant chaque specialité en clé, et une liste vide pour l'instant

    while etu_libre:
        etu = heapq.heappop(etu_libre)                                                                      # Prend le premiere element de la liste, le stock et le suppr de la liste
        for spe in dico_etu[etu]:                                                                           # pour chaque specialite dans la liste des specialite de etu
            if capacite[spe] > 0:                                                                           # Si la specialite peut accueillir un nouvel etudiant                                                                       
                couple_etu_spe[etu] = spe                                                                   # On met dans le dictionnaire : etudiant,specialite
                heapq.heappush(files_spe[spe], (recherche_classement_spe(dico_spe, etu, spe), etu))         # on renvoie un tuple qui contient le classement de l'etudiant dans la specialite, et l'etudiant en question
                capacite[spe] -= 1                                                                          # On decremente la capacite de la specialite
                break                                                                                       # On change du coup d'etudiant
            else:                                                                                           # Si par contre la capacite est deja a son max, on essaye de voir si on peut pas virer le "moins bon" etudiant selectionné
                pire_etudiant = max(files_spe[spe])                                                         # On définit le pire etudiant comme etant celui
                if recherche_classement_spe(dico_spe,etu,spe) < pire_etudiant[0]:                           # Si le classement de l'etudiant dans la spe est meilleure que celui du pire etudiant selectionné, alors on remplace
                    files_spe[spe].remove(pire_etudiant)                                                    # On enleve le pire etudiant des specialités
                    heapq.heappush(files_spe[spe], (recherche_classement_spe(dico_spe, etu, spe), etu))     # On ajoute le nouvel etudiant dans la file de la specialité
                    couple_etu_spe.pop(pire_etudiant[1])                                                    # On supprime l'ancien couple                       
                    couple_etu_spe[etu] = spe                                                               # On ajoute le nouveau
                    heapq.heappush(etu_libre, pire_etudiant[1])                                             # Le pire etudiant redevient libre (mskn)
                    break
                else :
                    continue
    return couple_etu_spe                                                                                                                                                                                                # A l'aide, j'ai recodé cet algo 30 fois

print("Côté étudiant  :")
debut = time.time()
affectation_etu = galeshapley_etu(dico_etu,dico_spe,capacite)
print(affectation_etu)

fin = time.time()
temps = fin-debut
print("Temps de l'algo côté étu : ",temps," secondes")

#Question 4 :

def galeshapley_spe(dico_etu,dico_spe,capacite):
    spe_libre = list(dico_spe.keys())
    heapq.heapify(spe_libre)
    couple_etu_spe =  {}

    while spe_libre:
        spe = heapq.heappop(spe_libre)
        for etu in dico_spe[spe]:
            if etu not in couple_etu_spe:
                couple_etu_spe[etu]=spe
                capacite[spe] -=1
                if capacite[spe]>0:
                    heapq.heappush(spe_libre, spe) # reste libre si encore de la place
                break
            else:
                spe_actuelle = couple_etu_spe[etu]
                if recherche_classement_spe(dico_etu, spe, etu)<recherche_classement_spe(dico_etu, spe_actuelle, etu):
                    couple_etu_spe[etu] = spe
                    capacite[spe] -=1
                    capacite[spe_actuelle] +=1
                    heapq.heappush(spe_libre,spe_actuelle)
                    break
                else:
                    continue

    return couple_etu_spe

print("Côté parcours :")
debut = time.time()
affectation_spe = galeshapley_spe(dico_etu,dico_spe,capacite)
print(affectation_spe)

fin = time.time()
print("Temps de l'algo côté parcours : ",fin-debut, "secondes")

#Question 5 : voir rapport.md

#Question 6 :

# {7: 7, 5: 0, 3: 8, 9: 2, 10: 4, 1: 5, 0: 6, 4: 1}

def paire_instable(couple_etu_spe,pref_etu,pref_spe):
    p_instable = []
    for etu_courant in couple_etu_spe:
        spe_courante = couple_etu_spe[etu_courant]
        classement=0
        while pref_spe[spe_courante][classement] != etu_courant:
            etu_a_comparer = pref_spe[spe_courante][classement]
            spe_etu_a_comparer = couple_etu_spe[etu_a_comparer]
            if pref_spe[spe_etu_a_comparer].index(etu_courant)<pref_spe[spe_etu_a_comparer].index(etu_a_comparer) and pref_etu[etu_courant].index(spe_etu_a_comparer)<pref_etu[etu_courant].index(spe_courante):
                p_instable.append((etu_courant,spe_etu_a_comparer))
            classement+=1
    
    return p_instable

#print("Paire instable côté étu : ",paire_instable(affectation_etu,liste_etu,liste_spe))
#print("Paire instable côté spé : ",paire_instable(affectation_spe,liste_etu,liste_spe))

