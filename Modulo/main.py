import conexaoBd
from controler import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
PATH = Path(__file__).parent / 'img'
#import ttkbootstrap

#-----------Main--------
#configuraçoes da janela

root = ttk.Window("BRUTUS","yeti",iconphoto='img/logo2.png')
root.geometry("1200x700")
root.resizable(False,False)
const.root=root

IniciaApp(root)

root.mainloop()



con.close()
