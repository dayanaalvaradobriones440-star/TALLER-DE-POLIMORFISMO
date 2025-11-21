import math
from FiguraGeometrica import FiguraGeometrica
class Circunferencia(FiguraGeometrica):
    """
     Clase que representa una circunferencia
    """
    def __init__(self, radio: float):
        # En este caso usamos ancho como radio
        super().__init__(radio, radio)

    def area(self) -> float:
        return math.pi * (self.ancho ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.ancho

    def __str__(self) -> str:
        return f"Circunferencia(radio={self.ancho})"
