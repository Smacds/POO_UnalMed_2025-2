from math import pi
        
class Circulo:
    def __init__(self,radio):
        self.radio=radio
    
    def calcular_area(self):
        area=pi*self.radio**2
        return area
    def calcular_perimetro(self):
        perimetro=2*pi*self.radio
        return perimetro

class Cuadrado:
    def __init__(self,lado):
        self.lado=lado
    def calcular_area(self):
        area=self.lado**2
        return area
    def calcular_perimetro(self):
        perimetro=4*self.lado
        return perimetro


class Rectangulo:
    def __init__(self,largo, ancho):
        self.largo=largo
        self.ancho=ancho
    
    def calcular_area(self):
        area=self.largo*self.ancho
        return area
    def calcular_perimetro(self):
        perimetro=2*(self.largo+self.ancho)
        return perimetro

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def calcular_area(self):
        area = self.base*self.altura/2
        return area
    
    def calcular_hipotenusa(self):
        hipotenusa=(self.base**2+self.altura**2)**0.5
        return hipotenusa
    def tipo_triangulo(self):
        if self.base==self.altura:
            return "El triángulo es isósceles"
        elif self.base == self.altura and self.altura == self.calcular_hipotenusa(): #esto no es posible porque de plano se asumiío que es rectangulo
            return "El triángulo es equilátero"
        else:
            return "El triángulo es escaleno"
    def calcular_perimetro(self):
        perimetro=self.base+self.altura+(self.base**2+self.altura**2)**0.5
        return perimetro


class pruebaFiguras:
    if __name__ =="__main__":
        circulo1=Circulo(2)
        cuadrado1=Cuadrado(3)
        rectangulo1=Rectangulo(1,2)
        triangulo1=TrianguloRectangulo(5,3)

        print(f"El area del circulo es: {circulo1.calcular_area()} cm²")
        print(f"El perimetro del circulo es: {circulo1.calcular_perimetro()} cm")
        print("\n")

        print(f"El area del cuadrado es: {cuadrado1.calcular_area()} cm²")
        print(f"El perimetro del cuadrado es: {cuadrado1.calcular_perimetro()} cm")
        print("\n")

        print(f"El area del rectangulo es: {rectangulo1.calcular_area()} cm²")
        print(f"El perimetro del rectangulo es: {rectangulo1.calcular_perimetro()} cm")
        print("\n")

        print(f"El area del triangulo es: {triangulo1.calcular_area()} cm²")
        print(f"El perimetro del triangulo es: {triangulo1.calcular_perimetro()} cm")
        print(f"La hipotenusa del triangulo es: {triangulo1.calcular_hipotenusa()} cm")
        print(f"{triangulo1.tipo_triangulo()}")