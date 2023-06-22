from controler import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sv_ttk




#-----------main--------
#configuraçoes da janela

root = tk.Tk()
root.geometry("1200x700")
root.resizable(False,False)

IniciaApp(root)


sv_ttk.set_theme("light")
root.mainloop()