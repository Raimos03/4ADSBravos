import conexaoBd
from controler import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
#import ttkbootstrap

#-----------Main--------
#configuraçoes da janela

root = ttk.Window("BRUTUS","yeti")


#root.title("BRUTUS")
root.geometry("1200x700")

#root.iconbitmap("img/logo.ico")



root.resizable(False,False)
const.root=root


IniciaApp(root)

root.mainloop()
#style = ttk.Style("yeti")


con.close()
