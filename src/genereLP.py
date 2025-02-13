import galeshapley
import generate

def generate_lp_file(students, specialties, capacities, preferences, k, filename="assignment.lp"):
    """
    Génère un fichier .lp pour résoudre l'affectation des étudiants aux spécialités.

    :param students: Liste des étudiants (ex: [0, 1, 2, ...])
    :param specialties: Liste des spécialités (ex: [0, 1, 2, ...])
    :param capacities: Liste des capacités des spécialités, où l'index représente la spécialité
    :param preferences: Liste des préférences des étudiants (index = étudiant, valeur = liste des préférences de spécialités)
    :param k: Nombre maximum de choix pris en compte par étudiant
    :param filename: Nom du fichier de sortie
    """
    with open(filename, "w") as f:
        # Fonction objectif (on maximise une constante pour vérifier la faisabilité)
        f.write("Maximize\nobj: maximiser le nombre total de 'choix préférés' pour tous les étudiants, où un 'choix préféré' est défini comme un étudiant affecté à une spécialité parmi ses kk premiers choix\n")

        # Contraintes
        f.write("Subject To\n")

        # Contrainte 1 : Chaque étudiant est affecté à exactement une spécialité parmi ses k premières préférences
        for i in students:
            top_k_choices = preferences[i][:k]  # On garde seulement les k premiers choix
            f.write(f"c_etudiant_{i}: " + " + ".join(f"x{i}_{j}" for j in top_k_choices) + " = 1\n")

        # Contrainte 2 : Respect des capacités des spécialités
        for j in specialties:
            students_who_can_choose_j = [i for i in students if j in preferences[i][:k]]
            if students_who_can_choose_j:  # On évite les contraintes vides
                f.write(f"c_capacite_{j}: " + " + ".join(f"x{i}_{j}" for i in students_who_can_choose_j) + f" <= {capacities[j]}\n")

        # Définition des variables binaires
        f.write("Binary\n")
        for i in students:
            for j in preferences[i][:k]:  # Seulement pour les choix possibles
                f.write(f"x{i}_{j} ")

        # Fin du fichier
        f.write("\nEnd\n")

    print(f"Fichier {filename} généré avec succès.")


# Exemple d'utilisation :
students = [i for i in range(11)]  # 11 étudiants
specialties = [i for i in range(9)]  # 9 spécialités
capacities = [2, 1, 1, 1, 1, 1, 1, 1, 2]  # Capacité de chaque spécialité
preferences = generate.genere_pref_etu(11)
print(preferences)

k = 3  # On limite aux 3 premières préférences

generate_lp_file(students, specialties, capacities, preferences, k)