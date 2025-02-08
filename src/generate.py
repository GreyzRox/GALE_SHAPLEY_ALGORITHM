import galeshapley
import PrefEtuSpe
import random

# Question 7

def genere_pref_etu(n):
    """ 
    n correspond au nombre d'etudiant présent,
    qui vont avoir une liste de preferences,
    c'est donc la longueur de notre dico
    """                     
    liste_spe = [0,1,2,3,4,5,6,7,8]             # On considère que la liste des specialité est la meme que dans l'énoncé, de 0 à 8
    dico_pref_etu = {}                          # On creer un dico qui va contenir des couples (etudiant, liste de preferences)         
    i = 0                                       # Une variable qui va iterer sur le nombre d'etudiant
    for i in range(n):                          
        temp = liste_spe[:]                     # on fait une copie de liste_spe, sans changer l'original (d'ou [:])
        random.shuffle(temp)                    # on utilise la commande random.shuffle(), qui donne un ordre aléatoire a une liste (merci sdd)
        dico_pref_etu[i]=temp                   # on associe le couple que l'on stock dans notre dico
    return dico_pref_etu

def genere_pref_spe(n):
    """
    n correspond à une liste d'etudiant,
    les specialités vont donc choisir
    une preferences sur cette liste 
    """
    liste_spe = [0,1,2,3,4,5,6,7,8]             # On reconsidere notre liste de spe
    liste_etu = list(range(n+1))                # On creer une liste d'etudiant allant de 0 a n : [0,1,2...n]
    dico_pref_spe = {}                          
    i = 0                                       # Une liste qui va itérer sur le nombre de spe
    for i in range(len(liste_spe)):             
        temp = liste_etu[:]                     # On copie une liste d'etudiant sans changer l'original
        random.shuffle(temp)                    # On shuffle cette copie
        dico_pref_spe[i] = temp                 # on creer le couple correspondant
    return dico_pref_spe

def genere_capacite(n,nb_spe):
    nb_deterministe = n//nb_spe
    reste = n%nb_spe
    liste_capacite = [nb_deterministe] * nb_spe

    for i in range(reste):
        liste_capacite[random.randint(0,nb_spe)] += 1
    return liste_capacite


print(genere_pref_etu(10))
print("\n")
print(genere_pref_spe(10))
print("\n")
print (genere_capacite(219,9))