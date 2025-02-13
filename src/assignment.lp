Maximize
obj: maximiser le nombre total de 'choix préférés' pour tous les étudiants, où un 'choix préféré' est défini comme un étudiant affecté à une spécialité parmi ses kk premiers choix
Subject To
c_etudiant_0: x0_3 + x0_7 + x0_8 = 1
c_etudiant_1: x1_2 + x1_5 + x1_3 = 1
c_etudiant_2: x2_1 + x2_7 + x2_5 = 1
c_etudiant_3: x3_0 + x3_4 + x3_3 = 1
c_etudiant_4: x4_5 + x4_3 + x4_6 = 1
c_etudiant_5: x5_4 + x5_3 + x5_5 = 1
c_etudiant_6: x6_3 + x6_7 + x6_6 = 1
c_etudiant_7: x7_4 + x7_1 + x7_5 = 1
c_etudiant_8: x8_0 + x8_3 + x8_2 = 1
c_etudiant_9: x9_2 + x9_5 + x9_3 = 1
c_etudiant_10: x10_1 + x10_8 + x10_3 = 1
c_capacite_0: x3_0 + x8_0 <= 2
c_capacite_1: x2_1 + x7_1 + x10_1 <= 1
c_capacite_2: x1_2 + x8_2 + x9_2 <= 1
c_capacite_3: x0_3 + x1_3 + x3_3 + x4_3 + x5_3 + x6_3 + x8_3 + x9_3 + x10_3 <= 1
c_capacite_4: x3_4 + x5_4 + x7_4 <= 1
c_capacite_5: x1_5 + x2_5 + x4_5 + x5_5 + x7_5 + x9_5 <= 1
c_capacite_6: x4_6 + x6_6 <= 1
c_capacite_7: x0_7 + x2_7 + x6_7 <= 1
c_capacite_8: x0_8 + x10_8 <= 2
Binary
x0_3 x0_7 x0_8 x1_2 x1_5 x1_3 x2_1 x2_7 x2_5 x3_0 x3_4 x3_3 x4_5 x4_3 x4_6 x5_4 x5_3 x5_5 x6_3 x6_7 x6_6 x7_4 x7_1 x7_5 x8_0 x8_3 x8_2 x9_2 x9_5 x9_3 x10_1 x10_8 x10_3 
End
