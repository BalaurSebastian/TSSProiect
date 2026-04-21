# Partitionare in clase de echivalenta (Equivalence partitioning)

# Impartim datele de intrare in clase tratate identic si alegem cate o valoare reprezentativa pentru fiecare clasa:

# intrari: nota_examen, nota_tema, prezenta
# Domeniu de intrare:
# - nota_examen: [0, 100]
# - nota_tema: [0, 100]
# - prezenta: [0, 100]
# Clase de echivalenta:
# - nota_examen: [0, 100] - valid, < 0 - invalid, > 100 - invalid
# - nota_tema: [0, 100] - valid, < 0 - invalid, > 100 - invalid
# - prezenta: [0, 49] - valid,dar picat, [50, 100] - valid, < 0 - invalid, > 100 - invalid
# Domeniu de iesire( metroda trecut()):
#     -True(studentul trece)
#     -False(studentul pica)
#     -Exceptie (date de intrare invalide)
# Clase de Echivalenta Globale:
#     C1 - toate intrarile sunt valide si studentul trece
#     C2 - toate intrarile sunt valide si studentul pica(prezenta < 50)
#     C3 - toate intrarile sunt valide si studentul pica(nota_finala < 50)
#     C4 - intrare invalida

# Analiza Valorilor de frontiera (Boundary Value Analysis)

# Pentru fiecare clasa de echivalenta alegem valori de sub limita, la limita si peste limita, in acest mod testam limitele de validare dar si cele logice impuse de aplicatie:

# Validare:
# B1-(-1, 50, 50)   # sub limita
# B2-(0, 50, 50)    # limita
# B3-(100, 50, 50)  # limita
# B4-(101, 50, 50)  # peste limita
# Prezenta:
# B5-(80, 80, 49)  # pica
# B6-(80, 80, 50)  # trece
# B7-(80, 80, 51)  # trece
# Nota Finala:
# B8-(49, 49, 50)  # sub prag
# B9-(50, 50, 50)   # prag
# B10-(51, 51, 50)   # peste prag
# Bursa:
# B11-(85, 85, 80)  # exact prag → True
# B12-(84, 85, 80)  # sub prag → False
# B13-(90, 85, 79)  # sub prag → False



import unittest
from ClasaTestare import NotareStudent

class TestNotareStudent(unittest.TestCase):
    def test_clase_echivalenta_C1(self):
        student = NotareStudent(80, 80, 80)
        self.assertTrue(student.trecut())
        
    def test_clase_echivalenta_C2(self):
        student = NotareStudent(80, 80, 40)
        self.assertFalse(student.trecut())

    def test_clase_echivalenta_C3(self):
        student = NotareStudent(40, 40, 80)
        self.assertFalse(student.trecut())

    def test_clase_echivalenta_C4(self):
        student = NotareStudent(-10, 80, 80)
        with self.assertRaises(ValueError):
            student.trecut()
    
    
    
    def test_valori_frontiera_B1(self):
        student = NotareStudent(-1, 50, 50)
        with self.assertRaises(ValueError):
            student.nota_finala()
            
    def test_valori_frontiera_B2(self):
        student = NotareStudent(0, 50, 50)
        self.assertTrue(student.nota_finala())
    
    def test_valori_frontiera_B3(self):
        student = NotareStudent(100, 50, 50)
        self.assertTrue(student.nota_finala())
        
    def test_valori_frontiera_B4(self):
        student = NotareStudent(101, 50, 50)
        with self.assertRaises(ValueError):
            student.nota_finala()
    
    

    def test_valori_frontiera_B5(self):
        student = NotareStudent(80, 80, 49)
        self.assertFalse(student.trecut())
    
    def test_valori_frontiera_B6(self):
        student = NotareStudent(80, 80, 50)
        self.assertTrue(student.trecut())
    
    def test_valori_frontiera_B7(self):
        student = NotareStudent(80, 80, 51)
        self.assertTrue(student.trecut())
    
    
    def test_valori_frontiera_B8(self):
        student = NotareStudent(49, 49, 50)
        self.assertFalse(student.trecut())
    
    def test_valori_frontiera_B9(self):
        student = NotareStudent(50, 50, 50)
        self.assertTrue(student.trecut())
    
    def test_valori_frontiera_B10(self):
        student = NotareStudent(51, 51, 50)
        self.assertTrue(student.trecut())
    
    
    def test_valori_frontiera_B11(self):
        student = NotareStudent(85, 85, 80)
        self.assertTrue(student.eligibil_bursa())
    
    def test_valori_frontiera_B12(self):
        student = NotareStudent(84, 85, 80)
        self.assertFalse(student.eligibil_bursa())
    def test_valori_frontiera_B13(self):
        student = NotareStudent(85, 85, 79)
        self.assertFalse(student.eligibil_bursa())

if __name__ == '__main__':
    unittest.main()