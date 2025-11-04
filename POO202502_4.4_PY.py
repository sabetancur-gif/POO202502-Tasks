#Ejercicio 4 Actividad 4

import tkinter as tk
from tkinter import messagebox

COLOR_PRINCIPAL = "#ff6a13"
COLOR_FONDO = "#f9f9f9"
COLOR_TEXTO = "#333333"
COLOR_BOTON = "#ff6a13"
COLOR_BOTON_TEXTO = "#ffffff"

class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []

    def esta_lleno(self):
        return len(self.programadores) >= 3

    def añadir_programador(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se puede agregar más programadores.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo):
        if any(char.isdigit() for char in campo):
            raise Exception("El campo no puede contener dígitos.")
        if len(campo) > 20:
            raise Exception("El campo no puede tener más de 20 caracteres.")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Equipo de Maratón")
        self.root.configure(bg=COLOR_FONDO)
        self.equipo = None
        self.programador_count = 0

        # Estilo común
        label_opts = {"bg": COLOR_FONDO, "fg": COLOR_TEXTO, "font": ("Arial", 10)}
        entry_opts = {"bg": "#ffffff", "fg": COLOR_TEXTO, "font": ("Arial", 10)}

        # Datos del equipo
        tk.Label(root, text="Nombre del equipo", **label_opts).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.nombre_equipo_entry = tk.Entry(root, **entry_opts)
        self.nombre_equipo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Universidad", **label_opts).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.universidad_entry = tk.Entry(root, **entry_opts)
        self.universidad_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Lenguaje de programación", **label_opts).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.lenguaje_entry = tk.Entry(root, **entry_opts)
        self.lenguaje_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(root, text="Crear equipo", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.crear_equipo).grid(row=3, columnspan=2, pady=10)

        # Datos de programadores
        tk.Label(root, text="Nombre del programador", **label_opts).grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.nombre_prog_entry = tk.Entry(root, **entry_opts)
        self.nombre_prog_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(root, text="Apellidos del programador", **label_opts).grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.apellidos_prog_entry = tk.Entry(root, **entry_opts)
        self.apellidos_prog_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Button(root, text="Añadir programador", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.añadir_programador).grid(row=6, columnspan=2, pady=10)

    def crear_equipo(self):
        nombre = self.nombre_equipo_entry.get()
        universidad = self.universidad_entry.get()
        lenguaje = self.lenguaje_entry.get()
        if not nombre or not universidad or not lenguaje:
            messagebox.showerror("Error", "Todos los campos del equipo son obligatorios.")
            return
        self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)
        messagebox.showinfo("Equipo creado", "Equipo creado exitosamente.")

    def añadir_programador(self):
        if not self.equipo:
            messagebox.showerror("Error", "Primero debes crear el equipo.")
            return

        nombre = self.nombre_prog_entry.get()
        apellidos = self.apellidos_prog_entry.get()

        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            programador = Programador(nombre, apellidos)
            self.equipo.añadir_programador(programador)
            self.programador_count += 1
            messagebox.showinfo("Programador añadido", f"Programador {self.programador_count} añadido correctamente.")
            self.nombre_prog_entry.delete(0, tk.END)
            self.apellidos_prog_entry.delete(0, tk.END)

            if self.equipo.esta_lleno():
                self.mostrar_equipo()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_equipo(self):
        info = f"Equipo: {self.equipo.nombre_equipo}\nUniversidad: {self.equipo.universidad}\nLenguaje: {self.equipo.lenguaje_programacion}\nIntegrantes:\n"
        for i, prog in enumerate(self.equipo.programadores, start=1):
            info += f"{i}. {prog.nombre} {prog.apellidos}\n"
        messagebox.showinfo("Equipo completo", info)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
