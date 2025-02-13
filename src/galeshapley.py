#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:19:01 2025

@author: 28710554
"""
import PrefEtuSpe
import heapq
from collections import deque
import time
import copy
from copy import deepcopy
import random

liste_etu = PrefEtuSpe.PrefEtu("../data/PrefEtu.txt")
liste_spe = PrefEtuSpe.PrefSpe("../data/PrefSpe.txt")
capacite = PrefEtuSpe.Capacite_spe("../data/PrefSpe.txt")                                                                                                                                                                              # C'etait un enfer à coder

#Question 3

def galeshapley_etu(liste_etu, liste_spe, capacite):
    Petu = deepcopy(liste_etu)                                                                              # On copie la liste des étudiants        
    Pspe = deepcopy(liste_spe)                                                                              # On copie la liste des spécialités
    cap = capacite.copy()                                                                                   # On copie la liste des capacités
    couple_etu_spe = [None] * len(Petu)                                                                     # On crée une liste vide pour les couples étudiants-spécialités
    prefSpeIndices = [{etu: idx for idx, etu in enumerate(prefs)} for prefs in Pspe]                        # On crée une liste de dictionnaires pour les indices des préférences des spécialités
    spe_tas = [[] for _ in range(len(Pspe))]                                                                # On crée une liste de tas pour les spécialités
    etu_libre = list(range(len(Petu)))                                                                      # On crée une liste des étudiants libres (de 0 à n-1)
    while etu_libre:                                                                                        # Tant qu'il reste des étudiants libres
        etu_act = etu_libre.pop(0)                                                                          # On prend le premier étudiant de la liste des étudiants libres
        liste_spe_act = Petu[etu_act]                                                                       # On prend la liste des spécialités préférées de l'étudiant actuel
        if liste_spe_act != []:                                                                             # Si la liste des spécialités préférées n'est pas vide
            spe_pref = liste_spe_act.pop(0)                                                                 # On prend la première spécialité de la liste des spécialités préférées
            if cap[spe_pref] > 0:                                                                           # Si la capacité de la spécialité préférée est supérieure à 0
                couple_etu_spe[etu_act] = spe_pref                                                          # On ajoute le couple étudiant-spécialité à la liste des couples
                cap[spe_pref] -= 1                                                                          # On décrémente la capacité de la spécialité préférée
                heapq.heappush(spe_tas[spe_pref], (prefSpeIndices[spe_pref][etu_act], etu_act))            # On ajoute l'étudiant actuel au tas de la spécialité préférée
            else: 
                if prefSpeIndices[spe_pref][etu_act] < spe_tas[spe_pref][0][0]:                            # Si l'étudiant actuel est préféré à l'étudiant le moins bien classé de la spécialité préférée
                    etu_libre.append(spe_tas[spe_pref][0][1])                                               # On ajoute l'étudiant le moins bien classé de la spécialité préférée à la liste des étudiants libres
                    heapq.heappop(spe_tas[spe_pref])                                                        # On retire l'étudiant le moins bien classé de la spécialité préférée du tas
                    couple_etu_spe[etu_act] = spe_pref                                                      # On ajoute le couple étudiant-spécialité à la liste des couples
                    heapq.heappush(spe_tas[spe_pref], (prefSpeIndices[spe_pref][etu_act], etu_act))        # On ajoute l'étudiant actuel au tas de la spécialité préférée
                else:
                    etu_libre.append(etu_act)                                                               # On ajoute l'étudiant actuel à la liste des étudiants libres
    return couple_etu_spe

#Question 4 :

liste_etu = PrefEtuSpe.PrefEtu("../data/PrefEtu.txt")
liste_spe = PrefEtuSpe.PrefSpe("../data/PrefSpe.txt")
capacite = PrefEtuSpe.Capacite_spe("../data/PrefSpe.txt")
 
def galeshapley_spe(liste_etu,liste_spe,capacite):                                                          # On reprend les listes de préférences des étudiants et des spécialités, et la capacité des spécialités 
    
    spe_libre = deque(range(len(liste_spe)))                                                                # On crée une deque pour les spécialités libres 
    
    spe_preferences = [deque(liste_spe[spe]) for spe in range(len(liste_spe))]                              # On crée une deque pour les préférences des spécialités    
    couple_etu_spe =  [None] * (len(liste_etu))                                                             # On crée une liste vide pour les couples étudiants-spécialités 

    while spe_libre:                                                                                        # Tant qu'il reste des spécialités libres                                   
        spe = spe_libre.popleft()                                                                           # On prend la première spécialité de la deque des spécialités libres    
        
        if capacite[spe] == 0:                                                                              # Si la capacité de la spécialité est égale à 0                                       
            continue
        
        etu = spe_preferences[spe].popleft()                                                                # On prend le premier étudiant de la deque des préférences de la spécialité 
        if couple_etu_spe[etu] is None:                                                                     # Si l'étudiant n'a pas de spécialité attribuée
            couple_etu_spe[etu]=spe                                                                         # On attribue la spécialité à l'étudiant
            capacite[spe] -=1                                                                               # On décrémente la capacité de la spécialité    
            if capacite[spe]>0:                                                                             # Si la capacité de la spécialité est supérieure à 0    
               spe_libre.append(spe)                                                                        # On remet la spécialité dans la deque des spécialités libres                                               
        else:
            spe_actuelle = couple_etu_spe[etu]                                                              # On prend la spécialité actuelle de l'étudiant                                                   
            classement_spe = liste_etu[etu].index(spe)                                                      # On prend le classement de la spécialité dans la liste des préférences de l'étudiant   
            classement_spe_actuelle = liste_etu[etu].index(spe_actuelle)                                    # On prend le classement de la spécialité actuelle dans la liste des préférences de l'étudiant
            if classement_spe < classement_spe_actuelle:                                                    # Si la spécialité est mieux classée que la spécialité actuelle 
                couple_etu_spe[etu] = spe                                                                   # On attribue la spécialité à l'étudiant                                               
                capacite[spe] -=1                                                                           # On décrémente la capacité de la spécialité
                capacite[spe_actuelle] +=1                                                                  # On incrémente la capacité de la spécialité actuelle
                
                if capacite[spe_actuelle] > 0:                                                              # Si la capacité de la spécialité actuelle est supérieure à 0
                    spe_libre.append(spe_actuelle)                                                          # On remet l'ancienne spécialité dans la deque si elle a encore de la place
                if capacite[spe] > 0:                                                                       # Si la capacité de la nouvelle spécialité est supérieure à 0
                    spe_libre.append(spe)                                                                   # On remet la nouvelle spécialité dans la deque si elle a encore de la place
            else:
                spe_libre.append(spe)                                                                       # On remet la spécialité dans la deque des spécialités libres
    return couple_etu_spe                                                                                   # On retourne la liste des couples étudiants-spécialités

#Question 6 :

def paire_instable(couple_etu_spe,liste_etu,liste_spe):
    """ 
    Le but de cet algo est de vérifier qu'il N'Y A PAS de paires instables
    Logiquement, Cet algo renvoie une liste vide.
    """
    p_instable = []                                                                                                     # Création de la liste des paires potentiellement instable
    for etu_courant in range(len(couple_etu_spe)):                                                                                  # On parcourt chaque couple
        spe_courante = couple_etu_spe[etu_courant]                                                                      # On isole la specialité lié au couple
        
        classement=0                                                                                                    # On créer un classement, ce qui va nous permettre de comparer
        while liste_spe[spe_courante][classement] != etu_courant:                                                       # Tant que notre etudiant est different de celui de l'iteration
            etu_a_comparer = liste_spe[spe_courante][classement]                                                         # On extrait l'etudiant qui est a la position classement de la spe_courante
            
            if etu_a_comparer < len(couple_etu_spe):  # Vérifie que l'étudiant a bien une spécialité attribuée
                spe_etu_a_comparer = couple_etu_spe[etu_a_comparer]  

                # Vérification de la paire instable :
                if (liste_spe[spe_etu_a_comparer].index(etu_courant)<liste_spe[spe_etu_a_comparer].index(etu_a_comparer) and liste_etu[etu_courant].index(spe_etu_a_comparer)<liste_etu[etu_courant].index(spe_courante)):   
                    p_instable.append((etu_courant, spe_etu_a_comparer))  

            classement += 1
    
    return p_instable