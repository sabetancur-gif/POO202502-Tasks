class Calculos:
    @staticmethod
    def calcular_salario_bruto(horas_lab: float, valor_hora: float) -> float:
        return horas_lab * valor_hora

    @staticmethod
    def calcular_porc_retencion(retencion: float) -> float:
        return retencion / 100
    
    @staticmethod
    def calcular_valor_retencion_fuente(retencion: float, salario_bruto: float) -> float:
        return retencion * salario_bruto
    @staticmethod
    def calcular_salario_neto(salario_bruto: float, valor_retencion_fuente: float) -> float:
        return salario_bruto - valor_retencion_fuente

class POO202502_S01_E12:
    @staticmethod
    def main():
        
        horas_lab = float(input("Ingrese la cantidad de horas trabajadas: "))
        valor_hora = float(input("Ingrese el valor de la hora: "))
        retencion = float(input("Ingrese el valor decimal de la retencion: "))
    
        salario_bruto = Calculos.calcular_salario_bruto(horas_lab, valor_hora)
        retencion = Calculos.calcular_porc_retencion(retencion)
        valor_retencion_fuente = Calculos.calcular_valor_retencion_fuente(retencion, salario_bruto)
        salario_neto = Calculos.calcular_salario_neto(salario_bruto, valor_retencion_fuente)
    
        # Mostrar resultados
        print(f"El salario bruto es: {salario_bruto}")
        print(f"El saldo retenido en la fuente es: {valor_retencion_fuente}")
        print(f"El salario neto es: {salario_neto}")


# Punto de entrada, igual que public static void main en Java
if __name__ == "__main__":
    POO202502_S01_E12.main()
