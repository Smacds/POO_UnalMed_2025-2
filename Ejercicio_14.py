class Calculos:
    @staticmethod
    def calcular_cuadrado(b):
        return(b**2)

    @staticmethod
    def calcular_cubo(b):
        return(b**3)

a = float(input("Ingrese un número: "))
cuadrado=Calculos.calcular_cuadrado(a)
cubo=Calculos.calcular_cubo(a)
print(f"El cuadrado de {a} es {cuadrado}")
print(f"El cubo de {a} es {cubo}")