# Exercice Tableau
"""
class Appareil:
    def __init__(self, nom, couleur):
        self._nom = nom
        self._couleur = couleur
        self.__patate = "Patate"

    def bruit(self):
        print("zzzz")


class Ordinateur(Appareil):
    def __init__(self, type, nom, couleur):
        super().__init__(nom, couleur)
        self._type = type

    def bruit(self):
        print("Faites du bruit!")


pc = Ordinateur("Linux", "Henri le PC", "noir")
pc.bruit()
"""


# Exercice de Héritage et polymorphisme dans le read me
class Instrument:
    def __init__(self, categorie, taille):
        self._categorie = categorie
        self._taille = taille

    def bruit(self):
        print("ding")

    def inventeur(self):
        print("Leonardo DiCaprio")


class Piano(Instrument):
    def __init__(self, categorie, taille, couleur):
        super().__init__(categorie, taille)
        self.__couleur = couleur

    def inventeur(self):
        print("Bartolomeo Cristofori")

    def rush_e(self):
        print("palalalalala boom!")


class Guitare(Instrument):
    def __init__(self, categorie, taille, nombrecordes):
        super().__init__(categorie, taille)
        self.__nombrecordes = nombrecordes

    def bruit(self):
        print("diling diling diling")

    def legende(self):
        print("Carlos Santana")


piano = Piano("vent", "grand", "blanc et noir")
piano.rush_e()
piano.inventeur()

guitare = Guitare("corde", "moyen", "6")
guitare.bruit()
guitare.legende()
