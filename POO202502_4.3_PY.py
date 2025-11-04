"""Solución al tercer punto de la actividad N°4 de POO_2025_02."""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import math


class NumericApp:
    """ P """
    def __init__(self, master=None):
        self.master = master or tk.Tk()
        self.master.title("Cálculos numéricos - Interactivo (POO)")
        self.master.geometry("560x420")

        lbl = tk.Label(
            self.master,
            text="Ingrese un valor numérico:",
            font=("Arial", 12)
        )
        lbl.pack(pady=(12, 4))

        self.entry_valor = tk.Entry(self.master, font=("Arial", 12), width=20)
        self.entry_valor.pack()

        frame_botones = tk.Frame(self.master)
        frame_botones.pack(pady=10)

        btn_ln = tk.Button(
            frame_botones,
            text="Calcular ln (logaritmo neperiano)",
            command=self.calcular_logaritmo_neperiano
        )
        btn_ln.grid(row=0, column=0, padx=6, pady=6)

        btn_sqrt = tk.Button(frame_botones, text="Calcular raíz cuadrada",
                             command=self.calcular_raiz_cuadrada)
        btn_sqrt.grid(row=0, column=1, padx=6, pady=6)

        btn_ambos = tk.Button(
            frame_botones,
            text="Calcular ambos",
            command=self.calcular_ambos
        )
        btn_ambos.grid(row=1, column=0, padx=6, pady=6, columnspan=1)

        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar
        )
        btn_limpiar.grid(row=1, column=1, padx=6, pady=6)

        self.salida = scrolledtext.ScrolledText(
            self.master,
            width=70,
            height=12,
            font=("Consolas", 10)
        )
        self.salida.pack(pady=8)

    # --- Lógica reutilizable ---
    def obtener_valor(self):
        """Lee el texto del entry y devuelve (valor_float, None)
        o (None, excepcion)."""
        s = self.entry_valor.get().strip()
        if s == "":
            return None, ValueError("Entrada vacía")
        # permitir coma decimal
        s = s.replace(",", ".")
        try:
            v = float(s)
            return v, None
        except Exception as e:  # pylint: disable=broad-except
            return None, e

    def mostrar(self, msg):
        """Inserta una línea en el scrolledtext y
        se asegura de hacer scroll al final."""
        self.salida.insert(tk.END, msg + "\n")
        self.salida.see(tk.END)

    # --- Operaciones ---
    def calcular_logaritmo_neperiano(self):
        """ P """
        self.salida.delete(1.0, tk.END)  # limpiar salida para este cálculo
        valor, err = self.obtener_valor()
        if err:
            msg = (f"Input error ({type(err).__name__}): El valor "
                   "debe ser numérico para calcular el logaritmo.")
            self.mostrar(msg)
            messagebox.showerror("Error de entrada", msg)
            return

        try:
            # En matemática ln está definido solo para valores > 0
            if valor <= 0:
                raise ArithmeticError(
                    (
                        "El valor debe ser un número positivo "
                        "(mayor que 0) para calcular ln."
                    )
                )
            resultado = math.log(valor)
            self.mostrar(f"Resultado ln({valor}) = {resultado}")
        except ArithmeticError as e:
            msg = f"ArithmeticError: {e}"
            self.mostrar(msg)
            messagebox.showerror("Error aritmético", msg)
        except Exception as e:  # pylint: disable=broad-except
            msg = f"{type(e).__name__}: {e}"
            self.mostrar(msg)
            messagebox.showerror("Excepción", msg)
        finally:
            self.mostrar("Ingresando al finally del logaritmo\n")

    def calcular_raiz_cuadrada(self):
        """ P """
        self.salida.delete(1.0, tk.END)  # limpiar salida para este cálculo
        valor, err = self.obtener_valor()
        if err:
            msg = (f"Input error ({type(err).__name__}): El valor debe "
                   "ser numérico para calcular la raíz cuadrada.")
            self.mostrar(msg)
            messagebox.showerror("Error de entrada", msg)
            return

        try:
            if valor < 0:
                raise ArithmeticError(
                    (
                        "El valor debe ser un número positivo (>= 0) "
                        "para calcular la raíz cuadrada."
                    )
                )
            resultado = math.sqrt(valor)
            self.mostrar(f"Resultado sqrt({valor}) = {resultado}")
        except ArithmeticError as e:
            msg = f"ArithmeticError: {e}"
            self.mostrar(msg)
            messagebox.showerror("Error aritmético", msg)
        except Exception as e:  # pylint: disable=broad-except
            msg = f"{type(e).__name__}: {e}"
            self.mostrar(msg)
            messagebox.showerror("Excepción", msg)
        finally:
            self.mostrar("Ingresando al finally de la raíz cuadrada\n")

    def calcular_ambos(self):
        """ P """
        valor, err = self.obtener_valor()
        if err:
            msg = (f"Input error ({type(err).__name__}): "
                   "El valor debe ser numérico.")
            self.mostrar(msg)
            messagebox.showerror("Error de entrada", msg)
            return

        # Intentamos logaritmo
        try:
            if valor <= 0:
                raise ArithmeticError(
                    (
                        "El valor debe ser un número positivo "
                        "(mayor que 0) para calcular ln."
                    )
                )
            resultado_ln = math.log(valor)
            self.mostrar(f"Resultado ln({valor}) = {resultado_ln}")
        except Exception as e:  # pylint: disable=broad-except
            self.mostrar(f"Excepción en ln -> {type(e).__name__}: {e}")

        self.mostrar("Ingresando al finally del logaritmo")

        # Intentamos raíz
        try:
            if valor < 0:
                raise ArithmeticError(
                    (
                        "El valor debe ser un número positivo (>= 0) "
                        "para calcular la raíz cuadrada."
                    )
                )
            resultado_sqrt = math.sqrt(valor)
            self.mostrar(f"Resultado sqrt({valor}) = {resultado_sqrt}")
        except Exception as e:  # pylint: disable=broad-except
            self.mostrar(f"Excepción en sqrt -> {type(e).__name__}: {e}")

        self.mostrar("Ingresando al finally de la raíz cuadrada\n")

    def limpiar(self):
        """ P """
        self.salida.delete(1.0, tk.END)
        self.entry_valor.delete(0, tk.END)

    def run(self):
        """ P """
        self.master.mainloop()


if __name__ == "__main__":
    app = NumericApp()
    app.run()
