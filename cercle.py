import math

class Cercle:
    def __init__(self, rayon: float):
        self.rayon = rayon

    @property
    def rayon(self) -> float:
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        if valeur <= 0:
            raise ValueError("Le rayon doit être strictement positif.")
        self._rayon = valeur

    def aire(self) -> float:
        return math.pi * self.rayon ** 2

    def perimetre(self) -> float:
        return 2 * math.pi * self.rayon

    def __str__(self) -> str:
        return f"Cercle(rayon={self.rayon})"

# Test
c = Cercle(5.0)
print(c.aire())      # 78.53981633974483
print(c.perimetre()) # 31.41592653589793
try:
    c.rayon = -10
except ValueError as e:
    print(f"Erreur interceptée : {e}")