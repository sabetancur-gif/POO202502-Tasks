import math as m

class Calculos:
    @staticmethod
    def area_circulo(radio_c: float) -> float:
        return m.pi * m.pow(radio_c, 2)

    @staticmethod
    def perimetro_circulo(radio_c: float) -> float:
        return 2 * m.pi * radio_c

class POO202502_S01_E17:
    @staticmethod
    def main():
        
        # we read the radio of circle
        radio_c = float(input("Ingrese el radio del circulo: "))
        
        # we calculate of area and perimeter from tha Calculos class
        area_c = Calculos.area_circulo(radio_c)
        perimetro_c = Calculos.perimetro_circulo(radio_c)
    
        # we display the messages associated with the requested variables
        print(f"El radio del circulos es: {radio_c}")
        print(f"El area del circulo es: {area_c}")
        print(f"La longitud de la circuderencia es: {perimetro_c}")


# Punto de entrada, igual que public static void main en Java
if __name__ == "__main__":
    POO202502_S01_E17.main()
