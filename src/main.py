# -*- coding: utf-8 -*-

import galeshapley
import generate
import time
import matplotlib.pyplot as plt

GRAPH = True

def main():                                             
    if GRAPH:                                           # Si l'on veut generer le graph, alors nous devons changer la valeur de la constante GRAPH
        plot_temps(temps_etu(),temps_spe())             # On appelle alors la fonction plot_temps()
    else:
        temps_etu()                                     # Sinon on appelle seulement le temps d'execution pour etu et pour temps
        temps_spe()

def temps_etu():
    n = 200                                                                                                                         # Demarrons a partir de n = 200, ce qui correspond a notre nombre d'etudiant
    liste_moyenne_temps = []                                                                                                        # Nous allons stocké la moyenne des 10 iterations sur n etudiant dans cette liste
    while n <= 2000:                                                                                                                # Tant que n n'aura pas atteint 2000
        liste_temps = []                                                                                                            # Créeons une liste des temps obtenus avec n fixe
        for i in range(10):                                                                                                         # repetons 10 fois l'iteration suivante
            debut = time.time()                                                                                                     # Mesurons le temps
            galeshapley.galeshapley_etu(generate.genere_pref_etu(n),generate.genere_pref_spe(n),generate.genere_capacite(n,9))      # Application de galeshapley_etu avec n etu et 9 spe
            fin = time.time()                                                                                                       # Fin du temps
            temps = fin - debut                                                                                                     # temps obtenus
            liste_temps.append(temps)                                                                                               # Stockage du temps obtenus dans la liste liste_temps
        temps_moyen = sum(liste_temps)/len(liste_temps)                                                                             # Après les 10 ite, calcul de la moyenne
        liste_moyenne_temps.append(temps_moyen)                                                                                     # ajout dans la liste de toutes les moyennes de temps
        n += 200                                                                                                                    # On passe a n suivant
    print (liste_moyenne_temps)                                                                                                     
    return liste_moyenne_temps

def temps_spe():                                                                                                                    # Exactement pareil que en haut
    n = 200
    liste_moyenne_temps = []
    while n <= 2000:
        liste_temps = []
        for i in range(10):
            debut = time.time()
            galeshapley.galeshapley_spe(generate.genere_pref_etu(n),generate.genere_pref_spe(n),generate.genere_capacite(n,9))
            fin = time.time()
            temps = fin - debut
            liste_temps.append(temps)
        temps_moyen = sum(liste_temps)/len(liste_temps)
        liste_moyenne_temps.append(temps_moyen)
        n += 200
    print (liste_moyenne_temps)
    return liste_moyenne_temps

def plot_temps(liste_moyenne_temps_etu, liste_moyenne_temps_spe):
    n_values = [200 * (i + 1) for i in range(len(liste_moyenne_temps_etu))]
    plt.plot(n_values, liste_moyenne_temps_etu, marker='o', linestyle='-', color='b', label='Étudiants')
    plt.plot(n_values, liste_moyenne_temps_spe, marker='x', linestyle='-', colo