import functools

def valider_positif(*indices: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for idx in indices:
                if idx < len(args):
                    value = args[idx]
                    if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
                        raise ValueError(f"L'argument à l'index {idx} doit être un nombre positif.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class Rectangle:
    @valider_positif(1, 2) # Valide largeur (index 1) et hauteur (index 2)
    def __init__(self, largeur: float, hauteur: float):
        self.largeur = largeur
        self.hauteur = hauteur

    @valider_positif(1) # Valide facteur (index 1)
    def aire(self, facteur: float = 1.0) -> float:
        return self.largeur * self.hauteur * facteur

# Test
rect = Rectangle(5, 10)
print(rect.aire()) # 50.0
try:
    rect.aire(-1)
except ValueError as e:
    print(e) # L'argument à l'index 1 doit être un nombre positif.