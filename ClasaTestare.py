class StudentGrade:
    def __init__(self, nota_examen, nota_tema, prezenta):
        self.nota_examen = nota_examen        # 0 - 100
        self.nota_tema = nota_tema  # 0 - 100
        self.prezenta = prezenta        # 0 - 100 (%)

    def is_valid(self):
        if self.nota_examen < 0 or self.nota_examen > 100:
            return False
        if self.nota_tema < 0 or self.nota_tema > 100:
            return False
        if self.prezenta < 0 or self.prezenta > 100:
            return False
        return True

    def nota_finala(self):
        if not self.is_valid():
            raise ValueError("Invalid input")
        return 0.6 * self.nota_examen + 0.3 * self.nota_tema + 0.1 * self.prezenta
        # 60% examen, 30% tema, 10% prezenta
    def trecut(self):
        nota = self.nota_finala()
        if self.prezenta < 50:
            return False
        if nota >= 50:
            return True
        else:
            return False
        
    def eligibil_bursa(self):
        nota = self.nota_finala()
        if nota >= 85 and self.prezenta >= 90:
            return True
        else:
            return False
    def categorie_nota(self):
        nota = self.nota_finala()
        
        if nota < 0 or nota > 100:
            raise ValueError("Nota finala invalida")
        
        if nota < 50:
            return "Picat"
        elif nota < 70:
            return "Bine"
        elif nota < 90:
            return "Foarte bine"
        else:
            return "Excelent"
