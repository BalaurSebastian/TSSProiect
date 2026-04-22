# TSSProiect

## Structura Proiectului

Clasa "Notare Student" implementata in python.<br/>
Primeste ca date de intrare 3 parametrii: nota_examen, nota_tema, prezenta.<br/>
Contine urmatoarele metode:<br/>
-"is_valid()" - verifica daca valorile de intrare sunt corecte (intre 0 si 100)<br/>
-"nota_finala()" - calculeaza nota finala a studentului utilizand o medie ponderata (60% nota_examen, 40% nota_tema)<br/>
-"trecut()" - determina daca studentul a promovat pe baza notei finale si a prezentei<br/>
-"categorie_nota()" - clasifica nota finala in categorii (Picat, Bine, Foarte Bine, Excelent)<br/>
-"eligibil_bursa()" - verifica daca studentul indeplineste conditiile de bursa (nota finala >= 85 , prezenta >= 80) <br/>

## Partitionare in clase de echivalenta (Equivalence partitioning)

### Intrari: nota_examen, nota_tema, prezenta

### Domeniu de intrare:
- nota_examen: [0, 100]
- nota_tema: [0, 100]
- prezenta: [0, 100]
  
### Impartim datele de intrare in clase tratate identic si alegem cate o valoare reprezentativa pentru fiecare clasa:

### Clase de echivalenta:
- nota_examen: [0, 100] - valid, < 0 - invalid, > 100 - invalid
- nota_tema: [0, 100] - valid, < 0 - invalid, > 100 - invalid
- prezenta: [0, 49] - valid,dar picat, [50, 100] - valid, < 0 - invalid, > 100 - invalid

### Domeniu de iesire(metoda trecut()):
```
    -True(studentul trece)
    -False(studentul pica)
    -Exceptie (date de intrare invalide)
```
### Clase de Echivalenta Globale:
```
    C1 - toate intrarile sunt valide si studentul trece
    C2 - toate intrarile sunt valide si studentul pica(prezenta < 50)
    C3 - toate intrarile sunt valide si studentul pica(nota_finala < 50)
    C4 - intrare invalida
```
## Analiza Valorilor de frontiera (Boundary Value Analysis)

### Pentru fiecare clasa de echivalenta alegem valori de sub limita, la limita si peste limita, in acest mod testam limitele de validare dar si cele logice impuse de aplicatie:

### Validare:
```
B1-(-1, 50, 50)   - sub limita
B2-(0, 50, 50)    - limita
B3-(100, 50, 50)  - limita
B4-(101, 50, 50)  - peste limita
```
### Prezenta:
```
B5-(80, 80, 49)  - pica
B6-(80, 80, 50)  - trece
B7-(80, 80, 51)  - trece
```
### Nota Finala:
```
B8-(49, 49, 50)  - sub prag
B9-(50, 50, 50)  - prag
B10-(51, 51, 50) - peste prag
```
### Bursa:
```
B11-(85, 85, 80)  - exact prag → True
B12-(84, 85, 80)  - sub prag (nota) → False
B13-(90, 85, 79)  - sub prag (prezenta) → False
```

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
