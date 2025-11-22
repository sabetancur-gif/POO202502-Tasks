"""
Módulo update.py

Interfaz gráfica para actualizar el número de un contacto.
Replica la lógica del Java UpdateFriend:
- Verifica existencia del nombre.
- Crea un archivo temporal y escribe el contenido actualizado.
- Reemplaza el archivo original por el temporal.
"""
from __future__ import annotations

import os
import tempfile
import tkinter as tk
from tkinter import messagebox
from typing import Optional, Tuple

FILENAME: str = "friendsContact.txt"
SEP: str = "!"


class FriendBook:
    """
    Clase con utilidades para leer, comprobar existencia y actualizar contactos.
    """

    def __init__(self, path: str = FILENAME, sep: str = SEP) -> None:
        self.path: str = path
        self.sep: str = sep
        self._ensure_file()

    def _ensure_file(self) -> None:
        """Crea el archivo si no existe."""
        if not os.path.exists(self.path):
            open(self.path, "a", encoding="utf-8").close()

    def _parse_line(self, line: str) -> Optional[Tuple[str, int]]:
        """Parsea una línea en (nombre, número) o None si está mal formada."""
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
        """Devuelve la lista de contactos válidos del archivo."""
        friends: list[Tuple[str, int]] = []
        self._ensure_file()
        with open(self.path, "r", encoding="utf-8") as fh:
            for raw in fh:
                parsed = self._parse_line(raw)
                if parsed:
                    friends.append(parsed)
        return friends

    def exists_name(self, input_name: str) -> bool:
        """
        Comprueba si existe un contacto con el nombre dado.

        Parameters
        ----------
        input_name : str
            Nombre a comprobar.

        Returns
        -------
        bool
            True si existe, False en caso contrario.
        """
        for name, _ in self.list_friends():
            if name == input_name:
                return True
        return False

    def update_friend(self, input_name: str, new_number: int) -> Tuple[bool, str]:
        """
        Actualiza el número del contacto que coincide con input_name.

        Crea un archivo temporal, escribe todas las entradas copiadas
        pero reemplaza la línea del contacto objetivo por la nueva.

        Parameters
        ----------
        input_name : str
            Nombre del contacto a actualizar.
        new_number : int
            Nuevo número que se asignará.

        Returns
        -------
        Tuple[bool, str]
            (True, mensaje) si se actualizó, (False, mensaje) si no existe o hubo error.
        """
        try:
            if not self.exists_name(input_name):
                return False, " El nombre introducido no existe. "

            fd, tmp_path = tempfile.mkstemp(prefix="tmp_friends_", text=True)
            os.close(fd)
            try:
                with open(self.path, "r", encoding="utf-8") as raf, \
                     open(tmp_path, "w", encoding="utf-8") as tmpraf:
                    for raw in raf:
                        line = raw.rstrip("\n")
                        if not line:
                            continue
                        index = line.find(self.sep)
                        if index == -1:
                            # Si no tiene separador lo copiamos tal cual
                            tmpraf.write(line + os.linesep)
                            continue
                        name = line[:index]
                        if name == input_name:
                            new_line = f"{name}{self.sep}{new_number}"
                            tmpraf.write(new_line + os.linesep)
                        else:
                            tmpraf.write(line + os.linesep)
                # Reemplazar el archivo original de forma atómica cuando sea posible
                os.replace(tmp_path, self.path)
            finally:
                # Si algo falló y quedó el temporal, intentar eliminarlo
                if os.path.exists(tmp_path):
                    try:
                        os.remove(tmp_path)
                    except OSError:
                        pass
            return True, " Amigo updated. "
        except OSError as err:
            return False, str(err)


class UpdateFriendGUI(tk.Tk):
    """
    Interfaz para seleccionar un contacto y actualizar su número.
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Update Friend")
        self.geometry("420x300")
        self.resizable(False, False)
        self.fb: FriendBook = FriendBook()

        tk.Label(self, text="Selecciona un contacto:").pack(padx=8, pady=(8, 0), anchor="w")
        self.listbox: tk.Listbox = tk.Listbox(self, width=50, height=8)
        self.listbox.pack(padx=8, pady=6)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        entry_frame: tk.Frame = tk.Frame(self)
        entry_frame.pack(fill="x", padx=8, pady=6)
        tk.Label(entry_frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.name_entry: tk.Entry = tk.Entry(entry_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=6, pady=4)
        tk.Label(entry_frame, text="Nuevo Número:").grid(row=1, column=0, sticky="e")
        self.num_entry: tk.Entry = tk.Entry(entry_frame, width=30)
        self.num_entry.grid(row=1, column=1, padx=6, pady=4)

        btn_frame: tk.Frame = tk.Frame(self)
        btn_frame.pack(padx=8, pady=8)
        update_btn: tk.Button = tk.Button(btn_frame, text="Update", command=self.on_update)
        update_btn.pack(side="left", padx=6)
        refresh_btn: tk.Button = tk.Button(btn_frame, text="Refresh list", command=self.load_list)
        refresh_btn.pack(side="left", padx=6)
        close_btn: tk.Button = tk.Button(btn_frame, text="Close", command=self.destroy)
        close_btn.pack(side="left", padx=6)

        self.load_list()

    def load_list(self) -> None:
        """
        Carga los contactos al Listbox en formato 'Nombre!Numero'.
        """
        self.listbox.delete(0, tk.END)
        try:
            friends = self.fb.list_friends()
            for name, number in friends:
                self.listbox.insert(tk.END, f"{name}{SEP}{number}")
        except OSError as err:
            messagebox.showerror("IOError", str(err))

    def on_select(self, _event) -> None:
        """
        Al seleccionar un elemento del Listbox, rellena los Entry con nombre y número.
        """
        selection = self.listbox.curselection()
        if not selection:
            return
        text = self.listbox.get(selection[0])
        idx = text.find(SEP)
        if idx != -1:
            name = text[:idx]
            number = text[idx + 1 :]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.num_entry.delete(0, tk.END)
            self.num_entry.insert(0, number)

    def on_update(self) -> None:
        """
        Handler del botón Update: valida y solicita la actualización a FriendBook.
        """
        input_name: str = self.name_entry.get().strip()
        num_str: str = self.num_entry.get().strip()
        if not input_name or not num_str:
            messagebox.showwarning("Faltan datos", "Debe proporcionar: <Nombre> <NuevoNumero>")
            return
        try:
            new_number: int = int(num_str)
        except ValueError as nef:
            messagebox.showerror("Número inválido", str(nef))
            return

        ok, msg = self.fb.update_friend(input_name, new_number)
        if ok:
            messagebox.showinfo("Resultado", msg)
            self.load_list()
        else:
            messagebox.showwarning("Resultado", msg)


if __name__ == "__main__":
    app = UpdateFriendGUI()
    app.mainloop()
