import controler
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sv_ttk



def FrameMenu( pai):

    fr1= tk.Frame(master=pai,height=50,width=100,bg="blue")
    fr1.pack()

    fr2= tk.Frame(master=pai,bg="red")
    fr2.place(x=250,y=500,height=200,width=500)

    fr3= tk.Frame(master=pai,bg="orange")
    fr3.place(x=50,y=100,height=200,width=500)
                                    
    # s1=ttk.Style()
    # s1.configure('NAME.TFrame',background="#E61E50")
    # fr2=ttk.Frame(root,height=100,width=100,style='NAME.TFrame')
    # fr2.place( x=10, y=10)
    # fr2.pack()

    button = ttk.Button(pai,text="CLique")
    button.pack()
    return 




