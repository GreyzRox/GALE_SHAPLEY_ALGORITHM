Maximize
obj: maximiser le nombre total de 'choix préférés' pour tous les étudiants, où un 'choix préféré' est défini comme un étudiant affecté à une spécialité parmi ses kk premiers choix
Subject To
c_etudiant_0: x0_8 + x0_0 + x0_1 = 1
c_etudiant_1: x1_6 + x1_5 + x1_1 = 1
c_etudiant_2: x2_8 + x2_1 + x2_4 = 1
c_etudiant_3: x3_1 + x3_3 + x3_8 = 1
c_etudiant_4: x4_5 + x4_8 + x4_7 = 1
c_etudiant_5: x5_2 + x5_4 + x5_1 = 1
c_etudiant_6: x6_5 + x6_1 + x6_7 = 1
c_etudiant_7: x7_0 + x7_4 + x7_8 = 1
c_etudiant_8: x8_2 + x8_7 + x8_3 = 1
c_etudiant_9: x9_4 + x9_1 + x9_2 = 1
c_etudiant_10: x10_6 + x10_7 + x10_5 = 1
c_capacite_0: x0_0 + x7_0 <= 2
c_capacite_1: x0_1 + x1_1 + x2_1 + x3_1 + x5_1 + x6_1 + x9_1 <= 1
c_capacite_2: x5_2 + x8_2 + x9_2 <= 1
c_capacite_3: x3_3 + x8_3 <= 1
c_capacite_4: x2_4 + x5_4 + x7_4 + x9_4 <= 1
c_capacite_5: x1_5 + x4_5 + x6_5 + x10_5 <= 1
c_capacite_6: x1_6 + x10_6 <= 1
c_capacite_7: x4_7 + x6_7 + x8_7 + x10_7 <= 1
c_capacite_8: x0_8 + x2_8 + x3_8 + x4_8 + x7_8 <= 2
Binary
x0_8 x0_0 x0_1 x1_6 x1_5 x1_1 x2_8 x2_1 x2_4 x3_1 x3_3 x3_8 x4_5 x4_8 x4_7 x5_2 x5_4 x5_1 x6_5 x6_1 x6_7 x7_0 x7_4 x7_8 x8_2 x8_7 x8_3 x9_4 x9_1 x9_2 x10_6 x10_7 x10_5 
End
