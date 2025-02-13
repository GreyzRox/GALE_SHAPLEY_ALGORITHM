import unittest
import PrefEtuSpe
import galeshapley
import generate

class TestPrefEtuSpe(unittest.TestCase):
    def test_PrefEtu(self):
        expected = [
            [5, 7, 6, 8, 3, 2, 0, 1, 4],
            [6, 5, 0, 4, 7, 2, 8, 3, 1],
            [4, 0, 7, 2, 8, 3, 1, 6, 5],
            [6, 5, 7, 0, 8, 4, 3, 1, 2],
            [1, 6, 7, 5, 0, 2, 4, 8, 3],
            [0, 7, 4, 2, 8, 3, 1, 6, 5],
            [5, 7, 6, 2, 8, 3, 0, 1, 4],
            [7, 0, 4, 2, 8, 3, 1, 6, 5],
            [5, 7, 6, 2, 8, 3, 0, 1, 4],
            [2, 6, 5, 8, 3, 1, 4, 7, 0],
            [6, 4, 0, 8, 3, 1, 5, 2, 7]
        ]
        result = PrefEtuSpe.PrefEtu("../data/PrefEtu.txt")
        self.assertEqual(result, expected)
        print("fonction PrefEtu : OK")

    def test_PrefSpe(self):
        expected = [
            [7, 9, 5, 4, 3, 1, 0, 10, 6, 8, 2],
            [7, 5, 9, 4, 3, 1, 0, 10, 8, 6, 2],
            [3, 9, 5, 4, 7, 6, 1, 0, 10, 8, 2],
            [7, 9, 5, 4, 3, 1, 0, 6, 10, 8, 2],
            [10, 3, 0, 4, 5, 6, 7, 8, 9, 1, 2],
            [1, 0, 3, 4, 5, 6, 7, 2, 9, 10, 8],
            [0, 1, 3, 4, 5, 6, 7, 2, 8, 10, 9],
            [7, 6, 9, 5, 4, 3, 1, 0, 10, 8, 2],
            [1, 0, 3, 4, 5, 6, 7, 2, 9, 10, 8]
        ]
        result = PrefEtuSpe.PrefSpe("../data/PrefSpe.txt")
        self.assertEqual(result, expected)
        print("fonction PrefSpe : OK")

    def test_Capacite_spe(self):
        expected = [2, 1, 1, 1, 1, 1, 1, 1, 2]
        result = PrefEtuSpe.Capacite_spe("../data/PrefSpe.txt")
        self.assertEqual(result, expected)
        print("fonction Capacite_spe : OK")

class TestGaleShapley(unittest.TestCase):
    def setUp(self):
        self.liste_etu = PrefEtuSpe.PrefEtu("../data/PrefEtu.txt")
        self.liste_spe = PrefEtuSpe.PrefSpe("../data/PrefSpe.txt")
        self.capacite = PrefEtuSpe.Capacite_spe("../data/PrefSpe.txt")

    def test_galeshapley_etu(self):
        result = galeshapley.galeshapley_etu(self.liste_etu, self.liste_spe, self.capacite)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(self.liste_etu))
        self.assertEqual(galeshapley.paire_instable(result,self.liste_etu,self.liste_spe),[])
        print("fonction galeshapley_etu : OK")

    def test_galeshapley_spe(self):
        result = galeshapley.galeshapley_spe(self.liste_etu, self.liste_spe, self.capacite)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(self.liste_etu))
        self.assertEqual(galeshapley.paire_instable(result,self.liste_etu,self.liste_spe),[])
        print("fonction galeshapley_spe : OK")

class TestGenerate(unittest.TestCase):
    def test_genere_pref_etu(self):
        n = 10
        result = generate.genere_pref_etu(n)
        self.assertEqual(len(result), n)
        for prefs in result:
            self.assertEqual(len(prefs), 9)
        print("fonction genere_pref_etu : OK")

    def test_genere_pref_spe(self):
        n = 10
        result = generate.genere_pref_spe(n)
        self.assertEqual(len(result), 9)
        for prefs in result:
            self.assertEqual(len(prefs), n)
        print("fonction genere_pref_spe : OK")

    def test_genere_capacite(self):
        n = 10
        nb_spe = 3
        result = generate.genere_capacite(n, nb_spe)
        self.assertEqual(len(result), nb_spe)
        self.assertEqual(sum(result), n)
        print("fonction genere_capacite : OK")

if __name__ == '__main__':
    unittest.main()