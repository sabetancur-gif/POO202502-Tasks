#Ejercicio 2 actividad 4
    
import tkinter as tk
from tkinter import messagebox

class Vendedor:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None

    def verificar_edad(self, edad: int):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        self.edad = edad

    def imprimir(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}"

# Interfaz con Tkinter
def crear_interfaz():
    def procesar_datos():
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        try:
            edad = int(entry_edad.get())
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)
            vendedor_info = vendedor.imprimir()
            messagebox.showinfo("Datos del Vendedor", vendedor_info)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    ventana = tk.Tk()
    ventana.title("Registro de Vendedor")
    ventana.configure(bg="#440099")

    estilo = {"bg": "#440099", "fg": "white", "font": ("Arial", 10, "bold")}

    tk.Label(ventana, text="Nombre:", **estilo).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Apellidos:", **estilo).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_apellidos = tk.Entry(ventana)
    entry_apellidos.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Edad:", **estilo).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_edad = tk.Entry(ventana)
    entry_edad.grid(row=2, column=1, padx=10, pady=5)

    boton = tk.Button(ventana, text="Registrar", command=procesar_datos, **estilo)
    boton.grid(row=3, column=0, columnspan=2, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()
