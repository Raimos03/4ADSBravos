import controler
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sv_ttk
from consulta import *
import constantes as const

from mysql import connector

def vVendas(root): #colcoar aqui a tela Thiago
    

    return 

def vConsultaCarros(root):

    def pesquisar():
        modelo = entry_modelo.get()
        chassi = entry_chassi.get()
        cor = entry_cor.get()
        km = entry_km.get()
        preco = entry_preco.get()
        ano = entry_ano.get()
        
        exibir_resultados(pesquisar_no_banco_dados(modelo, chassi, cor, km, preco, ano))

    def exibir_resultados(resultados):
        # Criação da janela de exibição dos resultados
        janela_resultados = Toplevel(janelaConsulta)
        janela_resultados.title("Resultados da pesquisa")
        janela_resultados.geometry("1200x700")
        janela_resultados.resizable(False,False)


        # Exibir cada registro retornado pela pesquisa
        for registro in resultados:
            # Criação do frame para conter o botão e os detalhes do registro
            frame_registro = Frame(janela_resultados)
            frame_registro.pack()

            # Função para capturar o registro selecionado
            def selecionar_registro(registro):
                messagebox.showinfo("Registro selecionado", f"Registro selecionado: {registro}")

            # Botão para selecionar o registro
            botao_selecao = Button(frame_registro, text="Selecionar", command=lambda r=registro: selecionar_registro(r))
            botao_selecao.pack(side=LEFT)

            # Detalhes do registro
            detalhes_registro = f"ID: {registro[0]} Chassi: {registro[1]} Cor: {registro[2]} Km: {registro[3]} Ano: {registro[4]} Modelo: {registro[5]} Custo: {registro[6]} Preço: {registro[7]} Quantidade: {registro[8]}"
            label_detalhes = Label(frame_registro, text=detalhes_registro)
            label_detalhes.pack(side=LEFT)
        



    #Definindo nova janela TopLevel
    janelaConsulta = Toplevel(root)
    janelaConsulta.grab_set()
    janelaConsulta.title("BRUTUS - Consulta de veículos")
    janelaConsulta.geometry("1200x700")
    janelaConsulta.resizable(False,False)

    # Label e campo de pesquisa por modelo
    label_modelo = Label(janelaConsulta, text="Modelo:")
    label_modelo.pack()
    entry_modelo = Entry(janelaConsulta)
    entry_modelo.pack()

    # Label e campo de pesquisa por chassi
    label_chassi = Label(janelaConsulta, text="Chassi:")
    label_chassi.pack()
    entry_chassi = Entry(janelaConsulta)
    entry_chassi.pack()

    # Label e campo de pesquisa por cor
    label_cor = Label(janelaConsulta, text="Cor:")
    label_cor.pack()
    entry_cor = Entry(janelaConsulta)
    entry_cor.pack()

    # Label e campo de pesquisa por km
    label_km = Label(janelaConsulta, text="KM:")
    label_km.pack()
    entry_km = Entry(janelaConsulta)
    entry_km.pack()

    # Label e campo de pesquisa por preço
    label_preco = Label(janelaConsulta, text="Preço:")
    label_preco.pack()
    entry_preco = Entry(janelaConsulta)
    entry_preco.pack()

    # Label e campo de pesquisa por ano
    label_ano = Label(janelaConsulta, text="Ano:")
    label_ano.pack()
    entry_ano = Entry(janelaConsulta)
    entry_ano.pack()

    # Botão de pesquisa
    button_pesquisar = Button(janelaConsulta, text="Pesquisar", command=pesquisar) #clique no botao executa
    button_pesquisar.pack()

    # Iniciar a janela principal
    #root.mainloop()
    return 

def vConsultaClientes(root):
    
    #Definindo nova janela TopLevel
    janelaConsulta = Toplevel(root)
    janelaConsulta.grab_set()
    janelaConsulta.title("BRUTUS - Consulta de clientes")
    janelaConsulta.geometry("1200x700")
    janelaConsulta.resizable(False,False)

    # Label e campo de entrada para nome
    label_nome = Label(janelaConsulta, text="Nome:")
    label_nome.pack()
    entry_nome = Entry(janelaConsulta)
    entry_nome.pack()

    # Label e campo de entrada para idade
    label_idade = Label(janelaConsulta, text="Idade:")
    label_idade.pack()
    entry_idade = Entry(janelaConsulta)
    entry_idade.pack()

    # Label e campo de entrada para CPF
    label_cpf = Label(janelaConsulta, text="CPF:")
    label_cpf.pack()
    entry_cpf = Entry(janelaConsulta)
    entry_cpf.pack()

    # Label e campo de entrada para endereço
    label_endereco = Label(janelaConsulta, text="Endereço:")
    label_endereco.pack()
    entry_endereco = Entry(janelaConsulta)
    entry_endereco.pack()

    # Label e campo de entrada para cidade
    label_cidade = Label(janelaConsulta, text="Cidade:")
    label_cidade.pack()
    entry_cidade = Entry(janelaConsulta)
    entry_cidade.pack()

    # Label e campo de entrada para CEP
    label_cep = Label(janelaConsulta, text="CEP:")
    label_cep.pack()
    entry_cep = Entry(janelaConsulta)
    entry_cep.pack()

    # Label e campo de entrada para telefone
    label_telefone = Label(janelaConsulta, text="Telefone:")
    label_telefone.pack()
    entry_telefone = Entry(janelaConsulta)
    entry_telefone.pack()

    # Label e campo de entrada para email
    label_email = Label(janelaConsulta, text="Email:")
    label_email.pack()
    entry_email = Entry(janelaConsulta)
    entry_email.pack()

    # Label e campo de entrada para sexo
    label_sexo = Label(janelaConsulta, text="Sexo:")
    label_sexo.pack()
    entry_sexo = Entry(janelaConsulta)
    entry_sexo.pack()

    # Botão de pesquisa
    button_pesquisar = Button(janelaConsulta, text="Pesquisar")
    button_pesquisar.pack()

    # Iniciar a janela principal
    #root.mainloop()
    return 

def vLogin(root):

    #Definindo título da janela
    root.title("BRUTUS - Identificação")

    # Labels
    label_username = Label(root, text="Nome de usuário:")
    label_username.pack()

    # Entrada de nome de usuário
    entry_username = Entry(root)
    entry_username.pack()

    # Label
    label_password = Label(root, text="Senha:")
    label_password.pack()

    # Entrada de senha
    entry_password = Entry(root, show="*")
    entry_password.pack()

    # Botão de login
    button_login = Button(root, text="Login")
    button_login.pack()

    # Label para exibir resultado
    label_result = Label(root, text="")
    label_result.pack()

    # Iniciar a janela principal
    #root.mainloop()
    return [login, senha]

def vCadastroCliente(root):

    #Definindo nova janela TopLevel
    janelaConsulta = Toplevel(root)
    janelaConsulta.grab_set()
    janelaConsulta.title("BRUTUS - Cadastro de clientes")
    janelaConsulta.geometry("1200x700")
    janelaConsulta.resizable(False,False)

    # Label e campo de entrada para nome
    label_nome = Label(janelaConsulta, text="Nome:")
    label_nome.pack()
    entry_nome = Entry(janelaConsulta)
    entry_nome.pack()

    # Label e campo de entrada para idade
    label_idade = Label(janelaConsulta, text="Idade:")
    label_idade.pack()
    entry_idade = Entry(janelaConsulta)
    entry_idade.pack()

    # Label e campo de entrada para CPF
    label_cpf = Label(janelaConsulta, text="CPF:")
    label_cpf.pack()
    entry_cpf = Entry(janelaConsulta)
    entry_cpf.pack()

    # Label e campo de entrada para endereço
    label_endereco = Label(janelaConsulta, text="Endereço:")
    label_endereco.pack()
    entry_endereco = Entry(janelaConsulta)
    entry_endereco.pack()

    # Label e campo de entrada para cidade
    label_cidade = Label(janelaConsulta, text="Cidade:")
    label_cidade.pack()
    entry_cidade = Entry(janelaConsulta)
    entry_cidade.pack()

    # Label e campo de entrada para CEP
    label_cep = Label(janelaConsulta, text="CEP:")
    label_cep.pack()
    entry_cep = Entry(janelaConsulta)
    entry_cep.pack()

    # Label e campo de entrada para telefone
    label_telefone = Label(janelaConsulta, text="Telefone:")
    label_telefone.pack()
    entry_telefone = Entry(janelaConsulta)
    entry_telefone.pack()

    # Label e campo de entrada para email
    label_email = Label(janelaConsulta, text="Email:")
    label_email.pack()
    entry_email = Entry(janelaConsulta)
    entry_email.pack()

    # Label e campo de entrada para sexo
    label_sexo = Label(janelaConsulta, text="Sexo:")
    label_sexo.pack()
    entry_sexo = Entry(janelaConsulta)
    entry_sexo.pack()

    # Botão de cadastrar
    button_cadastrar = Button(janelaConsulta, text="Cadastrar")
    button_cadastrar.pack()

    # Iniciar a janela principal
    #root.mainloop()


    return

def vCadastroCarro(root):

    #Definindo nova janela TopLevel
    janelaConsulta = Toplevel(root)
    janelaConsulta.grab_set()
    janelaConsulta.title("BRUTUS - Cadastro de veículos")
    #janelaConsulta.geometry("1200x700")
    #janelaConsulta.resizable(False,False)

    # Label e campo de entrada para nome
    label_nome = Label(janelaConsulta, text="Modelo:")
    label_nome.pack()
    entry_nome = Entry(janelaConsulta)
    entry_nome.pack()

    # Label e campo de entrada para idade
    label_idade = Label(janelaConsulta, text="Chassi:")
    label_idade.pack()
    entry_idade = Entry(janelaConsulta)
    entry_idade.pack()

    # Label e campo de entrada para CPF
    label_cpf = Label(janelaConsulta, text="Cor:")
    label_cpf.pack()
    entry_cpf = Entry(janelaConsulta)
    entry_cpf.pack()

    # Label e campo de entrada para endereço
    label_endereco = Label(janelaConsulta, text="KM:")
    label_endereco.pack()
    entry_endereco = Entry(janelaConsulta)
    entry_endereco.pack()

    # Label e campo de entrada para cidade
    label_cidade = Label(janelaConsulta, text="Preço:")
    label_cidade.pack()
    entry_cidade = Entry(janelaConsulta)
    entry_cidade.pack()

    # Label e campo de entrada para CEP
    label_cep = Label(janelaConsulta, text="Ano:")
    label_cep.pack()
    entry_cep = Entry(janelaConsulta)
    entry_cep.pack()

    # Botão de cadastrar
    button_cadastrar = Button(janelaConsulta, text="Cadastrar")
    button_cadastrar.pack()

    # Iniciar a janela principal
    #root.mainloop()

    return

def janelaPrincipal(root):


    def consultarClientes():
        # Lógica para abrir a janela de consulta de clientes
        print("Opção: Consultar Clientes")
        vConsultaClientes(root)

    def consultarVeiculo():
         # Lógica para abrir a janela de consulta de veículo
        print("Opção: Consultar Veículo")
        vConsultaCarros(root)

    def cadastrarCliente():
        # Lógica para abrir a janela de cadastro de clientes
        print("Opção: Cadastrar Cliente")
        vCadastroCliente(root)

    def cadastrarVeiculo():
        # Lógica para abrir a janela de cadastro de veículo
        print("Opção: Cadastrar Veículo")
        vCadastroCarro(root)

    # Função para exibir a opção selecionada
    def exibir_opcao(opcao):
        label_opcao.config(text=f"Opção selecionada: {opcao}")


    # Barra de navegação
    menu_bar = Menu(root)

    #imagem = PhotoImage(file="img/logo.ico")  
    # Criar um widget Label com a imagem como fundo
    #label_fundo = Label(root, image=imagem)
    label_fundo = Label(root)
    label_fundo.pack(anchor=CENTER)


    # Opções do menu
    menu_veiculo = Menu(menu_bar, tearoff=0)
    menu_veiculo.add_command(label="Consultar Veículo", command=consultarVeiculo)
    menu_veiculo.add_command(label="Cadastrar Veículo", command= cadastrarVeiculo)
    menu_bar.add_cascade(label="Veículo", menu=menu_veiculo)

    menu_clientes = Menu(menu_bar, tearoff=0)
    menu_clientes.add_command(label="Consultar Clientes", command=consultarClientes)
    menu_clientes.add_command(label="Cadastrar Cliente", command=cadastrarCliente)
    menu_bar.add_cascade(label="Clientes", menu=menu_clientes)

    root.config(menu=menu_bar)

    # Label para exibir a opção selecionada
    label_opcao = Label(root, text="Opção selecionada:")
    label_opcao.pack()

    # Iniciar a janela principal
    #root.mainloop()

    return




def MainView(root):


    print("Tela de Login criada : 1")
    login,senha=vLogin(root)
    const.inputLogin = login
    const.inputSenha = senha
    const.usuarioAut=ctlrLoginESenha(login,senha)
    



    return 





