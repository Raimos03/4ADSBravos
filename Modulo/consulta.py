import customtkinter
from tkinter import * #importando a biblioteca

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("1080x720")
janela.title("BRUTUS - CONSULTA ESTOQUE")
janela.iconbitmap("")
janela.resizable(False, False)


entrada1 = customtkinter.CTkEntry(master=janela, placeholder_text="Pesquisar modelo", width=300).place(x=10,y=25)

butao = customtkinter.CTkButton(master=janela, text="Buscar", width=100).place(x=320, y=25)

janela.mainloop()
