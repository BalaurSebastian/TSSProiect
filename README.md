# TSSProiect

## Partitionare in clase de echivalenta (Equivalence partitioning)

### Intrari: nota_examen, nota_tema, prezenta

### Domeniu de intrare:
- nota_examen: [0, 100]
- nota_tema: [0, 100]
- prezenta: [0, 100]

### Clase de echivalenta:
- nota_examen: [0, 100] - valid, < 0 - invalid, > 100 - invalid
- nota_tema: [0, 100] - valid, < 0 - invalid, > 100 - invalid
- prezenta: [0, 49] - valid,dar picat, [50, 100] - valid, < 0 - invalid, > 100 - invalid

### Domeniu de iesire(metoda trecut()):

    -True(studentul trece)
    -False(studentul pica)
    -Exceptie (date de intrare invalide)
  
### Clase de Echivalenta Globale:

    C1 - toate intrarile sunt valide si studentul trece
    C2 - toate intrarile sunt valide si studentul pica(prezenta < 50)
    C3 - toate intrarile sunt valide si studentul pica(nota_finala < 50)
    C4 - intrare invalida
