# # Partitionare in clase de echivalenta (Equivalence partitioning)

# # Impartim datele de intrare in clase tratate identic si alegem cate o valoare reprezentativa pentru fiecare clasa:

# # intrari: nota_examen, nota_tema, prezenta
# # Domeniu de intrare:
# # - nota_examen: [0, 100]
# # - nota_tema: [0, 100]
# # - prezenta: [0, 100]
# # Clase de echivalenta:
# # - nota_examen: [0, 100] - valid, < 0 - invalid, > 100 - invalid
# # - nota_tema: [0, 100] - valid, < 0 - invalid, > 100 - invalid
# # - prezenta: [0, 49] - valid,dar picat, [50, 100] - valid, < 0 - invalid, > 100 - invalid
# # Domeniu de iesire : (nota_finala, trecut, eligibil_bursa, categorie):
# # Clase de Echivalenta Globale:
# #     C1 - toate intrarile sunt valide si studentul trece
# #     C2 - toate intrarile sunt valide si studentul pica(prezenta < 50)
# #     C3 - toate intrarile sunt valide si studentul pica(nota_finala < 50)
# #     C4 - intrare invalida

# # Analiza Valorilor de frontiera (Boundary Value Analysis)

# # Pentru fiecare clasa de echivalenta alegem valori de sub limita, la limita si peste limita, in acest mod testam limitele de validare dar si cele logice impuse de aplicatie:

# # Validare:
# # B1-(-1, 50, 50)   # sub limita
# # B2-(0, 50, 50)    # limita
# # B3-(100, 50, 50)  # limita
# # B4-(101, 50, 50)  # peste limita
# # Prezenta:
# # B5-(80, 80, 49)  # pica
# # B6-(80, 80, 50)  # trece
# # B7-(80, 80, 51)  # trece
# # Nota Finala:
# # B8-(49, 49, 50)  # sub prag
# # B9-(50, 50, 50)   # prag
# # B10-(51, 51, 50)   # peste prag
# # Bursa:
# # B11-(85, 85, 80)  # exact prag → True
# # B12-(84, 85, 80)  # sub prag → False
# # B13-(90, 85, 79)  # sub prag → False

# # Conditie + Circuite independente

# # Obiectiv:
# # - acoperire la nivel de conditie pentru deciziile din metodele: is_valid, trecut, eligibil_bursa
# # - acoperire pe circuite independente pentru fluxurile principale din: trecut si categorie_nota

# # Conditii urmarite:
# # - is_valid: fiecare conditie de forma x < 0 sau x > 100 evaluata pe True/False
# # - trecut: prezenta < 50 si nota >= 50 evaluate pe True/False
# # - eligibil_bursa: (nota >= 85) si (prezenta >= 80) evaluate pe True/False

# # Circuite independente urmarite:
# # - trecut: invalid input, prezenta sub prag, trecut, picat din nota
# # - categorie_nota: Picat, Bine, Foarte bine, Excelent


# import unittest
# from ClasaTestare import NotareStudent

# class TestNotareStudent(unittest.TestCase):
#     def test_clase_echivalenta_C1(self):
#         student = NotareStudent(80, 80, 80)
#         self.assertTrue(student.trecut())
        
#     def test_clase_echivalenta_C2(self):
#         student = NotareStudent(80, 80, 40)
#         self.assertFalse(student.trecut())

#     def test_clase_echivalenta_C3(self):
#         student = NotareStudent(40, 40, 80)
#         self.assertFalse(student.trecut())

#     def test_clase_echivalenta_C4(self):
#         student = NotareStudent(-10, 80, 80)
#         with self.assertRaises(ValueError):
#             student.trecut()
    
    
    
#     def test_valori_frontiera_B1(self):
#         student = NotareStudent(-1, 50, 50)
#         with self.assertRaises(ValueError):
#             student.nota_finala()
            
#     def test_valori_frontiera_B2(self):
#         student = NotareStudent(0, 50, 50)
#         self.assertTrue(student.nota_finala())
    
#     def test_valori_frontiera_B3(self):
#         student = NotareStudent(100, 50, 50)
#         self.assertTrue(student.nota_finala())
        
#     def test_valori_frontiera_B4(self):
#         student = NotareStudent(101, 50, 50)
#         with self.assertRaises(ValueError):
#             student.nota_finala()
    
    

#     def test_valori_frontiera_B5(self):
#         student = NotareStudent(80, 80, 49)
#         self.assertFalse(student.trecut())
    
#     def test_valori_frontiera_B6(self):
#         student = NotareStudent(80, 80, 50)
#         self.assertTrue(student.trecut())
    
#     def test_valori_frontiera_B7(self):
#         student = NotareStudent(80, 80, 51)
#         self.assertTrue(student.trecut())
    
    
#     def test_valori_frontiera_B8(self):
#         student = NotareStudent(49, 49, 50)
#         self.assertFalse(student.trecut())
    
#     def test_valori_frontiera_B9(self):
#         student = NotareStudent(50, 50, 50)
#         self.assertTrue(student.trecut())
    
#     def test_valori_frontiera_B10(self):
#         student = NotareStudent(51, 51, 50)
#         self.assertTrue(student.trecut())
    
    
#     def test_valori_frontiera_B11(self):
#         student = NotareStudent(85, 85, 80)
#         self.assertTrue(student.eligibil_bursa())
    
#     def test_valori_frontiera_B12(self):
#         student = NotareStudent(84, 85, 80)
#         self.assertFalse(student.eligibil_bursa())
#     def test_valori_frontiera_B13(self):
#         student = NotareStudent(85, 85, 79)
#         self.assertFalse(student.eligibil_bursa())
        
#     # Teste pentru omorarea mutantilor
#     def test_is_valid_prezenta_egal_0_returneaza_true(self): #Job 36
#         student = NotareStudent(50, 50, 0)
#         self.assertTrue(student.is_valid())
        
#     def test_categorie_nota_nota_finala_egala_50_returneaza_bine(self): #Job 39
#         student = NotareStudent(50, 50, 50)
#         self.assertEqual(student.categorie_nota(), "Bine")


# # Acoperire la nivel de conditie
# class TestConditie(unittest.TestCase):
#     def test_conditie_valida_nota_tema_invalida(self):
#         student = NotareStudent(50, -1, 50)
#         self.assertFalse(student.is_valid())

#     def test_conditie_valida_prezenta_invalida(self):
#         student = NotareStudent(50, 50, 101)
#         self.assertFalse(student.is_valid())

#     def test_conditie_trecut_nota_sub_prag(self):
#         student = NotareStudent(40, 40, 50)
#         self.assertFalse(student.trecut())

#     def test_conditie_eligibil_bursa_nota_sub_prag(self):
#         student = NotareStudent(84, 85, 80)
#         self.assertFalse(student.eligibil_bursa())


# # Acoperire pe circuite independente
# class TestCircuiteIndependente(unittest.TestCase):
#     def test_circuit_trecut_invalid_input(self):
#         student = NotareStudent(-1, 80, 80)
#         with self.assertRaises(ValueError):
#             student.trecut()

#     def test_circuit_trecut_prezenta_sub_prag(self):
#         student = NotareStudent(80, 80, 49)
#         self.assertFalse(student.trecut())

#     def test_circuit_trecut_prezenta_ok_nota_ok(self):
#         student = NotareStudent(70, 70, 80)
#         self.assertTrue(student.trecut())

#     def test_circuit_trecut_prezenta_ok_nota_sub_prag(self):
#         student = NotareStudent(40, 40, 80)
#         self.assertFalse(student.trecut())

#     def test_circuit_categorie_bine(self):
#         student = NotareStudent(60, 60, 80)
#         self.assertEqual(student.categorie_nota(), "Bine")

#     def test_circuit_categorie_foarte_bine(self):
#         student = NotareStudent(80, 80, 80)
#         self.assertEqual(student.categorie_nota(), "Foarte bine")

#     def test_circuit_categorie_excelent(self):
#         student = NotareStudent(95, 95, 80)
#         self.assertEqual(student.categorie_nota(), "Excelent")

# if __name__ == '__main__':
#     unittest.main()
import unittest
from ClasaTestare import NotareStudent

class TestNotareStudent(unittest.TestCase):

    def test_clase_echivalenta_C1(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(80, 80, 80)
        self.assertTrue(trecut)

    def test_clase_echivalenta_C2(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(80, 80, 40)
        self.assertFalse(trecut)

    def test_clase_echivalenta_C3(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(40, 40, 80)
        self.assertFalse(trecut)

    def test_clase_echivalenta_C4(self):
        s = NotareStudent(0,0,0)
        with self.assertRaises(ValueError):
            s.evaluare_student(-10, 80, 80)
            

    def test_B1_invalid_sub(self):
        s = NotareStudent(0,0,0)
        with self.assertRaises(ValueError):
            s.evaluare_student(-1, 50, 50)

    def test_B2_limita_0(self):
        s = NotareStudent(0,0,0)
        nota, _, _, _ = s.evaluare_student(0, 50, 50)
        self.assertEqual(nota, 0.6*0 + 0.4*50)

    def test_B3_limita_100(self):
        s = NotareStudent(0,0,0)
        nota, _, _, _ = s.evaluare_student(100, 50, 50)
        self.assertEqual(nota, 0.6*100 + 0.4*50)

    def test_B4_peste_limita(self):
        s = NotareStudent(0,0,0)
        with self.assertRaises(ValueError):
            s.evaluare_student(101, 50, 50)

    def test_B5_prezenta_49(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(80, 80, 49)
        self.assertFalse(trecut)

    def test_B6_prezenta_50(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(80, 80, 50)
        self.assertTrue(trecut)

    def test_B7_prezenta_51(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(80, 80, 51)
        self.assertTrue(trecut)

    def test_B8_nota_sub_50(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(49, 49, 50)
        self.assertFalse(trecut)

    def test_B9_nota_50(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(50, 50, 50)
        self.assertTrue(trecut)

    def test_B10_nota_51(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(51, 51, 50)
        self.assertTrue(trecut)

    def test_B11_bursa_prag(self):
        s = NotareStudent(0,0,0)
        _, _, bursa, _ = s.evaluare_student(85, 85, 80)
        self.assertTrue(bursa)

    def test_B12_bursa_sub_nota(self):
        s = NotareStudent(0,0,0)
        _, _, bursa, _ = s.evaluare_student(84, 85, 80)
        self.assertFalse(bursa)

    def test_B13_bursa_sub_prezenta(self):
        s = NotareStudent(0,0,0)
        _, _, bursa, _ = s.evaluare_student(90, 85, 79)
        self.assertFalse(bursa)


    def test_mutant_prezenta_0(self): # Job 36
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(50, 50, 0)
        self.assertEqual(trecut, False)

    def test_mutant_categorie_50(self): # Job 38
        s = NotareStudent(0,0,0)
        _, _, _, categorie = s.evaluare_student(50, 50, 50)
        self.assertEqual(categorie, "Bine")


class TestConditie(unittest.TestCase):

    def test_conditie_invalid_nota_tema(self):
        s = NotareStudent(0,0,0)
        with self.assertRaises(ValueError):
            s.evaluare_student(50, -1, 50)

    def test_conditie_invalid_prezenta(self):
        s = NotareStudent(0,0,0)
        with self.assertRaises(ValueError):
            s.evaluare_student(50, 50, 101)

    def test_conditie_trecut_nota_sub_prag(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(40, 40, 50)
        self.assertFalse(trecut)

    def test_conditie_bursa_nota_sub_prag(self):
        s = NotareStudent(0,0,0)
        _, _, bursa, _ = s.evaluare_student(84, 85, 80)
        self.assertFalse(bursa)


class TestCircuiteIndependente(unittest.TestCase):

    def test_circuit_invalid(self):
        s = NotareStudent(0,0,0)
        with self.assertRaises(ValueError):
            s.evaluare_student(-1, 80, 80)

    def test_circuit_prezenta_mica(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(80, 80, 49)
        self.assertFalse(trecut)

    def test_circuit_trecut(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(70, 70, 80)
        self.assertTrue(trecut)

    def test_circuit_picat_nota(self):
        s = NotareStudent(0,0,0)
        _, trecut, _, _ = s.evaluare_student(40, 40, 80)
        self.assertFalse(trecut)

    def test_categorie_bine(self):
        s = NotareStudent(0,0,0)
        _, _, _, categorie = s.evaluare_student(60, 60, 80)
        self.assertEqual(categorie, "Bine")

    def test_categorie_foarte_bine(self):
        s = NotareStudent(0,0,0)
        _, _, _, categorie = s.evaluare_student(80, 80, 80)
        self.assertEqual(categorie, "Foarte bine")

    def test_categorie_excelent(self):
        s = NotareStudent(0,0,0)
        _, _, _, categorie = s.evaluare_student(95, 95, 80)
        self.assertEqual(categorie, "Excelent")


if __name__ == '__main__':
    unittest.main()