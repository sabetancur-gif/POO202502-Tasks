"""
Módulo delete.py

Interfaz gráfica para eliminar un contacto por nombre.
Replica la lógica del Java DeleteFriend:
- Verifica existencia del nombre.
- Crea un archivo temporal copiando todas las entradas excepto la eliminada.
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
    Clase para operaciones de listado y borrado.
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
        """Parsea línea en (nombre, número) o None si inválida."""
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
        """Lista contactos válidos del archivo."""
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
        """
        for name, _ in self.list_friends():
            if name == input_name:
                return True
        return False

    def delete_friend(self, input_name: str) -> Tuple[bool, str]:
        """
        Elimina el contacto con nombre input_name usando un archivo temporal.

        Parameters
        ----------
        input_name : str
            Nombre del contacto a eliminar.

        Returns
        -------
        Tuple[bool, str]
            (True, mensaje) si fue eliminado; (False, mensaje) si no existe o error.
        """
        try:
            if not self.exists_name(input_name):
                return False, " Input name does not exists. "

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
                            tmpraf.write(line + os.linesep)
                            continue
                        name = line[:index]
                        if name == input_name:
                            # omitimos la línea (borrado)
                            continue
                        tmpraf.write(line + os.linesep)
                os.replace(tmp_path, self.path)
            finally:
                if os.path.exists(tmp_path):
                    try:
                        os.remove(tmp_path)
                    except OSError:
                        pass
            return True, " Friend deleted. "
        except OSError as err:
            return False, str(err)


class DeleteFriendGUI(tk.Tk):
    """
    Interfaz para seleccionar un contacto del listado y eliminarlo.
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Delete Friend")
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

        btn_frame: tk.Frame = tk.Frame(self)
        btn_frame.pack(padx=8, pady=8)
        del_btn: tk.Button = tk.Button(btn_frame, text="Delete", command=self.on_delete)
        del_btn.pack(side="left", padx=6)
        refresh_btn: tk.Button = tk.Button(btn_frame, text="Refresh list", command=self.load_list)
        refresh_btn.pack(side="left", padx=6)
        close_btn: tk.Button = tk.Button(btn_frame, text="Close", command=self.destroy)
        close_btn.pack(side="left", padx=6)

        self.load_list()

    def load_list(self) -> None:
        """
        Carga los contactos en el Listbox (formato 'Nombre!Numero').
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
        Rellena el Entry de nombre con la selección del Listbox.
        """
        sel = self.listbox.curselection()
        if not sel:
            return
        text = self.listbox.get(sel[0])
        idx = text.find(SEP)
        if idx != -1:
            name = text[:idx]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)

    def on_delete(self) -> None:
        """
        Handler para el botón Delete: valida la entrada y solicita el borrado.
        """
        input_name: str = self.name_entry.get().strip()
        if not input_name:
            messagebox.showwarning("Faltan datos", "Debe proporcionar: <Nombre>")
            return
        ok, msg = self.fb.delete_friend(input_name)
        if ok:
            messagebox.showinfo("Resultado", msg)
            self.load_list()
            self.name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Resultado", msg)


if __name__ == "__main__":
    app = DeleteFriendGUI()
    app.mainloop()
