class NotareStudent:
    def __init__(self, nota_examen, nota_tema, prezenta):
        self.nota_examen = nota_examen        # 0 - 100
        self.nota_tema = nota_tema  # 0 - 100
        self.prezenta = prezenta        # 0 - 100 (%)

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
    # def nota_finala(self):
    #     if not self.is_valid():
    #         raise ValueError("Invalid input")
    #     return 0.6 * self.nota_examen + 0.4 * self.nota_tema
    #     # 60% examen, 40% tema
    # def trecut(self):
    #     nota = self.nota_finala()
    #     if self.prezenta < 50:
    #         return False
    #     if nota >= 50:
    #         return True
    #     else:
    #         return False
        
    # def eligibil_bursa(self):
    #     nota = self.nota_finala()
    #     if nota >= 85 and self.prezenta >= 80:
    #         return True
    #     else:
    #         return False
    # def categorie_nota(self):
    #     nota = self.nota_finala()
        
    #     if nota < 0 or nota > 100:
    #         raise ValueError("Nota finala invalida")
        
    #     if nota < 50:
    #         return "Picat"
    #     elif nota < 70:
    #         return "Bine"
    #     elif nota < 90:
    #         return "Foarte bine"
    #     else:
    #         return "Excelent"
