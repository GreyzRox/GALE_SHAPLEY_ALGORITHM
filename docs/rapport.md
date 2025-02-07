#### Guillaume DUPART & Yanis TOUTAIN

# Rapport Mini-Projet IA & Jeux


Lorsque nous appliquons l'algorithme "coté étudiants" à l'aide de la fonction [galeshapley_etu](../src/galeshapley.py), nous arrivons a ce résultat : 

{0: 5, 1: 6, 4: 1, 5: 0, 3: 0, 7: 7, 9: 2, 6: 8, 10: 4, 2: 8, 8: 3}


| Proposition        | Décision   | Mariage                                                                                   |
|--------------------|------------|-------------------------------------------------------------------------------------------|
| 0 propose à 5      | 5 accepte  | ((0:5))                                                                                    |
| 1 propose à 6      | 6 accepte  | ((0:5), (1:6))                                                                             |
| 2 propose à 4      | 4 accepte  | ((0:5), (1:6), (2:4))                                                                      |
| 3 propose à 6      | 6 refuse à 3 | ((0:5), (1:6), (2:4))                                                                      |
| 3 propose à 5      | 5 refuse à 3 | ((0:5), (1:6), (2:4))                                                                      |
| 3 propose à 7      | 7 accepte  | ((0:5), (1:6), (2:4), (3:7))                                                               |
| 4 propose à 1      | 1 accepte  | ((0:5), (1:6), (2:4), (3:7), (4:1))                                                        |
| 5 propose à 0      | 0 accepte  | ((0:5), (1:6), (2:4), (3:7), (4:1), (5:0))                                                 |
| 6 propose à 5      | 5 refuse à 6 | ((0:5), (1:6), (2:4), (3:7), (4:1), (5:0))                                                 |
| 6 propose à 7      | 7 accepte  | ((0:5), (1:6), (2:4), (3:7), (4:1), (5:0), (6:7))                                          |
| 3 est enlevé de la spe 7 | - | ((0:5), (1:6), (2:4), (4:1), (5:0), (6:7))                                                 |
| 3 propose à 0      | 0 accepte  | ((0:5), (1:6), (2:4), (4:1), (5:0), (6:7), (3:0))                                          |
| 7 propose à 7      | 7 accepte  | ((0:5), (1:6), (2:4), (4:1), (5:0), (6:7), (3:0), (7:7))                                  |
| 6 est enlevé de la spe 7 | - | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7))                                          |
| 6 propose à 5      | 5 refuse à 6 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7))                                          |
| 6 propose à 7      | 7 refuse à 6 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7))                                          |
| 6 propose à 6      | 6 refuse à 6 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7))                                          |
| 6 propose à 2      | 2 accepte  | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (6:2))                                  |
| 8 propose à 5      | 5 refuse à 8 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (6:2))                                  |
| 8 propose à 7      | 7 refuse à 8 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (6:2))                                  |
| 8 propose à 6      | 6 refuse à 8 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (6:2))                                  |
| 8 propose à 2      | 2 refuse à 8 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (6:2))                                  |
| 8 propose à 8      | 8 accepte  | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (6:2), (8:8))                            |
| 9 propose à 2      | 2 accepte  | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (6:2), (8:8), (9:2))                    |
| 6 est enlevé de la spe 2 | - | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2))                            |
| 6 propose à 5      | 5 refuse à 6 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2))                            |
| 6 propose à 7      | 7 refuse à 6 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2))                            |
| 6 propose à 6      | 6 refuse à 6 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2))                            |
| 6 propose à 2      | 2 refuse à 6 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2))                            |
| 6 propose à 8      | 8 accepte  | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2), (6:8))                    |
| 10 propose à 6     | 6 refuse à 10 | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2), (6:8))                    |
| 10 propose à 4     | 4 accepte  | ((0:5), (1:6), (2:4), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2), (6:8), (10:4))            |
| 2 est enlevé de la spe 4 | - | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2), (6:8), (10:4))                   |
| 2 propose à 4      | 4 refuse à 2 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2), (6:8), (10:4))                   |
| 2 propose à 0      | 0 refuse à 2 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2), (6:8), (10:4))                   |
| 2 propose à 7      | 7 refuse à 2 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2), (6:8), (10:4))                   |
| 2 propose à 2      | 2 refuse à 2 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (8:8), (9:2), (6:8), (10:4))                   |
| 2 propose à 8      | 8 accepte  | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (9:2), (6:8), (10:4), (2:8))                    |
| 8 est enlevé de la spe 8 | - | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (9:2), (6:8), (10:4), (2:8))                    |
| 8 propose à 5      | 5 refuse à 8 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (9:2), (6:8), (10:4), (2:8))                    |
| 8 propose à 7      | 7 refuse à 8 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (9:2), (6:8), (10:4), (2:8))                    |
| 8 propose à 6      | 6 refuse à 8 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (9:2), (6:8), (10:4), (2:8))                    |
| 8 propose à 2      | 2 refuse à 8 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (9:2), (6:8), (10:4), (2:8))                    |
| 8 propose à 8      | 8 refuse à 8 | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (9:2), (6:8), (10:4), (2:8))                    |
| 8 propose à 3      | 3 accepte  | ((0:5), (1:6), (4:1), (5:0), (3:0), (7:7), (9:2), (6:8), (10:4), (2:8), (8:3))             |


Pour le temps d'execution, l'algorithme met 7.152557373046875e-07 secondes à s'executer
soit 0,0007152555737304688 ms

Concernant la complexité :

| Étape                                      | Opération                                                    | Complexité                        |
|--------------------------------------------|--------------------------------------------------------------|-----------------------------------|
| **Initialisation**                         | Créer la liste des étudiants (`etu_libre`)                   | \( O(n) \)                        |
|                                            | Appliquer `heapq.heapify` pour trier la liste des étudiants  | \( O(n) \)                        |
| **Boucle principale**                      | Boucle sur tous les étudiants                                 | \( n \) itérations                |
| **Parcours des spécialités pour chaque étudiant** | Boucle sur les spécialités de chaque étudiant                | \( k \) itérations par étudiant   |
| **Vérification de la capacité d'une spécialité** | Vérification de la capacité de la spécialité                | \( O(1) \)                        |
| **Ajout d'un étudiant dans une spécialité** | `heapq.heappush` pour ajouter un étudiant à une spécialité    | \( O(log k) \)                   |
| **Gestion de l'éviction d'un étudiant**    | `max(files_spe[spe])` pour trouver l'étudiant le moins bien classé | \( O(log k) \)               |
|                                            | `heapq.heappush` pour ajouter un nouvel étudiant dans la spécialité | \( O(log k) \)             |
|                                            | `heapq.heappush` pour réajouter un étudiant libre            | \( O(log n) \)                   |
| **Complexité totale**                      | Itérations sur tous les étudiants et toutes les spécialités | \( O(n * k * log(k)) \)   |
