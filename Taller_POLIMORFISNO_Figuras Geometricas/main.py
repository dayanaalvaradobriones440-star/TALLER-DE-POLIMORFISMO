from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

def sumar_areas(figuras: list) -> float:
    return sum(figura.area() for figura in figuras)

def sumar_perimetros(figuras: list) -> float:
    return sum(figura.perimetro() for figura in figuras)

if __name__ == "__main__":
    c1 = Cuadrado(5)
    c2 = Cuadrado(10)
    r1 = Rectangulo(4, 6)
    r2 = Rectangulo(3, 8)

    figuras = [c1, c2, r1, r2]
    for f in figuras:
        print(f"{f} -> Área: {f.area():.2f}, Perímetro: {f.perimetro():.2f}")
    try:
        c_invalido = Cuadrado(-3)
    except ValueError as e:
        print("Error al crear cuadrado:", e)

    print("\nSuma de áreas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))
