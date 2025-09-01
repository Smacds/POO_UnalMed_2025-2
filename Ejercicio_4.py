class edades():
    @staticmethod
    def alberto_edad(juan):
        alberto=juan*2/3
        return alberto
    @staticmethod
    def ana_edad(juan):
        ana=juan*4/3
        return ana
    @staticmethod
    def mama_edad(juan, ana, alberto):
        mama= juan + ana + alberto
        return mama
    
juan = int(input("Ingrese la edad de Juan: "))
alberto = int(edades.alberto_edad(juan))
ana= int(edades.ana_edad(juan))
mama= int(edades.mama_edad(juan,ana,alberto))

print(f"La edad de Juan es: {juan} años")
print(f"La edad de Alberto es: {alberto} años")
print(f"La edad de Ana es: {ana} años")
print(f"La edad de la Mamá es: {mama} años")