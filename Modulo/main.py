import conexaoBd
from controler import *
import tkinter as tk


#-----------Main--------
#configuraçoes da janela

root = tk.Tk()
root.title("BRUTUS")
root.geometry("1200x700")
root.iconbitmap("img\logo.ico")
root.resizable(False,False)

IniciaApp(root)

