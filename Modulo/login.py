#import customtkinter as ctk
from tkinter import * #importando a biblioteca
import conexaoBd



#Classe da aplicação


# def janela_consulta(self):
# #Configurando janela de consulta
#     janela.iconify()
#     janela_consulta = ctk.CTkToplevel(janela)
#     janela_consulta.geometry("1080x720")
#     janela_consulta.title("BRUTUS - CONSULTA ESTOQUE")
#     janela_consulta.iconbitmap("")
#     janela_consulta.resizable(False, False)
# #Configurando campos e botões
#     entrada1 = ctk.CTkEntry(master=janela_consulta, placeholder_text="Pesquisar modelo", width=300).place(x=10,y=25)
#     butao = ctk.CTkButton(master=janela_consulta, text="Buscar", width=100).place(x=320, y=25)

def vLogin(r):
#Configurando janela de login
 

    janela.title("BRUTUS - IDENTIFICAÇÃO")
    janela.iconbitmap("")
    janela.resizable(False, False)

#Configurando botões
    label = ctk.CTkLabel(master=janela, text="Autenticação").place(x=15,y=20)
    entrada1 = ctk.CTkEntry(master=janela, placeholder_text="Nome de usuário", width=300).place(x=10,y=105)
    entrada2 = ctk.CTkEntry(master=janela, placeholder_text="Senha", width=300, show="*").place(x=10,y=155)
    butao = ctk.CTkButton(master=janela, text="LOGIN", width=300, command=self.janela_consulta).place(x=10, y=205)

# ------ Principal Login

#janela = ctk.CTk()
    return



