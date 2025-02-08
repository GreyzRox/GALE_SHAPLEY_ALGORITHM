import galeshapley
import generate
import time
import matplotlib.pyplot as plt

GRAPH = True

def main():
    if GRAPH:
        plot_temps(temps_etu(),temps_spe())
    else:
        temps_etu()
        temps_spe()

def temps_etu():
    n = 200
    liste_moyenne_temps = []
    while n <= 2000:
        liste_temps = []
        for i in range(10):
            debut = time.time()
            galeshapley.galeshapley_etu(generate.genere_pref_etu(n),generate.genere_pref_spe(n),generate.genere_capacite(n,9))
            fin = time.time()
            temps = fin - debut
            liste_temps.append(temps)
        temps_moyen = sum(liste_temps)/len(liste_temps)
        liste_moyenne_temps.append(temps_moyen)
        n += 200
    print (liste_moyenne_temps)
    return liste_moyenne_temps

def temps_spe():
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

import matplotlib.pyplot as plt

def plot_temps(liste_moyenne_temps_etu, liste_moyenne_temps_spe):
    n_values = [200 * (i + 1) for i in range(len(liste_moyenne_temps_etu))]
    plt.plot(n_values, liste_moyenne_temps_etu, marker='o', linestyle='-', color='b', label='Étudiants')
    plt.plot(n_values, liste_moyenne_temps_spe, marker='x', linestyle='-', color='r', label='Spécialités')
    plt.title("Temps moyen d'exécution en fonction de n")  
    plt.xlabel("Nombre d'étudiants (n)")  
    plt.ylabel("Temps moyen (en secondes)")
    plt.legend()
    plt.grid(True)  
    plt.show()




main()