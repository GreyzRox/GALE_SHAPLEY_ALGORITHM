import gurobipy as gp
import PrefEtuSpe
import galeshapley

def borda_scores_dico(preferences, m):  
    """
    Calcule les scores de Borda pour chaque étudiant et spécialité.
    :param preferences: Liste de listes, où chaque liste correspond aux préférences d'un étudiant,
                        avec la spécialité à la position i représentant le ième choix.
    :param m: Nombre total de spécialités
    :return: Liste
    """
    n = len(preferences)  # Nombre d'étudiants
    borda_scores = {}
    for i, prefs in enumerate(preferences):
        borda_scores[i] = {}  # Créer un dictionnaire pour chaque étudiant
        for rank, j in enumerate(prefs):  # Rank = position dans la liste (0 = meilleur choix)
            borda_scores[i][j] = m - rank  # Score de Borda
    return borda_scores

def utilite_moyenne(arrangement,pref_etu,m):
    u_totale = 0
    for etu,spe in arrangement.items():
        score = m - pref_etu[etu].index(spe)
        u_totale+=score
    return u_totale/len(arrangement)

def utilite_min(arrangement,pref_etu,m):
    u_min = float('inf')
    for etu,spe in arrangement.items():
        score = m - pref_etu[etu].index(spe)
        if(score<u_min):
            u_min=score
    return u_min

def k_premiers_choix(students, specialties, capacities, preferences, k):
    model = gp.Model("KPremiersChoix")
    
    x = {}
    
    for i in students:
        x[i]={}
        for j in specialties:
            vname=f"x_{i}_{j}"
            x[i][j] = model.addVar(vtype=gp.GRB.BINARY, name=vname)
    
    model.setObjective(gp.quicksum(x[i][j] for i in students for j in specialties), gp.GRB.MAXIMIZE)
    
    # Contrainte 1 : Chaque étudiant est affecté à exactement une spécialité parmi ses k premières préférences
    for i in students:
        top_k_choices = preferences[i][:k]  # On garde seulement les k premiers choix
        model.addConstr(sum(x[i][j] for j in top_k_choices) == 1)
    
    # Contrainte 2 : Respect des capacités des spécialités
    for j in specialties:
        model.addConstr(sum(x[i][j] for i in students) <= capacities[j])
    
    model.optimize()
    
    res_k_premiers_choix = {}    
    
    if model.status == gp.GRB.OPTIMAL:
        print("Solution optimale trouvée :")
        for v in model.getVars():
            print(f"{v.varName} = {v.x}")
            # Extraire les résultats pour les variables x[i][j]
            if v.varName.startswith("x_"):  # Vérifier si la variable est une variable de décision
                i, j = map(int, v.varName[2:].split("_"))  # Extraire i et j de varName
                if v.x == 1:  # Si la variable est égale à 1 dans la solution
                    res_k_premiers_choix[i] = j  # Enregistrer l'affectation dans le dictionnaire
        print(f"Valeur de l'objectif = {model.objVal}")
    elif model.status == gp.GRB.INFEASIBLE:
        print("Le modèle est infaisable.")
    elif model.status == gp.GRB.UNBOUNDED:
        print("Le modèle est non borné.")
    else:
        print(f"Statut de la solution : {model.status}")
        
    return res_k_premiers_choix
        
def k_premiers_choix_max_u_min(students, specialties, capacities, preferences,utilities, k):
    model = gp.Model("Maximiser l'utilité minimale")
    
    x = {}
    
    for i in students:
        x[i]={}
        for j in specialties:
            vname=f"x_{i}_{j}"
            x[i][j] = model.addVar(vtype=gp.GRB.BINARY, name=vname)
    
    u_min = model.addVar(lb=0, ub=gp.GRB.INFINITY, name="u_min")
    
    model.setObjective(u_min, gp.GRB.MAXIMIZE)
    
    # Contrainte 1 : Chaque étudiant est affecté à exactement une spécialité parmi ses k premières préférences
    for i in students:
        top_k_choices = preferences[i][:k]  # On garde seulement les k premiers choix
        model.addConstr(sum(x[i][j] for j in top_k_choices) == 1)
    
    # Contrainte 2 : Respect des capacités des spécialités
    for j in specialties:
        model.addConstr(sum(x[i][j] for i in students) <= capacities[j])
    
    # Contrainte 3 : L'utilité de chaque étudiant doit être supérieure ou égale à u_min
    for i in students:
        for j in specialties:
            model.addConstr(utilities[i][j] * x[i][j] >= u_min)
    
    model.optimize()
    
    if model.status == gp.GRB.OPTIMAL:
        print("Solution optimale trouvée :")
        for v in model.getVars():
            print(f"{v.varName} = {v.x}")
        print(f"Valeur de l'objectif = {model.objVal}")
    elif model.status == gp.GRB.INFEASIBLE:
        print("Le modèle est infaisable.")
    elif model.status == gp.GRB.UNBOUNDED:
        print("Le modèle est non borné.")
    else:
        print(f"Statut de la solution : {model.status}")

def max_somme_u(students, specialties, capacities, utilites_etudiants,utilites_parcours):
    model = gp.Model("Maximiser la somme des utilités")

    # Variables de décision
    x = {}
    
    for i in students:
        x[i]={}
        for j in specialties:
            vname=f"x_{i}_{j}"
            x[i][j] = model.addVar(vtype=gp.GRB.BINARY, name=vname)

    # Fonction objectif (somme des utilités étudiants + utilités parcours)
    model.setObjective(
        gp.quicksum(utilites_etudiants[i][j] * x[i][j] for i in students for j in specialties) +
        gp.quicksum(utilites_parcours[j][i] * x[i][j] for i in students for j in specialties),
        gp.GRB.MAXIMIZE
    )

    # Contrainte 1 : Chaque étudiant est affecté à exactement une spécialité parmi ses k premières préférences
    for i in students:
        model.addConstr(sum(x[i][j] for j in specialties) == 1)
    
    # Contrainte 2 : Respect des capacités des spécialités
    for j in specialties:
        model.addConstr(sum(x[i][j] for i in students) <= capacities[j])

    model.optimize()
    
    res_max_somme_u = {}    
    
    if model.status == gp.GRB.OPTIMAL:
        print("Solution optimale trouvée :")
        for v in model.getVars():
            print(f"{v.varName} = {v.x}")
            # Extraire les résultats pour les variables x[i][j]
            if v.varName.startswith("x_"):  # Vérifier si la variable est une variable de décision
                i, j = map(int, v.varName[2:].split("_"))  # Extraire i et j de varName
                if v.x == 1:  # Si la variable est égale à 1 dans la solution
                    res_max_somme_u[i] = j  # Enregistrer l'affectation dans le dictionnaire
        print(f"Valeur de l'objectif = {model.objVal}")
    elif model.status == gp.GRB.INFEASIBLE:
        print("Le modèle est infaisable.")
    elif model.status == gp.GRB.UNBOUNDED:
        print("Le modèle est non borné.")
    else:
        print(f"Statut de la solution : {model.status}")
    
    return res_max_somme_u

def max_somme_u_5_premiers_choix(students, specialties, capacities, utilites_etudiants,utilites_parcours,preferences):
    model = gp.Model("Maximiser la somme des utilités")

    # Variables de décision
    x = {}
    
    for i in students:
        x[i]={}
        for j in specialties:
            vname=f"x_{i}_{j}"
            x[i][j] = model.addVar(vtype=gp.GRB.BINARY, name=vname)

    # Fonction objectif (somme des utilités étudiants + utilités parcours)
    model.setObjective(
        gp.quicksum(utilites_etudiants[i][j] * x[i][j] for i in students for j in specialties) +
        gp.quicksum(utilites_parcours[j][i] * x[i][j] for i in students for j in specialties),
        gp.GRB.MAXIMIZE
    )

    for i in students:
        top_k_choices = preferences[i][:5]  # On garde seulement les 5 premiers choix
        model.addConstr(sum(x[i][j] for j in top_k_choices) == 1)
    
    # Contrainte 2 : Respect des capacités des spécialités
    for j in specialties:
        model.addConstr(sum(x[i][j] for i in students) <= capacities[j])

    model.optimize()
    
    res_max_somme_u_5_premiers_choix = {}    
    
    if model.status == gp.GRB.OPTIMAL:
        print("Solution optimale trouvée :")
        for v in model.getVars():
            print(f"{v.varName} = {v.x}")
            # Extraire les résultats pour les variables x[i][j]
            if v.varName.startswith("x_"):  # Vérifier si la variable est une variable de décision
                i, j = map(int, v.varName[2:].split("_"))  # Extraire i et j de varName
                if v.x == 1:  # Si la variable est égale à 1 dans la solution
                    res_max_somme_u_5_premiers_choix[i] = j  # Enregistrer l'affectation dans le dictionnaire
        print(f"Valeur de l'objectif = {model.objVal}")
    elif model.status == gp.GRB.INFEASIBLE:
        print("Le modèle est infaisable.")
    elif model.status == gp.GRB.UNBOUNDED:
        print("Le modèle est non borné.")
    else:
        print(f"Statut de la solution : {model.status}")
    
    return res_max_somme_u_5_premiers_choix 

liste_etu = PrefEtuSpe.PrefEtu("../data/PrefEtu.txt")
liste_spe = PrefEtuSpe.PrefSpe("../data/PrefSpe.txt")
capacities = PrefEtuSpe.Capacite_spe("../data/PrefSpe.txt")

students = [i for i in range(len(liste_etu))]
specialties = [i for i in range(len(liste_spe))]
scores_etu = borda_scores_dico(liste_etu,len(specialties))
scores_spe = borda_scores_dico(liste_spe,len(students))

#GS Etu
gs_etu = galeshapley.galeshapley_etu(liste_etu,liste_spe,capacities)
res_etu = {}
for i in range(len(gs_etu)):
    res_etu[i]=gs_etu[i]

print("\n")
print("Résultat GS Etu : ",res_etu)
print("Paire instable GS Etu : ",galeshapley.paire_instable(gs_etu,liste_etu,liste_spe))
print("Utilité moyenne GS Etu : ",utilite_moyenne(res_etu,liste_etu,len(liste_spe)))
print("Utilité minimale GS Etu : ",utilite_min(res_etu,liste_etu,len(liste_spe)))
print("\n")

#GS Spe
gs_spe = galeshapley.galeshapley_spe(liste_etu,liste_spe,capacities)
res_spe = {}
for i in range(len(gs_spe)):
    res_spe[i]=gs_spe[i]

print("\n")
print("Résultat GS Spé : ",res_spe)
print("Paire instable GS Spé : ",galeshapley.paire_instable(gs_spe,liste_etu,liste_spe))
print("Utilité moyenne GS Spé : ",utilite_moyenne(res_spe,liste_etu,len(liste_spe)))
print("Utilité minimale GS Spé : ",utilite_min(res_spe,liste_etu,len(liste_spe)))
print("\n")

#Q13
res_k_premiers_choix = k_premiers_choix(students,specialties,capacities,liste_etu,5)
print("\n")
print("Résultat Q13 : ",res_k_premiers_choix)
print("Paire instable Q13 : ",galeshapley.paire_instable(res_k_premiers_choix,liste_etu,liste_spe))
print("Utilité moyenne Q13 : ",utilite_moyenne(res_k_premiers_choix,liste_etu,len(specialties)))
print("Utilité minimale Q13 : ",utilite_min(res_k_premiers_choix,liste_etu,len(liste_spe)))
print("\n")

#Q14
res_max_somme_u = max_somme_u(students,specialties,capacities,scores_etu,scores_spe)
print("\n")
print("Résultat Q14 : ",res_max_somme_u)
print("Paire instable Q14 : ",galeshapley.paire_instable(res_max_somme_u,liste_etu,liste_spe))
print("Utilité moyenne Q14 : ",utilite_moyenne(res_max_somme_u,liste_etu,len(specialties)))
print("Utilité minimale Q14 : ",utilite_min(res_max_somme_u,liste_etu,len(liste_spe)))
print("\n")

#Q15
res_max_somme_u_5_premiers_choix = max_somme_u_5_premiers_choix(students,specialties,capacities,scores_etu,scores_spe,liste_etu)
print("\n")
print("Résultat Q15 : ",res_max_somme_u_5_premiers_choix)
print("Paire instable Q15 : ",galeshapley.paire_instable(res_max_somme_u_5_premiers_choix,liste_etu,liste_spe))
print("Utilité moyenne Q15 : ",utilite_moyenne(res_max_somme_u_5_premiers_choix,liste_etu,len(specialties)))
print("Utilité minimale Q15 : ",utilite_min(res_max_somme_u_5_premiers_choix,liste_etu,len(liste_spe)))
print("\n")