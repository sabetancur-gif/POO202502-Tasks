""" P """

import tkinter as tk
from tkinter import messagebox
import math


class Notas:
    """Clase que representa una lista de 5 notas y métodos estadísticos."""
    def __init__(self):
        # Inicializa con cinco ceros
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        """Retorna el promedio (media) de las notas."""
        if len(self.lista_notas) == 0:
            return 0.0
        suma = 0.0
        for i in range(len(self.lista_notas)):
            suma += self.lista_notas[i]
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        """Retorna la desviación estándar poblacional."""
        n = len(self.lista_notas)
        if n == 0:
            return 0.0
        prom = self.calcular_promedio()
        suma = 0.0
        for x in self.lista_notas:
            suma += (x - prom) ** 2
        return math.sqrt(suma / n)

    def calcular_menor(self):
        """Retorna la nota mínima."""
        if not self.lista_notas:
            return 0.0
        menor = self.lista_notas[0]
        for x in self.lista_notas:
            if x < menor:
                menor = x
        return menor

    def calcular_mayor(self):
        """Retorna la nota máxima."""
        if not self.lista_notas:
            return 0.0
        mayor = self.lista_notas[0]
        for x in self.lista_notas:
            if x > mayor:
                mayor = x
        return mayor


class VentanaPrincipal(tk.Tk):
    """Interfaz gráfica equivalente a la VentanaPrincipal en Java."""
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.notas = Notas()
        self._crear_componentes()

    def _crear_componentes(self):
        # Labels y campos de entrada para 5 notas
        self.campos = []
        for i in range(5):
            lbl = tk.Label(self, text=f"Nota {i+1}:")
            lbl.place(x=20, y=20 + 30*i, width=80, height=23)
            entrada = tk.Entry(self)
            entrada.place(x=105, y=20 + 30*i, width=135, height=23)
            self.campos.append(entrada)

        # Botones
        btn_calcular = tk.Button(
            self,
            text="Calcular",
            command=self._on_calcular
        )
        btn_calcular.place(x=20, y=170, width=100, height=23)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self._on_limpiar)
        btn_limpiar.place(x=125, y=170, width=80, height=23)

        # Labels de resultados
        self.lbl_promedio = tk.Label(self, text="Promedio = ")
        self.lbl_promedio.place(x=20, y=210, width=240, height=23)

        self.lbl_desviacion = tk.Label(self, text="Desviación estándar = ")
        self.lbl_desviacion.place(x=20, y=240, width=240, height=23)

        self.lbl_mayor = tk.Label(self, text="Valor mayor = ")
        self.lbl_mayor.place(x=20, y=270, width=240, height=23)

        self.lbl_menor = tk.Label(self, text="Valor menor = ")
        self.lbl_menor.place(x=20, y=300, width=240, height=23)

    def _on_calcular(self):
        # Lee y valida entradas
        try:
            for i, campo in enumerate(self.campos):
                texto = campo.get().strip()
                if texto == "":
                    raise ValueError(f"Falta la nota {i+1}")
                valor = float(texto)
                self.notas.lista_notas[i] = valor
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
            return

        # Calcula y muestra (formateado a 2 decimales)
        prom = self.notas.calcular_promedio()
        desv = self.notas.calcular_desviacion()
        mayor = self.notas.calcular_mayor()
        menor = self.notas.calcular_menor()

        self.lbl_promedio.config(text=f"Promedio = {prom:.2f}")
        self.lbl_desviacion.config(text=f"Desviación estándar = {desv:.2f}")
        self.lbl_mayor.config(text=f"Valor mayor = {mayor}")
        self.lbl_menor.config(text=f"Valor menor = {menor}")

    def _on_limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        # Opcional: limpiar resultados y resetear lista de notas
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación estándar = ")
        self.lbl_mayor.config(text="Valor mayor = ")
        self.lbl_menor.config(text="Valor menor = ")
        self.notas = Notas()


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
