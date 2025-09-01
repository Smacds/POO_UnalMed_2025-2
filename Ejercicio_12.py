class Calculos:
    @staticmethod
    def salario_bruto(pago, horas):
        return pago * horas
    
    @staticmethod
    def retencion(salario_bruto, retencion):
        return salario_bruto * (retencion / 100)

    @staticmethod
    def salario_neto(salario_bruto, valor_retencion):
        return salario_bruto - valor_retencion

pago = float(input("Ingrese el pago por hora: "))
horas=float(input("Ingrese la cantidad de horas trabajadas:"))
retencion = int(input("Ingrese el porcentaje de retención: "))

salario_bruto = Calculos.salario_bruto(pago, horas)
retencion = Calculos.retencion(salario_bruto, retencion)
salario_neto = Calculos.salario_neto(salario_bruto, retencion)

print(f"El salario bruto es: {salario_bruto}")
print(f"El valor de retención es: {retencion}")
print(f"El salario neto es: {salario_neto}")