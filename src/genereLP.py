import galeshapley
import generate

def compute_borda_scores(preferences, m):
    """
    Calcule les scores de Borda pour chaque étudiant et spécialité.
    :param preferences: Liste de listes, où chaque liste correspond aux préférences d'un étudiant,
                        avec la spécialité à la position i représentant le ième choix.
    :param m: Nombre total de spécialités
    :return: Liste
    """
    n = len(preferences)  # Nombre d'étudiants
    borda_scores = [[0] * m for _ in range(n)]
    for i, prefs in enumerate(preferences):
        for rank, j in enumerate(prefs):  # Rank = position dans la liste (0 = meilleur choix)
            borda_scores[i][j] = m - rank  # Score de Borda
    return borda_scores

def generate_lp_file_k_premiers(students, specialties, capacities, preferences, k, filename="assignment.lp"):
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
        f.write("Maximize\nobj: ")
        f.write(" + ".join(f"x{i}_{j}" for i in students for j in specialties))
        f.write("\n")

        # Contraintes
        f.write("Subject To\n")

        # Contrainte 1 : Chaque étudiant est affecté à exactement une spécialité parmi ses k premières préférences
        for i in students:
            top_k_choices = preferences[i][:k]  # On garde seulement les k premiers choix
            f.write(f"c_etudiant_{i}: " + " + ".join(f"x{i}_{j}" for j in top_k_choices) + " = 1\n")

        # Contrainte 2 : Respect des capacités des spécialités
        for j in specialties:
            if students:
                f.write(f"c_capacite_{j}: " + " + ".join(f"x{i}_{j}" for i in students) + f" <= {capacities[j]}\n")

        # Définition des variables binaires
        f.write("Binary\n")
        for i in students:
            for j in specialties:  # Seulement pour les choix possibles
                f.write(f"x{i}_{j} ")

        # Fin du fichier
        f.write("\nEnd\n")

    print(f"Fichier {filename} généré avec succès.")

def generate_lp_file_max_u_min(students, specialties, capacities,scores, filename="assignment_max_u_min.lp"):
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
        f.write("Maximize\nobj: u\n")

        # Contraintes
        f.write("Subject To\n")

        # Contrainte 1 : Chaque étudiant est affecté à exactement une spécialité
        for i in students:
            f.write(f"c_etudiant_{i}: " + " + ".join(f"x{i}_{j}" for j in specialties) + " = 1\n")

        # Contrainte 2 : Respect des capacités des spécialités
        for j in specialties:
            if students:
                f.write(f"c_capacite_{j}: " + " + ".join(f"x{i}_{j}" for i in students) + f" <= {capacities[j]}\n")

        # Contrainte 3 : Utilité minimale
        for i in students:
            f.write(f"c_utilite_{i}: " + " + ".join(f"x{i}_{j} * {scores[i][j]}" for j in specialties) + f" >= u\n")
        
        # Définition des variables binaires
        f.write("Binary\n")
        for i in students:
            for j in specialties:  # Seulement pour les choix possibles
                f.write(f"x{i}_{j} ")
            f.write("\n")
        # Fin du fichier
        f.write("\nEnd\n")

    print(f"Fichier {filename} généré avec succès.")
    

def generate_lp_fichier_max_somme_u(students, specialties, capacities, scores, filename="assignment_max_somme_u.lp"):
    """
    Génère un fichier .lp pour le problème d'affectation.

    :param etudiants: Liste des étudiants.
    :param parcours: Liste des parcours.
    :param scores: Liste de listes des scores (utilités), où scores[i][j] est le score de l'étudiant i pour le parcours j.
    :param capacites: Liste des capacités des parcours, où capacites[j] est la capacité du parcours j.
    :param nom_fichier: Nom du fichier .lp à générer.
    """

    with open(filename, "w") as f:
        # Début du fichier .lp
        f.write("Maximize\n")
        f.write("obj: ")

        # Fonction objectif (somme des utilités)
        f.write(" + ".join(f"{scores[i][j]} * x{i}_{j}" for i in students for j in specialties))
        f.write("\n")

        f.write("Subject To\n")

        # Contrainte 1 : Chaque étudiant est affecté à exactement une spécialité
        for i in students:
            f.write(f"c_etudiant_{i}: " + " + ".join(f"x{i}_{j}" for j in specialties) + " = 1\n")

        # Contrainte 2 : Respect des capacités des spécialités
        for j in specialties:
            if students:
                f.write(f"c_capacite_{j}: " + " + ".join(f"x{i}_{j}" for i in students) + f" <= {capacities[j]}\n")


        # Variables binaires
        f.write("Binary\n")
        f.write(" ".join(f"x{i}_{j}" for i in students for j in specialties))
        f.write("\n")

        f.write("End\n")

    print(f"Fichier {filename} généré avec succès.")

def generate_lp_fichier_max_somme_u_k_premiers(students, specialties, capacities, scores, k, filename="assignment_max_somme_u_k_premiers.lp"):
    """
    Génère un fichier .lp pour le problème d'affectation.

    :param etudiants: Liste des étudiants.
    :param parcours: Liste des parcours.
    :param scores: Liste de listes des scores (utilités), où scores[i][j] est le score de l'étudiant i pour le parcours j.
    :param capacites: Liste des capacités des parcours, où capacites[j] est la capacité du parcours j.
    :param nom_fichier: Nom du fichier .lp à générer.
    """

    with open(filename, "w") as f:
        # Début du fichier .lp
        f.write("Maximize\n")
        f.write("obj: ")

        # Fonction objectif (somme des utilités)
        f.write(" + ".join(f"{scores[i][j]} * x{i}_{j}" for i in students for j in specialties))
        f.write("\n")

        f.write("Subject To\n")

        # Contrainte 1 : Chaque étudiant est affecté à exactement une spécialité parmi ses k premières préférences
        for i in students:
            top_k_choices = preferences[i][:k]  # On garde seulement les k premiers choix
            f.write(f"c_etudiant_{i}: " + " + ".join(f"x{i}_{j}" for j in top_k_choices) + " = 1\n")

        # Contrainte 2 : Respect des capacités des spécialités
        for j in specialties:
            if students:
                f.write(f"c_capacite_{j}: " + " + ".join(f"x{i}_{j}" for i in students) + f" <= {capacities[j]}\n")


        # Variables binaires
        f.write("Binary\n")
        f.write(" ".join(f"x{i}_{j}" for i in students for j in specialties))
        f.write("\n")

        f.write("End\n")

    print(f"Fichier {filename} généré avec succès.")


# Exemple d'utilisation :
students = [i for i in range(11)]  # 11 étudiants
specialties = [i for i in range(9)]  # 9 spécialités
capacities = [2, 1, 1, 1, 1, 1, 1, 1, 2]  # Capacité de chaque spécialité
preferences = generate.genere_pref_etu(11)
scores = compute_borda_scores(preferences,len(specialties))

k = 3  # On limite aux 3 premières préférences

generate_lp_file_k_premiers(students, specialties, capacities, preferences, k)
generate_lp_file_max_u_min(students,specialties,capacities,scores)
generate_lp_fichier_max_somme_u(students,specialties,capacities,scores)
generate_lp_fichier_max_somme_u_k_premiers(students,specialties,capacities, scores, 3)