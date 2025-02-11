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
    liste_spe = [0,1,2,3,4,5,6,7,8]                     # On considère que la liste des specialité est la meme que dans l'énoncé, de 0 à 8
    dico_pref_etu = []                                  # On creer une liste qui va contenir les preferences de chaque etudiant         
    for i in range(n):                          
        temp = liste_spe[:]                             # on fait une copie de liste_spe, sans changer l'original (d'ou [:])
        random.shuffle(temp)                            # on utilise la commande random.shuffle(), qui donne un ordre aléatoire a une liste (merci sdd)
        temp.append(dico_pref_etu)                      # On ajoute cette liste dans notre liste de preferences
    return dico_pref_etu

def genere_pref_spe(n):
    """
    n correspond à une liste d'etudiant,
    les specialités vont donc choisir
    une preferences sur cette liste 
    """
    liste_spe = [0,1,2,3,4,5,6,7,8]                     # On reconsidere notre liste de spe
    liste_etu = list(range(n+1))                        # On creer une liste d'etudiant allant de 0 a n : [0,1,2...n]
    dico_pref_spe = {}                          
    i = 0                                               # Une liste qui va itérer sur le nombre de spe
    for i in range(len(liste_spe)):             
        temp = liste_etu[:]                             # On copie une liste d'etudiant sans changer l'original
        random.shuffle(temp)                            # On shuffle cette copie
        dico_pref_spe[i] = temp                         # on creer le couple correspondant
    return dico_pref_spe

def genere_capacite(n,nb_spe):
    """
    n correspond au nombre total de place dispo,
    egalement le nombre d'etudiant.
    nb_spe correspond le nombre de specialités
    """                         
    nb_deterministe = n//nb_spe                         # On divise n par nb_spe pour avoir une idée de combien de place va avoir chaque spe
    reste = n%nb_spe                                    # Calcul du reste au cas ou la division n'est pas ronde
    liste_capacite = [nb_deterministe] * nb_spe         # Creation d'une liste contenant nb_spe element, chacun a comme valeur nb_deterministe

    for i in range(reste):                              # Cette boucle sert a attribué aléatoirement à une spécialité une place en plus, vis a vis du reste, au début je voulais faire que ce soit les premieres spé qui aient cette capacité en plus, mais je pense que ca aurait été inéquitable
        liste_capacite[random.randint(0,nb_spe-1)] += 1
    return liste_capacite