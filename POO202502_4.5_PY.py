"""Solución al quinto punto de la actividad N°4 de POO_2025_02."""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import traceback


class FileReaderApp:
    """ P """
    def __init__(self, master=None):
        self.master = master or tk.Tk()
        self.master.title("Lector de archivos - Interactivo (POO)")
        self.master.geometry("760x520")

        lbl_info = tk.Label(
            self.master,
            text=(
                "Seleccione un archivo o "
                "escriba la ruta y pulse 'Leer archivo'."),
            font=("Arial", 12))
        lbl_info.pack(pady=(10, 6))

        # Frame para entrada y botones
        frame_ruta = tk.Frame(self.master)
        frame_ruta.pack(padx=10, fill="x")

        # Entry y botones con grid
        self.entry_ruta = tk.Entry(frame_ruta, font=("Consolas", 11))
        self.entry_ruta.grid(row=0, column=0, sticky="ew", padx=(0, 6), pady=6)

        btn_browse = tk.Button(
            frame_ruta, text="Seleccionar...",
            command=self.seleccionar_archivo, width=12)
        btn_browse.grid(row=0, column=1, padx=(0, 6))

        btn_leer = tk.Button(
            frame_ruta, text="Leer archivo",
            command=self.leer_archivo, width=12)
        btn_leer.grid(row=0, column=2, padx=(0, 6))

        btn_limpiar = tk.Button(
            frame_ruta, text="Limpiar",
            command=self.limpiar, width=10)
        btn_limpiar.grid(row=0, column=3)

        frame_ruta.columnconfigure(0, weight=1)

        # Área de salida
        self.salida = scrolledtext.ScrolledText(
            self.master, width=95, height=28, font=("Consolas", 11))
        self.salida.pack(padx=10, pady=(6, 10), fill="both", expand=True)

    # --- Utilidades ---
    def seleccionar_archivo(self):
        """ P """
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if ruta:
            self.entry_ruta.delete(0, tk.END)
            self.entry_ruta.insert(0, ruta)

    def mostrar(self, msg):
        """Inserta línea en el área de salida y hace scroll al final."""
        self.salida.insert(tk.END, msg + "\n")
        self.salida.see(tk.END)

    # --- Lógica principal ---
    def leer_archivo(self):
        """Intenta leer el archivo con utf-8; si falla
        por decodificación, intenta latin-1."""
        self.salida.delete(1.0, tk.END)
        ruta = self.entry_ruta.get().strip()
        if not ruta:
            msg = ("Error: debe indicar la "
                   "ruta del archivo (o seleccionar uno).")
            self.mostrar(msg)
            messagebox.showerror("Ruta vacía", msg)
            return

        archivo = None
        try:
            self.mostrar(f"Intentando abrir el archivo: {ruta}")
            archivo = open(ruta, "r", encoding="utf-8")
            self.mostrar(
                "Archivo abierto correctamente (utf-8). "
                "Leyendo contenido...\n")
            for linea in archivo:
                self.salida.insert(tk.END, linea)
            messagebox.showinfo(
                "Lectura completada",
                "El archivo se leyó correctamente.")
        except FileNotFoundError as e:
            msg = (
                f"{type(e).__name__}: "
                "No se encontró el archivo.\nDetalle: {e}")
            self.mostrar(msg)
            messagebox.showerror("Archivo no encontrado", msg)
        except PermissionError as e:
            msg = (f"{type(e).__name__}: Permiso denegado "
                   "al leer el archivo.\nDetalle: {e}")
            self.mostrar(msg)
            messagebox.showerror("Permiso denegado", msg)
        except UnicodeDecodeError as e:
            self.mostrar(
                f"{type(e).__name__}: error de decodificación "
                "(utf-8). Intentando latin-1...\nDetalle: {e}\n")
            try:
                if archivo:
                    archivo.close()
                archivo = open(ruta, "r", encoding="latin-1")
                self.mostrar(
                    "Archivo abierto con latin-1. Leyendo contenido...\n")
                for linea in archivo:
                    self.salida.insert(tk.END, linea)
                messagebox.showinfo(
                    "Lectura completada (latin-1)",
                    "El archivo se leyó correctamente con latin-1.")
            except Exception as e2:  # pylint: disable=broad-except
                msg = (
                    f"{type(e2).__name__}: No se pudo leer "
                    "el archivo con latin-1.\nDetalle: {e2}")
                self.mostrar(msg)
                messagebox.showerror("Error lectura", msg)
        except Exception as e:  # pylint: disable=broad-except
            tb = traceback.format_exc(limit=1)
            msg = f"{type(e).__name__}: {e}\n{tb}"
            self.mostrar(msg)
            messagebox.showerror("Excepción", msg)
        finally:
            try:
                if archivo and not archivo.closed:
                    archivo.close()
                    self.mostrar(
                        "\nIngresando al finally: "
                        "archivo cerrado correctamente.")
                else:
                    self.mostrar(
                        "\nIngresando al finally: no había archivo abierto.")
            except Exception as e_close:  # pylint: disable=broad-except
                self.mostrar(
                    "Ingresando al finally: fallo al cerrar "
                    f"archivo -> {type(e_close).__name__}: {e_close}")

    def limpiar(self):
        """ P """
        self.entry_ruta.delete(0, tk.END)
        self.salida.delete(1.0, tk.END)

    def run(self):
        """ P """
        self.master.mainloop()


if __name__ == "__main__":
    app = FileReaderApp()
    app.run()
