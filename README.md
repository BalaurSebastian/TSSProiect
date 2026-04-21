# TSSProiect

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


