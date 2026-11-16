
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

APP_NAME = "PES 6 Editor 2027"

class PES6Editor:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("1100x700")
        self.root.minsize(850, 550)
        self.root.configure(bg="#101820")

        self.game_folder = ""

        self.create_ui()

    def create_ui(self):
        header = tk.Frame(self.root, bg="#182936", height=75)
        header.pack(fill="x")

        tk.Label(
            header, text=APP_NAME,
            font=("Arial", 23, "bold"),
            fg="#00d9a6", bg="#182936"
        ).pack(side="left", padx=25, pady=18)

        sidebar = tk.Frame(self.root, bg="#18232d", width=220)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar, text="MAIN MENU",
            font=("Arial", 12, "bold"),
            fg="white", bg="#18232d"
        ).pack(pady=20)

        for name in [
            "Dashboard", "Game Folder",
            "Players Editor", "Teams Editor",
            "Kits Editor", "Graphics Editor",
            "AFS Explorer", "Settings"
        ]:
            tk.Button(
                sidebar, text=name,
                font=("Arial", 11),
                bg="#263746", fg="white",
                activebackground="#00a982",
                activeforeground="white",
                relief="flat", anchor="w",
                padx=18, pady=12,
                command=lambda n=name: self.show_page(n)
            ).pack(fill="x", padx=10, pady=3)

        self.content = tk.Frame(self.root, bg="#101820")
        self.content.pack(expand=True, fill="both")

        self.show_page("Dashboard")

    def show_page(self, page):
        for widget in self.content.winfo_children():
            widget.destroy()

        tk.Label(
            self.content, text=page,
            font=("Arial", 25, "bold"),
            fg="#00d9a6", bg="#101820"
        ).pack(anchor="w", padx=30, pady=30)

        if page == "Dashboard":
            self.dashboard()
        elif page == "Game Folder":
            self.folder_page()
        else:
            tk.Label(
                self.content,
                text="This module is not implemented yet.",
                font=("Arial", 13),
                fg="white", bg="#101820"
            ).pack(pady=30)

    def dashboard(self):
        cards = [
            ("Game Folder", "Not selected"),
            ("Players Editor", "Coming soon"),
            ("Teams Editor", "Coming soon"),
            ("AFS Explorer", "Coming soon")
        ]

        for title, status in cards:
            card = tk.Frame(
                self.content, bg="#203442",
                padx=25, pady=20
            )
            card.pack(fill="x", padx=30, pady=8)

            tk.Label(
                card, text=title,
                fg="white", bg="#203442",
                font=("Arial", 15, "bold")
            ).pack(anchor="w")

            tk.Label(
                card, text=status,
                fg="#00d9a6", bg="#203442",
                font=("Arial", 11)
            ).pack(anchor="w", pady=5)

    def folder_page(self):
        tk.Label(
            self.content,
            text="Select your PES 6 installation folder",
            fg="white", bg="#101820",
            font=("Arial", 14)
        ).pack(pady=25)

        tk.Button(
            self.content, text="Browse Game Folder",
            command=self.select_folder,
            bg="#00a982", fg="white",
            font=("Arial", 12, "bold"),
            relief="flat", padx=20, pady=12
        ).pack()

        self.folder_label = tk.Label(
            self.content,
            text=self.game_folder or "No folder selected",
            fg="white", bg="#101820",
            wraplength=600
        )
        self.folder_label.pack(pady=20)

    def select_folder(self):
        folder = filedialog.askdirectory(
            title="Select PES 6 Folder"
        )
        if folder:
            self.game_folder = folder
            self.folder_label.config(text=folder)
            messagebox.showinfo(
                APP_NAME,
                "Game folder selected successfully."
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = PES6Editor(root)
    root.mainloop()
