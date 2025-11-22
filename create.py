"""
Módulo create.py

Interfaz gráfica con Tkinter para añadir un contacto al archivo
'friendsContact.txt'. Cada línea del archivo tiene el formato:
    Nombre!Numero

Este módulo replica la lógica del programa Java AddFriend:
- Crea el archivo si no existe.
- Comprueba duplicados por nombre o por número.
- Añade la entrada al final del archivo.
- Muestra mensajes al usuario mediante cuadros de diálogo.

Uso:
    python add_friend_gui.py
"""
from __future__ import annotations

import os
import tkinter as tk
from tkinter import messagebox
from typing import Optional, Tuple

FILENAME: str = "friendsContact.txt"
SEP: str = "!"


class FriendBook:
    """
    Clase para manipular el archivo de contactos.

    Atributos
    ---------
    path: str
        Ruta del archivo (por defecto 'friendsContact.txt').
    sep: str
        Separador entre nombre y número (por defecto '!').
    """

    def __init__(self, path: str = FILENAME, sep: str = SEP) -> None:
        """
        Inicializa FriendBook y asegura que el archivo exista.

        Parameters
        ----------
        path : str
            Ruta del archivo donde se guardan los contactos.
        sep : str
            Separador entre nombre y número en cada línea.
        """
        self.path: str = path
        self.sep: str = sep
        self._ensure_file()

    def _ensure_file(self) -> None:
        """
        Crea el archivo vacío si no existe.
        """
        if not os.path.exists(self.path):
            open(self.path, "a", encoding="utf-8").close()

    def _parse_line(self, line: str) -> Optional[Tuple[str, int]]:
        """
        Parsea una línea del archivo y devuelve (nombre, número).

        Devuelve None si la línea está vacía o mal formada.

        Parameters
        ----------
        line : str
            Línea leída del archivo (incluye salto de línea).

        Returns
        -------
        Optional[Tuple[str, int]]
            Tupla (nombre, número) o None si no se puede parsear.
        """
        line = line.strip()
        if not line:
            return None
        parts = line.split(self.sep)
        if len(parts) != 2:
            return None
        name = parts[0]
        try:
            number = int(parts[1])
        except ValueError:
            return None
        return name, number

    def list_friends(self) -> list[Tuple[str, int]]:
        """
        Lista todos los contactos válidos del archivo.

        Returns
        -------
        list[Tuple[str, int]]
            Lista de tuplas (nombre, número).
        """
        friends: list[Tuple[str, int]] = []
        self._ensure_file()
        with open(self.path, "r", encoding="utf-8") as fh:
            for raw in fh:
                parsed = self._parse_line(raw)
                if parsed:
                    friends.append(parsed)
        return friends

    def add_friend(self, new_name: str, new_number: int) -> Tuple[bool, str]:
        """
        Añade un nuevo contacto si no existe el nombre ni el número.

        Parameters
        ----------
        new_name : str
            Nombre del contacto a añadir.
        new_number : int
            Número del contacto a añadir.

        Returns
        -------
        Tuple[bool, str]
            (True, mensaje) si se añadió; (False, mensaje) si hubo duplicado o error.
        """
        try:
            self._ensure_file()
            for name, number in self.list_friends():
                if name == new_name or number == new_number:
                    return False, " El nombre o número introducido ya existe. "

            with open(self.path, "a", encoding="utf-8") as fh:
                fh.write(f"{new_name}{self.sep}{new_number}" + os.linesep)
            return True, " Amigo agregado. "
        except OSError as err:
            return False, str(err)


class AddFriendGUI(tk.Tk):
    """
    Ventana principal para añadir contactos.

    Contiene:
    - Entradas para nombre y número.
    - Botón para añadir que valida y muestra mensajes.
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Add Friend")
        self.geometry("360x160")
        self.resizable(False, False)
        self.fb: FriendBook = FriendBook()

        # Widgets
        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
        self.name_entry: tk.Entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=0, column=1, padx=8, pady=8)

        tk.Label(self, text="Número:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
        self.num_entry: tk.Entry = tk.Entry(self, width=30)
        self.num_entry.grid(row=1, column=1, padx=8, pady=8)

        add_btn: tk.Button = tk.Button(self, text="Add Friend", command=self.on_add)
        add_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def on_add(self) -> None:
        """
        Handler para el botón 'Add Friend'.

        Valida los campos, intenta convertir el número a int y llama a FriendBook.add_friend.
        Muestra cuadros de diálogo según el resultado.
        """
        name: str = self.name_entry.get().strip()
        num_str: str = self.num_entry.get().strip()

        if not name or not num_str:
            messagebox.showwarning("Faltan datos", "Debe proporcionar: <Nombre> <Numero>")
            return

        try:
            number: int = int(num_str)
        except ValueError as nef:
            # Equivalente a NumberFormatException en Java
            messagebox.showerror("Número inválido", str(nef))
            return

        ok, msg = self.fb.add_friend(name, number)
        if ok:
            messagebox.showinfo("Resultado", msg)
            self.name_entry.delete(0, tk.END)
            self.num_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Resultado", msg)


if __name__ == "__main__":
    app = AddFriendGUI()
    app.mainloop()
