# TSSProiect

## Configuratia Hardware<br/>
-TBD

## Configuratia Software<br/>
-Sistem de operare Windows<br/>
-Python 3.13.x

## Structura Proiectului

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

## Diagrama CFG
![description](https://github.com/BalaurSebastian/TSSProiect/blob/main/Diagrama%20CFG.png)
  
## Acoperirea la nivel de conditie + Circuite independente

### Obiectiv:
- acoperire la nivel de conditie pentru deciziile din metodele: is_valid, trecut, eligibil_bursa
- acoperire pe circuite independente pentru fluxurile principale din: trecut si categorie_nota

#### Conditii urmarite:
- is_valid: fiecare conditie de forma x < 0 sau x > 100 evaluata pe True/False
- trecut: prezenta < 50 si nota >= 50 evaluate pe True/False
- eligibil_bursa: (nota >= 85) si (prezenta >= 80) evaluate pe True/False

#### Circuite independente urmarite:
- trecut: invalid input, prezenta sub prag, trecut, picat din nota
- categorie_nota: Picat, Bine, Foarte bine, Excelent

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


## Bibliografie

[1] _Tutorial: The basics_, https://cosmic-ray.readthedocs.io/en/latest/tutorials/intro/index.html, Data ultimei accesari: 28 aprilie 2026
