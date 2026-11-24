class Vecteur2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, autre: 'Vecteur2D') -> 'Vecteur2D':
        return Vecteur2D(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre: 'Vecteur2D') -> 'Vecteur2D':
        return Vecteur2D(self.x - autre.x, self.y - autre.y)

    def __mul__(self, scalaire: float) -> 'Vecteur2D':
        return Vecteur2D(self.x * scalaire, self.y * scalaire)

    def __eq__(self, autre: object) -> bool:
        if not isinstance(autre, Vecteur2D):
            return False
        return self.x == autre.x and self.y == autre.y

    def __repr__(self) -> str:
        return f"Vecteur2D({self.x}, {self.y})"

# Test
v1 = Vecteur2D(1, 2)
v2 = Vecteur2D(3, 4)
print(v1 + v2)                 # Vecteur2D(4, 6)
print(v2 - v1)                 # Vecteur2D(2, 2)
print(v1 * 2)                  # Vecteur2D(2, 4)
print(v1 == Vecteur2D(1, 2))   # True