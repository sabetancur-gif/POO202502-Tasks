"""Solución al primer punto de la actividad N°4 de POO_2025_02."""

import tkinter as tk
from tkinter import scrolledtext, messagebox


class ExceptionApp:
    """ P """
    def __init__(self, master=None):
        self.master = master or tk.Tk()
        self.master.title("Manejo de Excepciones - Interactivo (POO)")
        self.master.geometry("520x500")

        titulo = tk.Label(
            self.master,
            text="Simulación de excepciones con entrada de usuario",
            font=("Arial", 13, "bold")
        )
        titulo.pack(pady=10)

        # --- Bloque 1 ---
        frame1 = tk.LabelFrame(
            self.master,
            text="Bloque 1: División",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )
        frame1.pack(padx=10, pady=10, fill="x")

        tk.Label(
            frame1,
            text="Ingrese un número divisor (ej. 0 lanza excepción):",
            font=("Arial", 10)
        ).pack(anchor="w")
        self.entrada1 = tk.Entry(frame1, width=20)
        self.entrada1.pack(pady=5)
        tk.Button(
            frame1,
            text="Ejecutar bloque 1",
            command=self.ejecutar_bloque1,
            font=("Arial", 10)
        ).pack(pady=5)

        # --- Bloque 2 ---
        frame2 = tk.LabelFrame(
            self.master,
            text="Bloque 2: Objeto nulo",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )
        frame2.pack(padx=10, pady=10, fill="x")

        tk.Label(
            frame2,
            text=("Ingrese texto (deje vacío o escriba "
                  "'None' para simular excepción):"),
            font=("Arial", 10)
        ).pack(anchor="w")
        self.entrada2 = tk.Entry(frame2, width=20)
        self.entrada2.pack(pady=5)
        tk.Button(
            frame2,
            text="Ejecutar bloque 2",
            command=self.ejecutar_bloque2,
            font=("Arial", 10)
        ).pack(pady=5)

        # --- Área de salida ---
        self.salida = scrolledtext.ScrolledText(
            self.master,
            width=60,
            height=12,
            font=("Consolas", 10)
        )
        self.salida.pack(pady=10)

    def _log(self, text):
        """Agrega texto al área de salida."""
        self.salida.insert(tk.END, text + "\n")
        self.salida.see(tk.END)

    def ejecutar_bloque1(self):
        """ P """
        self.salida.delete(1.0, tk.END)
        try:
            self._log("Ingresando al primer try")
            valor = float(self.entrada1.get())
            cociente = 10000 / valor
            self._log(f"Resultado de la división: {cociente}")
        except ZeroDivisionError:
            msg = "División por cero"
            self._log(msg)
            messagebox.showwarning("Advertencia", msg)
        except ValueError:
            msg = "Error: debes ingresar un número válido"
            self._log(msg)
            messagebox.showwarning("Advertencia", msg)
        finally:
            self._log("Ingresando al primer finally\n")

    def ejecutar_bloque2(self):
        """ P """
        self.salida.delete(1.0, tk.END)
        try:
            self._log("Ingresando al segundo try")
            texto = self.entrada2.get()
            if texto.strip() == "" or texto.lower() == "none":
                objeto = None
            else:
                objeto = texto

            # Simula error como en Java si el objeto es None
            if objeto is None:
                resultado = objeto.toString()  # Provoca AttributeError
            else:
                resultado = str(objeto)

            self._log(f"Objeto convertido a string: {resultado}")
        except AttributeError:
            msg = ("Ocurrió una excepción: el objeto es None "
                   "o no tiene el método solicitado")
            self._log(msg)
            messagebox.showwarning("Advertencia", msg)
        except Exception as e:  # pylint: disable=broad-except
            msg = f"Ocurrió una excepción: {type(e).__name__}"
            self._log(msg)
            messagebox.showwarning("Advertencia", msg)
        finally:
            self._log("Ingresando al segundo finally\n")

    def run(self):
        """ P """
        self.master.mainloop()


if __name__ == "__main__":
    app = ExceptionApp()
    app.run()
