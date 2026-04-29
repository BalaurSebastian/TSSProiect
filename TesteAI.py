import unittest
from ClasaTestare import NotareStudent  # inlocuieste cu numele modulului tau


class TestNotareStudent(unittest.TestCase):

    # -------------------------
    # Clase de echivalenta
    # -------------------------
    def test_valori_valide_tipice(self):
        s = NotareStudent(80, 70, 90)
        rezultat = s.evaluare_student(80, 70, 90)
        self.assertAlmostEqual(rezultat[0], 0.6*80 + 0.4*70)
        self.assertTrue(rezultat[1])

    def test_valori_limita_inferioara(self):
        s = NotareStudent(0, 0, 0)
        rezultat = s.evaluare_student(0, 0, 0)
        self.assertEqual(rezultat[0], 0)
        self.assertFalse(rezultat[1])

    def test_valori_limita_superioara(self):
        s = NotareStudent(100, 100, 100)
        rezultat = s.evaluare_student(100, 100, 100)
        self.assertEqual(rezultat[0], 100)
        self.assertTrue(rezultat[1])

    def test_input_invalid_examen(self):
        s = NotareStudent(0, 0, 0)
        with self.assertRaises(ValueError):
            s.evaluare_student(-1, 50, 50)

    def test_input_invalid_tema(self):
        s = NotareStudent(0, 0, 0)
        with self.assertRaises(ValueError):
            s.evaluare_student(50, 101, 50)

    def test_input_invalid_prezenta(self):
        s = NotareStudent(0, 0, 0)
        with self.assertRaises(ValueError):
            s.evaluare_student(50, 50, 200)

    # -------------------------
    # Acoperire instructiuni & decizii
    # -------------------------
    def test_prezenta_sub_50(self):
        s = NotareStudent(80, 80, 40)
        rezultat = s.evaluare_student(80, 80, 40)
        self.assertFalse(rezultat[1])

    def test_nota_sub_50(self):
        s = NotareStudent(40, 40, 80)
        rezultat = s.evaluare_student(40, 40, 80)
        self.assertFalse(rezultat[1])

    def test_nota_peste_50(self):
        s = NotareStudent(60, 60, 80)
        rezultat = s.evaluare_student(60, 60, 80)
        self.assertTrue(rezultat[1])

    # -------------------------
    # Acoperire conditii
    # -------------------------
    def test_conditie_bursa_adevarat(self):
        s = NotareStudent(90, 90, 90)
        rezultat = s.evaluare_student(90, 90, 90)
        self.assertTrue(rezultat[2])

    def test_conditie_bursa_fals_nota(self):
        s = NotareStudent(80, 80, 90)
        rezultat = s.evaluare_student(80, 80, 90)
        self.assertFalse(rezultat[2])

    def test_conditie_bursa_fals_prezenta(self):
        s = NotareStudent(90, 90, 70)
        rezultat = s.evaluare_student(90, 90, 70)
        self.assertFalse(rezultat[2])

    # -------------------------
    # Categorii (circuite independente)
    # -------------------------
    def test_categorie_picat(self):
        s = NotareStudent(40, 40, 80)
        rezultat = s.evaluare_student(40, 40, 80)
        self.assertEqual(rezultat[3], "Picat")

    def test_categorie_bine(self):
        s = NotareStudent(60, 60, 80)
        rezultat = s.evaluare_student(60, 60, 80)
        self.assertEqual(rezultat[3], "Bine")

    def test_categorie_foarte_bine(self):
        s = NotareStudent(80, 80, 80)
        rezultat = s.evaluare_student(80, 80, 80)
        self.assertEqual(rezultat[3], "Foarte bine")

    def test_categorie_excelent(self):
        s = NotareStudent(95, 95, 90)
        rezultat = s.evaluare_student(95, 95, 90)
        self.assertEqual(rezultat[3], "Excelent")

    # -------------------------
    # Mutanti (ex: schimbare operatori, praguri)
    # -------------------------
    def test_prag_50_exact(self):
        s = NotareStudent(50, 50, 80)
        rezultat = s.evaluare_student(50, 50, 80)
        self.assertTrue(rezultat[1])

    def test_prag_85_exact_bursa(self):
        s = NotareStudent(85, 85, 80)
        rezultat = s.evaluare_student(85, 85, 80)
        self.assertTrue(rezultat[2])

    def test_prag_80_prezenta_bursa(self):
        s = NotareStudent(90, 90, 80)
        rezultat = s.evaluare_student(90, 90, 80)
        self.assertTrue(rezultat[2])


if __name__ == "__main__":
    unittest.main()