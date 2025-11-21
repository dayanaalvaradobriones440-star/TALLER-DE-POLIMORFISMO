from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):
    """
    Clase que representa un cuadrado.
    """

    def __init__(self, lado: float):
        super().__init__(lado, lado)

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        return 4 * self.ancho

    def __str__(self) -> str:
        return f"Cuadrado(lado={self.ancho})"



