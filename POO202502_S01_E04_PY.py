class Calculos:
    @staticmethod
    def calcular_edalber(edjuan: float) -> float:
        return 2 * (edjuan / 3)

    @staticmethod
    def calcular_edana(edjuan: float) -> float:
        return 4 * (edjuan / 3)

    @staticmethod
    def calcular_edmama(edjuan: float, edalber: float, edana:float) -> float:
        return edjuan + edalber + edana


class POO202502_S01_E04:
    @staticmethod
    def main():
        # read the Juan is age
        edjuan = float(input("Ingrese la edad de Juan: "))

        # calculates the other ages from the Calculos class
        edalber = Calculos.calcular_edalber(edjuan)
        edana = Calculos.calcular_edana(edjuan)
        edmama = Calculos.calcular_edmama(edjuan, edalber, edana)

        # we display the messages with the respective ages
        print("¡Edades de los cuatro integrantes!")
        print(f"Juan: {edjuan}")
        print(f"Alberto: {edalber}")
        print(f"Ana: {edana}")
        print(f"Mamá: {edmama}")

if __name__ == "__main__":
    POO202502_S01_E04.main()
