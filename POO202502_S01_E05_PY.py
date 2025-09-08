import math as m

class Calculos:
    @staticmethod
    def calcular_suma(suma: float, x: float) -> float:
        return suma + x

    @staticmethod
    def calcular_x(x: float, y: float) -> float:
        return x + m.pow(y,2)

class POO202502_S01_E05:
    @staticmethod
    def main():
        
        suma = float(input("Ingrese el valor inicial de suma: "))
        x = float(input("Ingrese el valor inicial de x: "))
        y = float(input("Ingrese el valor inicial de y: "))

        
        suma = Calculos.calcular_suma(suma, x)
        x = Calculos.calcular_x(x, y)
        
        suma += x/y 

        # Mostrar resultados
        print(f"El valor de la suma es: {suma}")


# Punto de entrada, igual que public static void main en Java
if __name__ == "__main__":
    POO202502_S01_E05.main()
