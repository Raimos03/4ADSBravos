#import customtkinter as ctk
from controler import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sv_ttk
import login

#janela = ctk.CTk()

#Classe da aplicação
# class Application():
#     def __init__(self):
#         self.janela = janela
#         self.janela_login()
#         janela.mainloop()

# Application()

#-----------Main--------
#configuraçoes da janela


root = tk.Tk()
root.geometry("1200x700")
root.resizable(False,False)

IniciaApp(root)


sv_ttk.set_theme("light")
root.mainloop()