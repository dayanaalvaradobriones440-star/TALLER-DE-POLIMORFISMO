class FiguraGeometrica:
    """
    Clase base que representa figuras geométricas.
    """

    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor: float):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor: float):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(ancho={self.ancho}, alto={self.alto})"
