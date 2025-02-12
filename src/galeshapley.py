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
import random

liste_etu = PrefEtuSpe.PrefEtu("../data/PrefEtu.txt")
liste_spe = PrefEtuSpe.PrefSpe("../data/PrefSpe.txt")
capacite = PrefEtuSpe.Capacite_spe("../data/PrefSpe.txt")                                                                                                                                                                              # C'etait un enfer à coder

#Question 3

def galeshapley_etu(liste_etu, liste_spe, capacite):
    Petu = liste_etu.copy()                                                                                 # On copie la liste des étudiants
    Pspe = liste_spe.copy()                                                                                 # On copie la liste des spécialités
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
                heapq.heappush(spe_tas[spe_pref], (-prefSpeIndices[spe_pref][etu_act], etu_act))            # On ajoute l'étudiant actuel au tas de la spécialité préférée
            else: # Sinon
                if -prefSpeIndices[spe_pref][etu_act] < spe_tas[spe_pref][0][0]:                            # Si l'étudiant actuel est préféré à l'étudiant le moins bien classé de la spécialité préférée
                    etu_libre.append(spe_tas[spe_pref][0][1])                                               # On ajoute l'étudiant le moins bien classé de la spécialité préférée à la liste des étudiants libres
                    heapq.heappop(spe_tas[spe_pref])                                                        # On retire l'étudiant le moins bien classé de la spécialité préférée du tas
                    couple_etu_spe[etu_act] = spe_pref                                                      # On ajoute le couple étudiant-spécialité à la liste des couples
                    heapq.heappush(spe_tas[spe_pref], (-prefSpeIndices[spe_pref][etu_act], etu_act))        # On ajoute l'étudiant actuel au tas de la spécialité préférée
                else:
                    etu_libre.append(etu_act)                                                               # On ajoute l'étudiant actuel à la liste des étudiants libres
    return couple_etu_spe

#Question 4 :

liste_etu = PrefEtuSpe.PrefEtu("../data/PrefEtu.txt")
liste_spe = PrefEtuSpe.PrefSpe("../data/PrefSpe.txt")
capacite = PrefEtuSpe.Capacite_spe("../data/PrefSpe.txt")
 
def galeshapley_spe(liste_etu,liste_spe,capacite):
    
    # Utilisation de deque pour les spécialités libres
    spe_libre = deque(range(len(liste_spe)))
    
   # Création de la liste des préférences des spécialités pour chaque étudiant
    spe_preferences = [deque(liste_spe[spe]) for spe in range(len(liste_spe))]
    couple_etu_spe =  [None] * (len(liste_etu))

    while spe_libre:
        spe = spe_libre.popleft()
        
        if capacite[spe] == 0:
            continue
        
        # Extraire l'étudiant préféré (le premier de la liste de préférences de la spécialité)
        etu = spe_preferences[spe].popleft()
        if couple_etu_spe[etu] is None:
            couple_etu_spe[etu]=spe
            capacite[spe] -=1
            if capacite[spe]>0:
               spe_libre.append(spe)
        else:
            spe_actuelle = couple_etu_spe[etu]
            classement_spe = liste_etu[etu].index(spe)
            classement_spe_actuelle = liste_etu[etu].index(spe_actuelle)            
            if classement_spe < classement_spe_actuelle:
                couple_etu_spe[etu] = spe
                capacite[spe] -=1
                capacite[spe_actuelle] +=1
                
                if capacite[spe_actuelle] > 0:
                    spe_libre.append(spe_actuelle)  # On remet l'ancienne spécialité dans la deque si elle a encore de la place
                if capacite[spe] > 0:
                    spe_libre.append(spe)
            else:
                spe_libre.append(spe)

    return couple_etu_spe

#Question 6 :

def paire_instable(couple_etu_spe,pref_etu,pref_spe):
    """ 
    Le but de cet algo est de vérifier qu'il N'Y A PAS de paires instables
    Logiquement, Cet algo renvoie une liste vide.
    """
    p_instable = []                                                                                                     # Création de la liste des paires potentiellement instable
    for etu_courant in couple_etu_spe:                                                                                  # On parcourt chaque couple
        spe_courante = couple_etu_spe[etu_courant]                                                                      # On isole la specialité lié au couple
        classement=0                                                                                                    # On créer un classement, ce qui va nous permettre de comparer
        while pref_spe[spe_courante][classement] != etu_courant:                                                        # Tant que notre etudiant est different de celui de l'iteration
            etu_a_comparer = pref_spe[spe_courante][classement]                                                         # On extrait l'etudiant qui est a la position classement de la spe_courante
            spe_etu_a_comparer = couple_etu_spe[etu_a_comparer]                                                         # On Regarde la specialite de l'etu a comparer dans la liste de couple
            if (pref_spe[spe_etu_a_comparer].index(etu_courant)<pref_spe[spe_etu_a_comparer].index(etu_a_comparer)      # Si l'étudiant etu_courant préfère la spécialité de l'étudiant etu_a_comparer
                    and pref_etu[etu_courant].index(spe_etu_a_comparer)<pref_etu[etu_courant].index(spe_courante)):         # à la sienne et si la spécialité de etu_a_comparer préfère etu_courant à l'étudiant qu'elle lui a actuellement attribué, ce qui créerait une paire instable.
                    
                p_instable.append((etu_courant,spe_etu_a_comparer))                                                     # On ajoute la paire instable
            classement+=1
    
    return p_instable
