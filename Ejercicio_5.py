class Calculos:
    @staticmethod
    def sumar(x,suma):
        suma=x+suma
        return suma

    @staticmethod
    def calcular_x(x1,y):
        x1=x1+y**2
        return x1
    @staticmethod
    def suma_final(x2,y,suma3):
        suma3=suma3+x2/y
        return suma3
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))
suma=Calculos.sumar(x,0)
x=Calculos.calcular_x(x,y)
print(f"El valor de la suma es: {suma}")
suma=Calculos.suma_final(x,y,suma)
print(f"El valor de la suma es: {suma}")