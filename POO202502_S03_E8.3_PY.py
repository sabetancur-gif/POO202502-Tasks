"""
figuras_gui.py

Equivalente en Python (tkinter) de las clases Java:
- FiguraGeometrica (base)
- Cilindro
- Esfera
- Piramide (pirámide cuadrada)
y ventanas:
- VentanaPrincipal (elige figura)
- VentanaCilindro
- VentanaEsfera
- VentanaPiramide

Cómo usar:
    python figuras_gui.py
"""
import tkinter as tk
from tkinter import messagebox
import math


# =========================
# Modelo: figuras geométricas
# =========================
class FiguraGeometrica:
    """Clase base. Guarda volumen y superficie."""
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def set_volumen(self, v):
        """  """
        self.volumen = v

    def set_superficie(self, s):
        """  """
        self.superficie = s


class Cilindro(FiguraGeometrica):
    """Cilindro definido por radio y altura."""
    def __init__(self, radio: float, altura: float):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        """  """
        # V = pi * r^2 * h
        return math.pi * (self.radio ** 2) * self.altura

    def calcular_superficie(self):
        """  """
        # Superficie total = 2*pi*r*(r + h)
        return 2 * math.pi * self.radio * (self.radio + self.altura)


class Esfera(FiguraGeometrica):
    """Esfera definida por radio."""
    def __init__(self, radio: float):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        """  """
        # V = 4/3 * pi * r^3
        return (4.0 / 3.0) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        """  """
        # Superficie = 4 * pi * r^2
        return 4 * math.pi * (self.radio ** 2)


class Piramide(FiguraGeometrica):
    """Pirámide cuadrada definida por base (lado de la base), altura y apotema.
       Volumen = base^2 * altura / 3
       Superficie total = base^2 + area lateral
       Area lateral (pirámide cuadrada) = 2 * base * apotema
    """
    def __init__(self, base: float, altura: float, apotema: float):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        """ P """
        return (self.base ** 2) * self.altura / 3.0

    def calcular_superficie(self):
        """ P """
        # Base^2 + lateral
        area_lateral = 2.0 * self.base * self.apotema
        return (self.base ** 2) + area_lateral


# =========================
# Vistas: ventanas con tkinter
# =========================
class VentanaCilindro(tk.Toplevel):
    """  """
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("320x220")
        self.resizable(False, False)
        self._crear_componentes()

    def _crear_componentes(self):
        tk.Label(self, text="Radio (cm):").place(x=20, y=20)
        self.entrada_radio = tk.Entry(self)
        self.entrada_radio.place(x=120, y=20, width=160)

        tk.Label(self, text="Altura (cm):").place(x=20, y=60)
        self.entrada_altura = tk.Entry(self)
        self.entrada_altura.place(x=120, y=60, width=160)

        btn_calcular = tk.Button(self, text="Calcular", command=self._calcular)
        btn_calcular.place(x=20, y=100, width=100)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self._limpiar)
        btn_limpiar.place(x=130, y=100, width=100)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm³): ")
        self.lbl_volumen.place(x=20, y=140)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm²): ")
        self.lbl_superficie.place(x=20, y=170)

    def _validar_float(self, texto, nombre):
        try:
            val = float(texto)
            if val < 0:
                raise ValueError("negativo")
            return val
        except (ValueError, TypeError) as exc:
            raise ValueError(
                f"Entrada inválida para {nombre}."
                "Debe ser un número no negativo."
            ) from exc

    def _calcular(self):
        try:
            r = self._validar_float(self.entrada_radio.get().strip(), "radio")
            h = self._validar_float(
                self.entrada_altura.get().strip(),
                "altura"
            )
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        cil = Cilindro(r, h)
        self.lbl_volumen.config(text=f"Volumen (cm³): {cil.volumen:.2f}")
        self.lbl_superficie.config(
            text=f"Superficie (cm²): {cil.superficie:.2f}"
        )

    def _limpiar(self):
        self.entrada_radio.delete(0, tk.END)
        self.entrada_altura.delete(0, tk.END)
        self.lbl_volumen.config(text="Volumen (cm³): ")
        self.lbl_superficie.config(text="Superficie (cm²): ")


class VentanaEsfera(tk.Toplevel):
    """  """
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("320x180")
        self.resizable(False, False)
        self._crear_componentes()

    def _crear_componentes(self):
        tk.Label(self, text="Radio (cm):").place(x=20, y=20)
        self.entrada_radio = tk.Entry(self)
        self.entrada_radio.place(x=120, y=20, width=160)

        btn_calcular = tk.Button(self, text="Calcular", command=self._calcular)
        btn_calcular.place(x=20, y=60, width=100)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self._limpiar)
        btn_limpiar.place(x=130, y=60, width=100)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm³): ")
        self.lbl_volumen.place(x=20, y=100)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm²): ")
        self.lbl_superficie.place(x=20, y=130)

    def _validar_float(self, texto, nombre):
        try:
            val = float(texto)
            if val < 0:
                raise ValueError("negativo")
            return val
        except (ValueError, TypeError) as exc:
            raise ValueError(
                f"Entrada inválida para {nombre}."
                "Debe ser un número no negativo."
            ) from exc

    def _calcular(self):
        try:
            r = self._validar_float(self.entrada_radio.get().strip(), "radio")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        esf = Esfera(r)
        self.lbl_volumen.config(text=f"Volumen (cm³): {esf.volumen:.2f}")
        self.lbl_superficie.config(
            text=f"Superficie (cm²): {esf.superficie:.2f}"
        )

    def _limpiar(self):
        self.entrada_radio.delete(0, tk.END)
        self.lbl_volumen.config(text="Volumen (cm³): ")
        self.lbl_superficie.config(text="Superficie (cm²): ")


class VentanaPiramide(tk.Toplevel):
    """  """
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide (cuadrada)")
        self.geometry("360x240")
        self.resizable(False, False)
        self._crear_componentes()

    def _crear_componentes(self):
        tk.Label(self, text="Base (lado en cm):").place(x=20, y=20)
        self.entrada_base = tk.Entry(self)
        self.entrada_base.place(x=160, y=20, width=160)

        tk.Label(self, text="Altura (cm):").place(x=20, y=60)
        self.entrada_altura = tk.Entry(self)
        self.entrada_altura.place(x=160, y=60, width=160)

        tk.Label(self, text="Apotema (cm):").place(x=20, y=100)
        self.entrada_apotema = tk.Entry(self)
        self.entrada_apotema.place(x=160, y=100, width=160)

        btn_calcular = tk.Button(self, text="Calcular", command=self._calcular)
        btn_calcular.place(x=20, y=140, width=100)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self._limpiar)
        btn_limpiar.place(x=130, y=140, width=100)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm³): ")
        self.lbl_volumen.place(x=20, y=180)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm²): ")
        self.lbl_superficie.place(x=20, y=210)

    def _validar_float(self, texto, nombre):
        try:
            val = float(texto)
            if val < 0:
                raise ValueError("negativo")
            return val
        except (ValueError, TypeError) as exc:
            raise ValueError(
                f"Entrada inválida para {nombre}."
                "Debe ser un número no negativo."
            ) from exc

    def _calcular(self):
        try:
            base = self._validar_float(self.entrada_base.get().strip(), "base")
            altura = self._validar_float(
                self.entrada_altura.get().strip(), "altura"
            )
            apotema = self._validar_float(
                self.entrada_apotema.get().strip(), "apotema"
            )
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        pir = Piramide(base, altura, apotema)
        self.lbl_volumen.config(text=f"Volumen (cm³): {pir.volumen:.2f}")
        self.lbl_superficie.config(
            text=f"Superficie (cm²): {pir.superficie:.2f}"
        )

    def _limpiar(self):
        self.entrada_base.delete(0, tk.END)
        self.entrada_altura.delete(0, tk.END)
        self.entrada_apotema.delete(0, tk.END)
        self.lbl_volumen.config(text="Volumen (cm³): ")
        self.lbl_superficie.config(text="Superficie (cm²): ")


class VentanaPrincipal(tk.Tk):
    """  """
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("260x200")
        self.resizable(False, False)
        self._crear_componentes()

    def _crear_componentes(self):
        lbl = tk.Label(self, text="Seleccione una figura:")
        lbl.place(x=20, y=20)

        btn_cilindro = tk.Button(
            self, text="Cilindro",
            command=self._abrir_cilindro
        )
        btn_cilindro.place(x=20, y=60, width=100)

        btn_esfera = tk.Button(self, text="Esfera", command=self._abrir_esfera)
        btn_esfera.place(x=130, y=60, width=100)

        btn_piramide = tk.Button(
            self, text="Pirámide", command=self._abrir_piramide
        )
        btn_piramide.place(x=20, y=100, width=210)

    def _abrir_cilindro(self):
        VentanaCilindro(self)

    def _abrir_esfera(self):
        VentanaEsfera(self)

    def _abrir_piramide(self):
        VentanaPiramide(self)


# =========================
# Main
# =========================
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
