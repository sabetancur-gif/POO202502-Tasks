"""
Módulo display_friends_gui

Interfaz gráfica que muestra los contactos almacenados en
`friendsContact.txt`. Reproduce la funcionalidad de DisplayFriends
del programa Java.

Uso:
    python display_friends_gui.py
"""
from __future__ import annotations

import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from typing import Optional, Tuple

FILENAME: str = "friendsContact.txt"
SEP: str = "!"


class FriendBook:
    """
    Clase auxiliar para leer contactos del archivo.
    """

    def __init__(self, path: str = FILENAME, sep: str = SEP) -> None:
        """
        Inicializa FriendBook y asegura la existencia del archivo.

        Parameters
        ----------
        path : str
            Ruta del archivo de contactos.
        sep : str
            Separador entre nombre y número.
        """
        self.path: str = path
        self.sep: str = sep
        self._ensure_file()

    def _ensure_file(self) -> None:
        """
        Crea el archivo si no existe.
        """
        if not os.path.exists(self.path):
            open(self.path, "a", encoding="utf-8").close()

    def _parse_line(self, line: str) -> Optional[Tuple[str, int]]:
        """
        Parsea una línea del archivo en (nombre, número) o None si la línea es inválida.
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
        Devuelve la lista de contactos válidos.
        """
        friends: list[Tuple[str, int]] = []
        self._ensure_file()
        with open(self.path, "r", encoding="utf-8") as fh:
            for raw in fh:
                parsed = self._parse_line(raw)
                if parsed:
                    friends.append(parsed)
        return friends


class DisplayFriendsGUI(tk.Tk):
    """
    Ventana que muestra los contactos en un ScrolledText con botón Refresh.
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Display Friends")
        self.geometry("480x360")
        self.resizable(True, True)
        self.fb: FriendBook = FriendBook()

        tk.Label(self, text="Contactos (Nombre y Número):").pack(padx=8, pady=(8, 0), anchor="w")
        self.text: scrolledtext.ScrolledText = scrolledtext.ScrolledText(self, width=60, height=18, wrap=tk.WORD)
        self.text.pack(padx=8, pady=6, expand=True, fill="both")

        btn_frame: tk.Frame = tk.Frame(self)
        btn_frame.pack(padx=8, pady=6, anchor="e")
        refresh_btn: tk.Button = tk.Button(btn_frame, text="Refresh", command=self.load_contacts)
        refresh_btn.pack(side="right", padx=4)
        close_btn: tk.Button = tk.Button(btn_frame, text="Close", command=self.destroy)
        close_btn.pack(side="right", padx=4)

        # Cargar al inicio
        self.load_contacts()

    def load_contacts(self) -> None:
        """
        Lee los contactos desde FriendBook y los muestra en el ScrolledText.
        Maneja errores de IO y formatos.
        """
        try:
            friends = self.fb.list_friends()
            self.text.config(state=tk.NORMAL)
            self.text.delete("1.0", tk.END)
            if not friends:
                # Si no hay contactos, dejamos el área vacía (comportamiento similar al Java).
                pass
            else:
                for name, number in friends:
                    self.text.insert(tk.END, f"Friend Name: {name}\nContact Number: {number}\n\n")
            self.text.config(state=tk.DISABLED)
        except OSError as ioe:
            messagebox.showerror("IOError", str(ioe))
        except ValueError as nef:
            messagebox.showerror("ValueError", str(nef))


if __name__ == "__main__":
    app = DisplayFriendsGUI()
    app.mainloop()
