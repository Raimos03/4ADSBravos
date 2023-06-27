import customtkinter as ctk
from tkinter import * #importando a biblioteca
import conexaoBd

janela = ctk.CTk()

#Classe da aplicação
class Application():
    def __init__(self):
        self.janela = janela
        self.janela_login()
        janela.mainloop()

    def janela_consulta(self):
    #Configurando janela de consulta
        janela.iconify()
        janela_consulta = ctk.CTkToplevel(janela)
        janela_consulta.geometry("1080x720")
        janela_consulta.title("BRUTUS - CONSULTA ESTOQUE")
        janela_consulta.iconbitmap("")
        janela_consulta.resizable(False, False)
    #Configurando campos e botões
        entrada1 = ctk.CTkEntry(master=janela_consulta, placeholder_text="Pesquisar modelo", width=300).place(x=10,y=25)
        butao = ctk.CTkButton(master=janela_consulta, text="Buscar", width=100).place(x=320, y=25)

    def janela_login(self):
    #Configurando janela de login
        ctk.set_default_color_theme("blue")
        janela.geometry("320x400")
        janela.title("BRUTUS - IDENTIFICAÇÃO")
        janela.iconbitmap("")
        janela.resizable(False, False)
    #Configurando botões
        label = ctk.CTkLabel(master=janela, text="Autenticação").place(x=15,y=20)
        entrada1 = ctk.CTkEntry(master=janela, placeholder_text="Nome de usuário", width=300).place(x=10,y=105)
        entrada2 = ctk.CTkEntry(master=janela, placeholder_text="Senha", width=300, show="*").place(x=10,y=155)
        butao = ctk.CTkButton(master=janela, text="LOGIN", width=300, command=self.janela_consulta).place(x=10, y=205)

Application()
