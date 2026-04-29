# TSSProiect

## Configuratia Hardware<br/>
-TBD

## Configuratia Software<br/>
-Sistem de operare Windows<br/>
-Python 3.13.x

## Structura Proiectului

<img width="638" height="841" alt="image" src="https://github.com/user-attachments/assets/ed407795-ab70-4367-aeaa-46a445b9f5e8" />


## 1. Partitionare in clase de echivalenta (Equivalence Partitioning)

### Intrari: nota_examen, nota_tema, prezenta

---

### Domeniu de intrare:
- nota_examen ∈ [0, 100]
- nota_tema ∈ [0, 100]
- prezenta ∈ [0, 100]

---

### Clase de echivalenta (pe fiecare intrare)

### nota_examen:
- N1 = [0, 100] (valid)
- N2 = {x | x < 0} (invalid)
- N3 = {x | x > 100} (invalid)

### nota_tema:
- T1 = [0, 100] (valid)
- T2 = {x | x < 0} (invalid)
- T3 = {x | x > 100} (invalid)

### prezenta:
- P1 = [0, 49] (valid, dar insuficient pentru promovare)
- P2 = [50, 100] (valid)
- P3 = {x | x < 0} (invalid)
- P4 = {x | x > 100} (invalid)


### Domeniu de iesire (metoda evaluare_student)

### Metoda returneaza:

---

- nota_finala (float)
- trecut (True / False)
- eligibil_bursa (True / False)
- categorie (string)

---

### Clase de echivalenta pentru iesire

### pentru trecut:
- R1 = studentul promoveaza (prezenta ≥ 50 si nota_finala ≥ 50)
- R2 = studentul nu promoveaza (prezenta < 50 sau nota_finala < 50)

### pentru eligibil_bursa:
- B1 = eligibil (nota_finala ≥ 85 si prezenta ≥ 80)
- B2 = neeligibil (orice alt caz)

### pentru categorie:
- C1 = Picat (nota_finala < 50)
- C2 = Bine (50 ≤ nota_finala < 70)
- C3 = Foarte bine (70 ≤ nota_finala < 90)
- C4 = Excelent (nota_finala ≥ 90)

---

## Clase de echivalenta globale

Clasele globale sunt obtinute prin combinarea intrarilor:

C1 = (nota_examen ∈ N1, nota_tema ∈ T1, prezenta ∈ P2)
     → studentul promoveaza

C2 = (nota_examen ∈ N1, nota_tema ∈ T1, prezenta ∈ P1)
     → studentul nu promoveaza (din cauza prezentei)

C3 = (nota_examen ∈ N1, nota_tema ∈ T1, prezenta ∈ P2, dar nota_finala < 50)
     → studentul nu promoveaza (din cauza notei)

C4 = (nota_examen ∈ N2 ∪ N3 ∪ T2 ∪ T3 ∪ P3 ∪ P4)
     → intrare invalida (ValueError)

---

## C: ( nota_examen, nota_tema, prezenta) -> (nota_finala, trecut, eligibil_bursa, categorie)</br>

| Nota examen | Nota tema | Prezenta | Rezultat asteptat (evaluare_student) |
|------------|----------|----------|----------------------------------------|
| 80         | 80       | 80       | (72.0, True, False, "Foarte bine")     |
| 80         | 80       | 40       | (72.0, False, False, "Foarte bine")    |
| 40         | 40       | 80       | (40.0, False, False, "Picat")          |
| -10        | 80       | 80       | ValueError                             |
| 0          | 50       | 50       | (20.0, False, False, "Picat")          |
| 100        | 50       | 50       | (80.0, True, False, "Foarte bine")     |
| 49         | 49       | 50       | (48.0, False, False, "Picat")          |
| 50         | 50       | 50       | (50.0, True, False, "Bine")            |
| 51         | 51       | 50       | (51.0, True, False, "Bine")            |
| 85         | 85       | 80       | (85.0, True, True, "Excelent")         |
| 84         | 85       | 80       | (83.6, True, False, "Foarte bine")     |
| 90         | 85       | 79       | (87.0, True, False, "Foarte bine")     |


<img width="593" height="496" alt="image" src="https://github.com/user-attachments/assets/725740a2-c9bd-46e9-8ee2-7479bce195d8" />


# 2. Analiza valorilor de frontieră (Boundary Value Analysis)

Analiza valorilor de frontieră este utilizată împreună cu partiționarea de echivalență și se concentrează pe testarea valorilor aflate la limitele claselor de echivalență, deoarece acestea sunt frecvent surse de erori.

Pentru clasa `NotareStudent`, valorile de frontieră sunt definite pentru fiecare intrare: `nota_examen`, `nota_tema` și `prezenta`.

---

## Domenii și valori de frontieră

Valorile de frontieră sunt alese pentru a testa:
- limitele domeniului de intrare (0 și 100)
- valori imediat sub și peste limite (-1 și 101)
- pragurile logice ale aplicației (50 pentru promovare, 85 pentru bursă, 80 pentru prezență)

### nota_examen și nota_tema:
- domeniu valid: [0, 100]
- valori de frontieră:
  - sub limită: -1
  - limită inferioară: 0
  - limită superioară: 100
  - peste limită: 101

### prezenta:
- domeniu valid: [0, 100]
- valori de frontieră:
  - sub limită: -1
  - limită inferioară: 0
  - prag de promovare: 49, 50, 51
  - limită superioară: 100
  - peste limită: 101

---

## Set de teste (Boundary Value Analysis)

B1  (-1, 50, 50)   → ValueError (nota_examen sub limită)  
B2  (0, 50, 50)    → valid → (20.0, False, False, "Picat")  
B3  (100, 50, 50)  → valid → (80.0, True, False, "Foarte bine")  
B4  (101, 50, 50)  → ValueError (nota_examen peste limită)  

B5  (80, 80, 49)   → (72.0, False, False, "Foarte bine")  
B6  (80, 80, 50)   → (72.0, True, False, "Foarte bine")  
B7  (80, 80, 51)   → (72.0, True, False, "Foarte bine")  

B8  (49, 49, 50)   → (48.0, False, False, "Picat")  
B9  (50, 50, 50)   → (50.0, True, False, "Bine")  
B10 (51, 51, 50)   → (51.0, True, False, "Bine")  

B11 (85, 85, 80)   → (85.0, True, True, "Excelent")  
B12 (84, 85, 80)   → (83.6, True, False, "Foarte bine")  
B13 (90, 85, 79)   → (87.0, True, False, "Foarte bine")  

---

## Tabel valori de frontieră

| Nota examen | Nota tema | Prezenta | Rezultat asteptat |
|-------------|-----------|----------|-------------------|
| -1          | 50        | 50       | ValueError        |
| 0           | 50        | 50       | (20.0, False, False, "Picat") |
| 100         | 50        | 50       | (80.0, True, False, "Foarte bine") |
| 101         | 50        | 50       | ValueError        |
| 80          | 80        | 49       | (72.0, False, False, "Foarte bine") |
| 80          | 80        | 50       | (72.0, True, False, "Foarte bine") |
| 80          | 80        | 51       | (72.0, True, False, "Foarte bine") |
| 49          | 49        | 50       | (48.0, False, False, "Picat") |
| 50          | 50        | 50       | (50.0, True, False, "Bine") |
| 51          | 51        | 50       | (51.0, True, False, "Bine") |
| 85          | 85        | 80       | (85.0, True, True, "Excelent") |
| 84          | 85        | 80       | (83.6, True, False, "Foarte bine") |
| 90          | 85        | 79       | (87.0, True, False, "Foarte bine") |

---
<img width="517" height="583" alt="image" src="https://github.com/user-attachments/assets/065054b7-4513-495f-aa18-bd8518596b61" />

## Diagrama CFG
![description](https://github.com/BalaurSebastian/TSSProiect/blob/main/Diagrama%20CFG.png)
  
## Acoperire structurală (Structural Coverage)

### Tipuri de acoperire:
- statement coverage
- decision coverage
- condition coverage
- circuite independente

---

### 1. Statement coverage (acoperire la nivel de instrucțiune)

Fiecare instrucțiune este executată macar o data (fiecare nod din graf este parcurs macar odata):

| Test | Input | Acoperă |
|------|------|--------|
| test_circuit_trecut | (70,70,80) | flux complet valid |
| test_circuit_prezenta_mica | (80,80,49) | ramura prezenta < 50 |
| test_circuit_picat_nota | (40,40,80) | ramura nota < 50 |
| test_categorie_excelent | (95,95,80) | categorie finală |
| test_categorie_bine | (60,60,80) | categorie medie |
| test_categorie_foarte_bine | (80,80,80) | categorie intermediară |
| test_circuit_invalid | (-1,80,80) | excepție |


---

### 2. Decision coverage (acoperire la nivel de decizie)

Fiecare decizie (if) este evaluată atât pe True cât și pe False (fiecare ramura a grafului este parcursa macar o data):

| Decizie | True (test) | False (test) |
|--------|------------|-------------|
| validare input | test_circuit_invalid | restul testelor |
| prezenta < 50 | test_circuit_prezenta_mica | test_circuit_trecut |
| nota >= 50 | test_circuit_trecut | test_circuit_picat_nota |
| nota >= 85 | test_categorie_excelent | test_conditie_bursa_nota_sub_prag |
| prezenta >= 80 | test_categorie_excelent | test_conditie_bursa_nota_sub_prag |
| nota < 50 | test_circuit_picat_nota | test_categorie_bine |
| nota < 70 | test_categorie_bine | test_categorie_foarte_bine |
| nota < 90 | test_categorie_foarte_bine | test_categorie_excelent |


---

### 3. Condition coverage (acoperire la nivel de condiție)

Fiecare condiție individuala este evaluată pe True și False:

| Condiție | True (test) | False (test) |
|----------|------------|-------------|
| nota_tema < 0 | test_conditie_invalid_nota_tema | test_circuit_trecut |
| prezenta > 100 | test_conditie_invalid_prezenta | test_circuit_trecut |
| prezenta < 50 | test_circuit_prezenta_mica | test_circuit_trecut |
| nota >= 50 | test_circuit_trecut | test_circuit_picat_nota |
| nota >= 85 | test_categorie_excelent | test_conditie_bursa_nota_sub_prag |
| prezenta >= 80 | test_categorie_excelent | test_conditie_bursa_nota_sub_prag |

---

### 4. Circuite independente

Pe baza grafului, fiecare circuit este acoperit de cel puțin un test:

| Circuit | Descriere | Test |
|--------|----------|------|
| P1 | Input invalid → excepție | test_circuit_invalid |
| P2 | Prezenta < 50 → picat | test_circuit_prezenta_mica |
| P3 | Prezenta OK, nota < 50 → picat | test_circuit_picat_nota |
| P4 | Student trecut | test_circuit_trecut |
| P5 | Categorie "Bine" | test_categorie_bine |
| P6 | Categorie "Foarte bine" | test_categorie_foarte_bine |
| P7 | Categorie "Excelent" | test_categorie_excelent |

---

## Testarea prin mutatii

Am folosit libraria cosmic-ray pentru a genera mutatiile.

Avantajele librariei cosmic-ray fata de mutmut:

* Executie configurabila

  Cosmic-ray permite alegerea executorului de teste, in timp ce mutmut foloseste doar pytest. Acest lucru este in special important pentru acest proiect fiindca pentru testare folosim unittest.

* Baza de date detaliata

  Cosmic-ray salveaza mutatiile intr-o baza de date sqlite. Pentru fiecare mutatie salveaza si anumite specificatii care includ numele operatorilor care au fost inlocuiti. Mutmut salveaza mutantii sub forma de fisiere intr-un folder. Datorita bazei de date si a specificatiilor detaliate, mutantii generati de cosmic-ray sunt mai usor de vizualizat si filtrat.

* Raport HTML

  Cosmic-ray poate genera un raport HTML care include detaliile salvate in baza de date, in timp ce mutmut necesita folosirea interfetei din terminal.

Pasii pe care i-am urmat pentru a realiza testarea prin mutatii [1]:

* Dupa instalare, mai intai am creat fisierul de configuratie `ray-config.toml`

* Apoi am initializat sesiunea (am generat mutantii) prin comanda: `cosmic-ray init ray-config.toml mutants.sqlite`

* In continuare, am verificat ca testele trec pe codul nemutat (baseline). Am folosit comanda: `cosmic-ray --verbosity=INFO baseline ray-config.toml`

* Mai departe, am pornit executarea testelor pe mutanti: `cosmic-ray exec ray-config.toml mutants.sqlite`

* La final, am generat raportul HTML: `cr-html ray-config.sqlite > report.html`

### Analiza raportului creat de generatorul de mutanti

Generatorul a creat 143 de mutanti, dintre care 24 au supravietuit.

Am adaugat inca doua teste pentru a omori 2 dintre mutanti. Dupa adaugarea acestor teste au mai fost omorati inca 4 mutanti, ramanand doar 18. Cele doua teste au tintit mutantii 36 si 38.

#### Mutantul 36

```python
--- mutation diff ---
--- aClasaTestare.py
+++ bClasaTestare.py
@@ -10,7 +10,7 @@
             raise ValueError("Invalid input")
         if nota_tema < 0 or nota_tema > 100:
             raise ValueError("Invalid input")
-        if prezenta < 0 or prezenta > 100:
+        if prezenta == 0 or prezenta > 100:
             raise ValueError("Invalid input")
 
         # calcul
```

Testul adaugat

```python
def test_mutant_prezenta_0(self): # Job 36
    s = NotareStudent(0,0,0)
    _, trecut, _, _ = s.evaluare_student(50, 50, 0)
    self.assertEqual(trecut, False)
```

#### Mutantul 38

```python
--- mutation diff ---
--- aClasaTestare.py
+++ bClasaTestare.py
@@ -31,7 +31,7 @@
            eligibil_bursa = False

        # categorie
-        if nota_finala < 50:
+        if nota_finala == 50:
            categorie = "Picat"
        elif nota_finala < 70:
            categorie = "Bine"
```

Testul adaugat

```python
def test_mutant_categorie_50(self): # Job 38
    s = NotareStudent(0,0,0)
    _, _, _, categorie = s.evaluare_student(50, 50, 50)
    self.assertEqual(categorie, "Bine")
```

## Prezentare Powerpoint

https://github.com/BalaurSebastian/TSSProiect/blob/main/PrezentareProiect.pptx


## Raport folosire AI pentru creare teste

### Prompt folosit: 

```
Asta este clasa mea in python:

class NotareStudent:

def __init__(self, nota_examen, nota_tema, prezenta):
     self.nota_examen = nota_examen # 0 - 100
     self.nota_tema = nota_tema # 0 - 100
     self.prezenta = prezenta # 0 - 100 (%)

def evaluare_student(self, nota_examen, nota_tema, prezenta):
      # validare
     if nota_examen < 0 or nota_examen > 100:
          raise ValueError("Invalid input")
     if nota_tema < 0 or nota_tema > 100:
          raise ValueError("Invalid input")
     if prezenta < 0 or prezenta > 100:
          raise ValueError("Invalid input")
     # calcul
     nota_finala = 0.6 * nota_examen + 0.4 * nota_tema
     # trecut
     if prezenta < 50:
          trecut = False
     elif nota_finala >= 50:
          trecut = True
     else:
          trecut = False
     # bursa
     if nota_finala >= 85 and prezenta >= 80:
          eligibil_bursa = True
     else:
          eligibil_bursa = False
     # categorie
     if nota_finala < 50:
          categorie = "Picat"
     elif nota_finala < 70:
          categorie = "Bine"
     elif nota_finala < 90:
          categorie = "Foarte bine"
     else:
          categorie = "Excelent"
     return nota_finala, trecut, eligibil_bursa, categorie

Creeaza o serie de teste pentru a demonstra partitionare pe clase de echivalenta, acoperire la nivel de instructiune, decizie, conditie, circuite independente si omorare de mutanti. Pune doar testele intr-un singur bloc usor copiabil.
```

### Rezultat prompt

```python
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
```

### Rulare teste

<img width="492" height="179" alt="image" src="https://github.com/user-attachments/assets/6d6d6a33-7761-45bc-823f-177e432f7936" />

### Raport Coverage

### Raport Mutanti

## Bibliografie

[1] _Tutorial: The basics_, https://cosmic-ray.readthedocs.io/en/latest/tutorials/intro/index.html, Data ultimei accesari: 28 aprilie 2026
