import math as m

class Calculos:
    @staticmethod
    def calcular_cuadrado(numero: float) -> float:
        return m.pow(numero, 2)

    @staticmethod
    def calcular_cubo(numero: float) -> float:
        return m.pow(numero, 3)

class POO202502_S01_E14:
    @staticmethod
    def main():
        
        numero = float(input("Ingrese un numero: "))
        
        cuadrado = Calculos.calcular_cuadrado(numero)
        cubo = Calculos.calcular_cubo(numero)
    
        # Mostrar resultados
        print(f"El numero ingresado fue: {numero}")
        print(f"El cuadrado del numero es: {cuadrado}")
        print(f"El cubo del numero es: {cubo}")


# Punto de entrada, igual que public static void main en Java
if __name__ == "__main__":
    POO202502_S01_E14.main()
