from math import pi

class circulo():
    @staticmethod
    def area(radio):
        area=pi*radio**2
        return area
    @staticmethod
    def circunferencia(radio):
        longitud=2*pi*radio
        return longitud
    
radio= float(input("Ingrese el valor del radio: "))
area = circulo.area(radio)
longitud = circulo.circunferencia(radio)

print(f"El area del circulo es: {area}")
print(f"La longitud de la circunferencia es: {longitud}")