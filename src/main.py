import galeshapley
import PrefEtuSpe
import generate
import time
import random


def main():
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

main()
