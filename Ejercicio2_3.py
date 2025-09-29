from enum import Enum
class tipoColor(Enum):
    blanco=1
    negro=2
    rojo=3
    naranja=4
    amarillo=5
    verde=6
    azul=7
    violeta=8
class tipoA(Enum):
    ciudad=1
    subcompacto=2
    compacto=3
    familiar=4
    ejecutivo=5
    suv=6
class tipoCom(Enum):
    gasolina=1
    bioetanol=2
    diesel=3
    biodiesel=4
    gas_natural=5

class Automovil:
    def __init__(self, marca, modelo, motor, tipoCom, tipoA, cantidadAsientos, cantidadPuertas, VelocidadMax, color,velActual):
        self.marca=marca
        self.modelo=modelo
        self.motor=motor
        self.tipoCom=tipoCom
        self.tipoA=tipoA
        self.cantidadAsientos=cantidadAsientos
        self.cantidadPuertas=cantidadPuertas
        self.VelocidadMax=VelocidadMax
        self.color=color    
        self.velActual=velActual


    def set_marca(self, nueva_marca):
        self.marca = nueva_marca
        print(f"La marca del automóvil ha sido actualizada a: {self.marca}")
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo
        print(f"El modelo del automóvil ha sido actualizado a: {self.modelo}")
    def set_motor(self, nuevo_motor):
        self.motor = nuevo_motor
        print(f"El motor del automóvil ha sido actualizado a: {self.motor}")
    def set_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"El color del automóvil ha sido actualizado a: {self.color.name}")
    def set_tipoCombustible(self, nuevo_tipoCom):
        self.tipoCom = nuevo_tipoCom
        print(f"El tipo de combustible del automóvil ha sido actualizado a: {self.tipoCom.name}")
    def set_tipoAutomovil(self, nuevo_tipoA):
        self.tipoA = nuevo_tipoA
        print(f"El tipo de automóvil ha sido actualizado a: {self.tipoA.name}")
    def set_cantidadAsientos(self, nueva_cantidad):
        self.cantidadAsientos = nueva_cantidad
        print(f"La cantidad de asientos del automóvil ha sido actualizada a: {self.cantidadAsientos}")
    def set_cantidadPuertas(self, nueva_cantidad):
        self.cantidadPuertas = nueva_cantidad
        print(f"La cantidad de puertas del automóvil ha sido actualizada a: {self.cantidadPuertas}")
    def set_VelocidadMax(self, nueva_velocidad):
        self.VelocidadMax = nueva_velocidad
        print(f"La velocidad máxima del automóvil ha sido actualizada a: {self.VelocidadMax} km/h")
    def set_velActual(self, nueva_velocidad):
        self.velActual = nueva_velocidad
        print(f"La velocidad actual del automóvil ha sido actualizada a: {self.velActual} km/h")
    
    
    def get_marca(self):
        return {
            'Marca': self.marca,
        }
    def get_modelo(self):
        return {
            'Modelo': self.modelo,
        }
    def get_motor(self):
        return {
            'Motor': self.motor,
        }
    def get_color(self):
        return {
            'Color': self.color.name,
        }
    def get_tipoCombustible(self):
        return {
            'Tipo de combustible': self.tipoCom.name,
        }
    def get_tipoAutomovil(self):
        return {
            'Tipo de automóvil': self.tipoA.name,
        }
    def get_cantidadAsientos(self):
        return {
            'Cantidad de asientos': self.cantidadAsientos,
        }
    def get_cantidadPuertas(self):
        return {
            'Cantidad de puertas': self.cantidadPuertas,
        }
    def get_VelocidadMax(self):
        return {
            'Velocidad máxima': self.VelocidadMax,
        }
    def get_velActual(self):
        return {
            'Velocidad actual': self.velActual,
        }
    



    def acelerar(self, incremento):
        if incremento < 0:
            return print("El incremento no puede ser negativo")
        
        if self.velActual+incremento >= self.VelocidadMax:
            self.velActual = self.velActual
            return print(f"No es posible acelerar {incremento} km/h, la velocidad actual es: {self.velActual} km/h")

        if self.velActual+incremento < self.VelocidadMax:
            self.velActual += incremento
            return print(f"Se ha acelerado {incremento} km/h, la velocidad actual es: {self.velActual} km/h")
        
    def desacelerar(self, decremento):
        if decremento <0:
            return print("El decremento no puede ser negativo")
        if self.velActual - decremento < 0:
            self.velActual = 0
            return print(f"No es posible desacelerar {decremento} km/h, la velocidad actual es: {self.velActual} km/h")
        self.velActual -= decremento
        return print(f"Se ha desacelerado {decremento} km/h, la velocidad actual es: {self.velActual} km/h")
    
    def frenar(self):
        self.velActual=0
        return print(f"El automóvil ha frenado, la velocidad actual es: {self.velActual} km/h")

    def tiempo_de_llegada(self, distancia):
        tiempo=distancia/self.velActual
        return print(f"El tiempo de llegada es: {tiempo} horas")
   
class EjercicioN23:
    if __name__ =="__main__":

        auto1=Automovil("Toyota", "Corolla", "1.8L", tipoCom.gasolina, tipoA.compacto, 5, 4, 180, tipoColor.blanco, 100)

        auto1.acelerar(20)
        auto1.tiempo_de_llegada(150)
        auto1.desacelerar(50)


        auto1.frenar()

        print(auto1.get_color())    
       
     

