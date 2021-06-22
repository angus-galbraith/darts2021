import tkinter as tk



class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Darts")
        self.geometry('800x600')