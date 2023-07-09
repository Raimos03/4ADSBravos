import controler as ctrl
import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import messagebox
from cadastra import *

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image

from consulta import *
import constantes as const

from mysql import connector

PATH = Path(__file__).parent / 'img'






def montaTabela(px,py,lvalores):

    treeFrame = ttk.Frame(const.FrameTotalPrincipal,width=630,height=150,style="#ffff")
    treeFrame.place(x=px+45,y=py)
    #for el in lvalores:

    s=ttk.Style()
    s.configure('Treeview', foreground = '#10223b',rowheight=25,font=("Helvetica",9),highlighttickness='#3b7cd1')
    s.configure("Treeview.Heading", font=('Helvetica', 10,'bold'),background='#3b7cd1', foreground='#f0f2f5') # Modify the font of the headings
    s.map('Treeview', background = [('selected','#b1c0de')])
    #3b7cd1

    col = ("Nome","Sobrenome","Cargo")
    tabela =ttk.Treeview(treeFrame, show="headings",columns = col, height=5 ,style='Treeview',padding=10)


    tabela.column("Nome",width = 180,anchor="ce")
    tabela.column("Sobrenome",width = 180,anchor="ce")
    tabela.column("Cargo",width = 180,anchor="ce")

    
    for s in col:
        tabela.heading(s, text=s)

    for el in lvalores:

        tabela.insert('',ttk.END,values=(el[3],el[4],el[5]))
        

    tabela.pack(fill='x')

    return

def vVendas(root): #colocar aqui a tela Thiago

    sf = ttk.Style()
    sf.configure('TFrame')
    sf.configure('VD.TFrame',background='#f5f6f7')
    comecoX=80
    comecoY=100
    paddingCampoX=70
    paddingCampoY=20
    paddingTextoY=20


    lvalores=[]

    global FrameTotalVendas
    const.telaSaida=5
    
    FrameVendas = ttk.Frame(root,height=700,width=1200)
    const.FrameTotalVendas = FrameVendas
    FrameVendas.pack()


    FrameMeio = ttk.Frame(FrameVendas,height=500,width=730,style='VD.TFrame') #height=160,width=730
    FrameMeio.place(x=230, y =100)
    #bootstyle=("iNVERSE","light")

    LVenda = ttk.Label(root, text= "Vendas:",foreground='#3b7cd1',background='#ffffff',font=("Helvetica",22))
    LVenda.place(x=80, y =80)

    #---

    FrameCadastrarVenda= ttk.Frame(FrameMeio,height=500,width=730,style='VD.TFrame') #height=160,width=730
    FrameCadastrarVenda.place(x=50, y =50)
    #bootstyle=("iNVERSE","light")
    #cinza #f5f6f7'

    LCadastrarVenda = ttk.Label(FrameMeio, text= "Cadastrar nova venda:",foreground='#3b7cd1',background='#f5f6f7',font=("Helvetica",18))
    LCadastrarVenda.place(x=80, y =45)


    # Entrada do id usuario
    label_campo1 = ttk.Label(FrameMeio, text="ID",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_campo1.place(x=comecoX,y=comecoY)

    entry_campo1 = ttk.Entry(FrameMeio,width=5)
    entry_campo1.place(x=comecoX,y=comecoY+paddingTextoY)


    # Entrada cpf usuario
    label_campo2 = ttk.Label(FrameMeio, text="CPF",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_campo2.place(x=comecoX+paddingCampoX,y=comecoY)

    entry_campo2 = ttk.Entry(FrameMeio,width=15)
    entry_campo2.place(x=comecoX+paddingCampoX,y=comecoY+paddingTextoY)

    # Entrada Nome usuario
    label_campo3 = ttk.Label(FrameMeio, text="Nome",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_campo3.place(x=comecoX+(paddingCampoX*3),y=comecoY)

    entry_campo3 = ttk.Entry(FrameMeio,width=35)
    entry_campo3.place(x=comecoX+(paddingCampoX*3),y=comecoY+paddingTextoY)

    # Entrada dp id do carro

    label_campo4 = ttk.Label(FrameMeio, text="ID do carro",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_campo4.place(x=comecoX,y=comecoY+paddingCampoY*3)

    entry_campo4 = ttk.Entry(FrameMeio,width=5)
    entry_campo4.place(x=comecoX,y=comecoY+paddingCampoY*3+ paddingTextoY)

    #Entrada dp modelo do carro

    label_campo5 = ttk.Label(FrameMeio, text="Modelo do carro",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_campo5.place(x=comecoX+paddingCampoX,y=comecoY+paddingCampoY*3)

    entry_campo5 = ttk.Entry(FrameMeio,width=15)
    entry_campo5.place(x=comecoX+paddingCampoX,y=comecoY+paddingCampoY*3+paddingTextoY)

    # Cor do mdelo

    label_campo6 = ttk.Label(FrameMeio, text="Cor",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_campo6.place(x=comecoX+paddingCampoX*3,y=comecoY+paddingCampoY*3)

    entry_campo6 = ttk.Entry(FrameMeio,width=15)
    entry_campo6.place(x=comecoX+paddingCampoX*3,y=comecoY+paddingCampoY*3+paddingTextoY)


    #Preco

    label_campo6 = ttk.Label(FrameMeio, text="Preco",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_campo6.place(x=comecoX+paddingCampoX*5,y=comecoY+paddingCampoY*3)

    entry_campo6 = ttk.Entry(FrameMeio,width=23)
    entry_campo6.place(x=comecoX+paddingCampoX*5,y=comecoY+paddingCampoY*3+paddingTextoY)

    #Quantidade

    label_campo6 = ttk.Label(FrameMeio, text="Quantidade",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_campo6.place(x=comecoX+paddingCampoX*7+40,y=comecoY+paddingCampoY*3)

    entry_campo6 = ttk.Entry(FrameMeio,width=7)
    entry_campo6.place(x=comecoX+paddingCampoX*7+40,y=comecoY+paddingCampoY*3+paddingTextoY)

    # Preco modelo



    # Cor do mdelo




    #----- deletar venda

    LCadastrarVenda = ttk.Label(FrameMeio, text= "Deletar Venda:",foreground='#3b7cd1',background='#f5f6f7',font=("Helvetica",18))
    LCadastrarVenda.place(x=80, y =240) 


    #botao cadastrar e deletar




    # if len(lista)<8:
    #     ExibePainelMensagemMeio("Favor Preencher todos os campos para cadastro")


    const.root.mainloop()
    return 


def cadastrarCliente():
        # Lógica para abrir a janela de cadastro de clientes
        print("Opção: Cadastrar Cliente")
        vCadastroCliente(const.root)

def cadastrarVeiculo():
        # Lógica para abrir a janela de cadastro de veículo
        print("Opção: Cadastrar Veículo")
        vCadastroCarro(const.root)

def CriaMenuPrincipal():



    #recebe o numero da tela

    frameUsuario=encontraSaidaFrame(const.telaSaida)

    root=const.root

    sm=ttk.Style()
    sm.configure('custom.TMenubutton', background='red', foreground='white', font=('Helvetica', 24))
    
    tmenu = tk.Menu(root)
    
    
    #imagem = PhotoImage(file="img/logo.ico")  
    # Criar um widget Label com a imagem como fundo
    #label_fundo = Label(root, image=imagem)

    ##label_fundo = ttk.Label(root,text="LABEL FUNDO")
    ##label_fundo.pack(anchor=CENTER)


    # Opções do menu

    menu_principal = ttk.Menu(tmenu, tearoff=0)
    menu_principal.add_command(label="Home", command=lambda: trocaFramePrincipali(const.telaSaida))
    tmenu.add_cascade(label="Home", menu=menu_principal)
    

    menu_veiculo = ttk.Menu(tmenu, tearoff=0)
    menu_veiculo.add_command(label="Consultar Veículo", command=consultarVeiculo)
    menu_veiculo.add_command(label="Cadastrar Veículo", command= cadastrarVeiculo)
    tmenu.add_cascade(label="Veículo", menu=menu_veiculo)

    menu_clientes = ttk.Menu(tmenu, tearoff=0)
    menu_clientes.add_command(label="Consultar Clientes", command=consultarClientes)
    menu_clientes.add_command(label="Cadastrar Cliente", command=cadastrarCliente)
    tmenu.add_cascade(label="Clientes", menu=menu_clientes)


    menu_vendas = ttk.Menu(tmenu, tearoff=0)
    menu_vendas.add_command(label="Vendas", command=lambda:trocaFrameVenda(frameUsuario))
    tmenu.add_cascade(label="Vendas", menu=menu_vendas)



    root.config(menu=tmenu)

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
    # janelaConsulta.geometry("1200x700")
    # janelaConsulta.resizable(False,False)

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
    const.root.mainloop()
    return 

def vConsultaClientes(root):

    def pesquisar():
        nome = entry_nome.get()
        idade = entry_idade.get()
        cpf = entry_cpf.get()
        cidade = entry_cidade.get()
        telefone = entry_telefone.get()
        sexo = entry_sexo.get()
        
        exibir_resultados(pesquisar_clientes_no_banco_dados(nome, idade, cpf, cidade, telefone, sexo))

    def exibir_resultados(resultados):
        # Criação da janela de exibição dos resultados
        janela_resultados = Toplevel(janelaConsulta)
        janela_resultados.title("Resultados da pesquisa")
        janela_resultados.geometry("1200x700")
        janela_resultados.resizable(False,False)
        z=10

        # Exibir cada registro retornado pela pesquisa
        for registro in resultados:
            # Criação do frame para conter o botão e os detalhes do registro
            frame_registro = Frame(janela_resultados)
            frame_registro.place(x=10, y=z)
            z+=40
          

            # Função para capturar o registro selecionado
            def selecionar_registro(registro):
                messagebox.showinfo("Registro selecionado", f"Registro selecionado: {registro}")

            # Botão para selecionar o registro
            botao_selecao = Button(frame_registro, text="Selecionar", command=lambda r=registro: selecionar_registro(r))
            botao_selecao.pack(side=LEFT)

            # Detalhes do registro
            detalhes_registro = f"ID: {registro[0]} Nome: {registro[1]} Idade: {registro[2]} CPF: {registro[3]} Endereço: {registro[4]} Cidade: {registro[5]}CEP: {registro[6]}\nTelefone: {registro[7]} Email: {registro[8]} Sexo: {registro[8]} Compras Feitas: {registro[8]}"
            label_detalhes = Label(frame_registro, text=detalhes_registro)
            label_detalhes.pack(side=LEFT)
    
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

    # Label e campo de entrada para cidade
    label_cidade = Label(janelaConsulta, text="Cidade:")
    label_cidade.pack()
    entry_cidade = Entry(janelaConsulta)
    entry_cidade.pack()

    # Label e campo de entrada para telefone
    label_telefone = Label(janelaConsulta, text="Telefone:")
    label_telefone.pack()
    entry_telefone = Entry(janelaConsulta)
    entry_telefone.pack()

    # Label e campo de entrada para sexo
    label_sexo = Label(janelaConsulta, text="Sexo:")
    label_sexo.pack()
    entry_sexo = Entry(janelaConsulta)
    entry_sexo.pack()

    # Botão de pesquisa
    button_pesquisar = Button(janelaConsulta, text="Pesquisar", command=pesquisar)
    button_pesquisar.pack()

    # Iniciar a janela principal
    #root.mainloop()

    return 

def vLogin(root):

    global FrameTotalLogin
    

    paddingtextoY= 29
    paddingelementoY = 50
    comecoX = 508
    comecoY =290


    FrameTotalLogin = ttk.Frame(root,height=700,width=1200)
    const.FrameTotalLogin = FrameTotalLogin
    FrameTotalLogin.pack()


    s = ttk.Style()
    s.configure('TFrame',foreground='#3b7cd1')

    #s.configure('SB.TFrame',background="#3b7cd1")

    # s.configure('Frame1.TFrame', background='#3b7cd1')
    FrameLogin =  ttk.Frame(FrameTotalLogin,height=330,width=350,bootstyle="light") 
    FrameLogin.place(x=435,y=210)
    
    splash=image=ttk.PhotoImage(name='logo',file=PATH / 'logo.png')
    limage=ttk.Label(FrameTotalLogin, image=splash)
    limage.place(x=480,y=comecoY-185)
   

    #Definindo título da janela
    root.title("BRUTUS - Identificação")
    
    # Labels
    
    label_username = ttk.Label(FrameTotalLogin, text="Nome de usuário:",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_username.place(x=comecoX,y=comecoY)
    
    
    #label_username.pack()

    # Entrada de nome de usuário
    entry_username = ttk.Entry(FrameTotalLogin,width=30)
    entry_username.place(x=comecoX,y=comecoY+paddingtextoY)
    comecoY+=paddingtextoY+paddingelementoY
    #entry_username.pack()

    # Label
    label_password = ttk.Label(FrameTotalLogin, text="Senha:",font=("Helvetica",10),bootstyle=("INVERSE","LIGHT"))
    label_password.place(x=comecoX,y=comecoY)
    comecoY+=paddingtextoY
    #label_password.pack()

    # Entrada de senha
    entry_password = ttk.Entry(FrameTotalLogin, show="*",width=30)
    entry_password.place(x=comecoX,y=comecoY)
    comecoY+=paddingelementoY

    # Botão de login
    button_login = ttk.Button(FrameTotalLogin, text="Login",command=lambda:ctrl.ctlrLoginESenha(entry_username.get(),entry_password.get()))
    button_login.place(x=comecoX+70,y=comecoY)
    
    #button_login.pack() -- pack centraliza
    const.inputLogin = entry_username.get()
    const.inputSenha = entry_password.get()


    # Label para exibir resultado
    global label_result
    label_result = ttk.Label(FrameTotalLogin, text="",bootstyle=("INVERSE","LIGHT"),font=("Helvetica",10))
    label_result.place(x=comecoX+53,y=comecoY+50)

    # Iniciar a janela principal
    const.root.mainloop()
    return 

def vCadastroCliente(root):

    def cadastra():
        nome = entry_nome.get()
        idade = entry_idade.get()
        cpf = entry_cpf.get()
        endereco = entry_endereco.get()
        cidade = entry_cidade.get()
        cep = entry_cep.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        sexo = entry_sexo.get()

        Mensagem(cadastrar_cliente_banco_dados(nome, idade, cpf, endereco, cidade, cep, telefone, email, sexo))
            
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
    button_cadastrar = Button(janelaConsulta, text="Cadastrar",command=cadastra)
    button_cadastrar.pack()

    # Iniciar a janela principal
    const.root.mainloop()


    return

def vCadastroCarro(root):

    def cadastra():
        chassi = entry_chassi.get()
        cor = entry_cor.get()
        km = entry_km.get()
        ano = entry_ano.get()
        modelo = entry_modelo.get()
        custo = entry_custo.get()
        preco = entry_preco.get()
        qt = entry_qt.get()

        Mensagem(cadastrar_veiculo_banco_dados(chassi, cor, km, ano, modelo, custo, preco, qt))
        
    #Definindo nova janela TopLevel
    janelaConsulta = Toplevel(root)
    janelaConsulta.grab_set()
    janelaConsulta.title("BRUTUS - Cadastro de veículos")
    janelaConsulta.geometry("1200x700")
    janelaConsulta.resizable(False,False)

    # Label e campo de entrada para chassi
    label_chassi = Label(janelaConsulta, text="Chassi:")
    label_chassi.pack()
    entry_chassi = Entry(janelaConsulta)
    entry_chassi.pack()

    # Label e campo de entrada para cor
    label_cor = Label(janelaConsulta, text="Cor:")
    label_cor.pack()
    entry_cor = Entry(janelaConsulta)
    entry_cor.pack()

    # Label e campo de entrada para km
    label_km = Label(janelaConsulta, text="KM:")
    label_km.pack()
    entry_km = Entry(janelaConsulta)
    entry_km.pack()

    # Label e campo de entrada para ano
    label_ano = Label(janelaConsulta, text="Ano:")
    label_ano.pack()
    entry_ano = Entry(janelaConsulta)
    entry_ano.pack()

    # Label e campo de entrada para modelo
    label_modelo = Label(janelaConsulta, text="Modelo:")
    label_modelo.pack()
    entry_modelo = Entry(janelaConsulta)
    entry_modelo.pack()

    # Label e campo de entrada para custo
    label_custo = Label(janelaConsulta, text="Custo:")
    label_custo.pack()
    entry_custo = Entry(janelaConsulta)
    entry_custo.pack()
    
    # Label e campo de entrada para preco
    label_preco = Label(janelaConsulta, text="Preço:")
    label_preco.pack()
    entry_preco = Entry(janelaConsulta)
    entry_preco.pack()

    # Label e campo de entrada para quantidade
    label_qt = Label(janelaConsulta, text="Quantidade:")
    label_qt.pack()
    entry_qt = Entry(janelaConsulta)
    entry_qt.pack()

    # Botão de cadastrar
    button_cadastrar = Button(janelaConsulta, text="Cadastrar", command=cadastra)
    button_cadastrar.pack()

    # Iniciar a janela principal
    #root.mainloop()

    return



def consultarClientes():
    # Lógica para abrir a janela de consulta de clientes
    print("Opção: Consultar Clientes")
    vConsultaClientes(const.root)

def consultarVeiculo():
     # Lógica para abrir a janela de consulta de veículo
    print("Opção: Consultar Veículo")
    vConsultaCarros(const.root)


def exibir_opcao(opcao):
    label_opcao.config(text=f"Opção selecionada: {opcao}")

def ExibePainelMensagemMeio(mensagem):

    msgframe= ttk.Frame(const.root,height=200,width=300)
    msgframe.place(x=492,y=260)
    md = ttk.dialogs.dialogs.MessageDialog(f"{mensagem}",buttons=['OK'],parent=msgframe)
    md.show()
    msgframe.destroy()
    msgframe.hidden=0


def janelaPrincipal(root):
    #const.telaSaida=0
    #global FrameTotalPrincipal
    FrameTotalPrincipal = ttk.Frame(root,height=700,width=1200)
    const.FrameTotalPrincipal=FrameTotalPrincipal


    FrameTotalPrincipal.pack()

    # raiz = Toplevel(root)
    # raiz.geometry(f"1200x700+{root.winfo_x()}+{root.winfo_y()}")

   
    print("Pagina saida %d",const.telaSaida)
    if const.telaSaida==0 or const.telaSaida==-1:
        ExibePainelMensagemMeio("Bem vindo Admin.")



    ## criacao  Menu ---------
    const.telaSaida=1
    CriaMenuPrincipal() # passando a tela atual


    

    #---- Iniciar a construcao da janela principal do meio com informacoes
    
    # s = ttk.Style()
    # s.configure('TFrame',foreground='#3b7cd1')
    # s.configure('SB.TFrame',background="#3b7cd1")
    # s.configure('Frame1.TFrame', background='#3g7cd1')

    
    global valorVenda

    sf = ttk.Style()
    sf.configure('TFrame')
    sf.configure('SB.TFrame',background='#f5f6f7')

    FrameTopo = ttk.Frame(const.FrameTotalPrincipal,height=180,width=730,style='SB.TFrame') #height=160,width=730
    FrameTopo.place(x=230, y =80)
    #bootstyle=("iNVERSE","light")

    LTotalVenda = ttk.Label(const.FrameTotalPrincipal, text= "Total de vendas:",foreground='#3b7cd1',background='#f5f6f7',font=("Helvetica",22))
    LTotalVenda.place(x=300, y =150)


    valorVenda=ctrl.ConsultaValorTotalBanco()
    p1= str(valorVenda//1000)
    p2= p1+'.000' 
    fvalorVenda=f'{p2}'+",00"

    #print(p2)

    LValorVenda = ttk.Label(const.FrameTotalPrincipal, text= f'{fvalorVenda}',background='#f5f6f7',font=("Helvetica",22))
    LValorVenda.place(x=700, y =150)


    load1 =ttk.PhotoImage(name='maintopo',file=PATH / 'imgprincipalmeiotopo.png')
    load1= load1.subsample(4)

    icontopo=Label(const.FrameTotalPrincipal,image=load1)
    icontopo.place(x=145,y=75)

    load2=ttk.PhotoImage(name='mainbaixo',file=PATH / 'imgprincipalmeiobaixo.png')
    load2= load2.subsample(4)
    imgbaixo = Label(FrameTotalPrincipal,image=load2)
    imgbaixo.place(x=145,y=320)




    FrameBaixo = ttk.Frame(const.FrameTotalPrincipal,height=280,width=730,style="SB.TFrame") #height=160,width=730
    FrameBaixo.place(x=230, y =320)

    LVendedores = ttk.Label(const.FrameTotalPrincipal, text= "Vendedores",foreground='#3b7cd1',background='#f5f6f7',font=("Helvetica",14))
    LVendedores.place(x=300, y =355)

    lvendedores=ctrl.ConsultaVendedores()
    montaTabela(280,410,lvendedores)


    const.root.mainloop()

    return 

def testeJanelas(root,janela):


    ## criacao  Menu ---------
    FrameTotalPrincipal = ttk.Frame(root,height=700,width=1200)
    const.FrameTotalPrincipal=FrameTotalPrincipal
    FrameTotalPrincipal.pack()


    const.telaSaida=0

    #CriaMenuPrincipal() # passando a tela atual
    
    if janela==5:
        trocaFrameVenda(const.FrameTotalPrincipal)



    const.root.mainloop()


    return

def ExibeStatusLoginSucesso(ntext):
    label_result.config(text=ntext)
    return


def trocaFrameVenda(frame):

  
    try:
        frame.pack_forget()
    except:
        print("Erro ao encontrar o frame de saida da troca de janela")
        return

    vVendas(const.root)
    return 

def trocaFrameCadastrarVenda():

    frame = encontraSaida
    try:
        frame.pack_forget()
    except:
        print("Erro ao encontrar o frame de saida da troca de janela")

    vVenda(const.root)
    return 

def trocaFrameCsonsultarVenda():

    frame = encontraSaida
    try:
        frame.pack_forget()
    except:
        print("Erro ao encontrar o frame de saida da troca de janela")

    vVenda(const.root)
    return 

def encontraSaidaFrame(isaida):
    # recebe o ido frame
    #retorna o frame do usuario

    if isaida == 0: #login
        print("Estou vindo da tela 0 - Login")
        return const.FrameTotalLogin

    if isaida == 1: # cadastro principal
        print("Estou vindo da tela 1 - Principal")
        return const.FrameTotalPrincipal
    if isaida == 2:  # consulta veiculos
        print("Estou vindo da tela 2")
        return 

    if isaida == 3:  # cadastro carros
        print("Estou vindo da tela 3")
        return 

    if isaida == 5:  # consulta carros
        print("Estou vindo da tela 4")
        return 

    if isaida == 0: #vendas
        print("Estou vindo da tela 5")
        return 

    return 

def trocaFramePrincipali(saida): #apaga a tela passada 
    
    if saida==0: # vindo do login

        ExibeStatusLoginSucesso("Usuario Validado")
        frame=const.FrameTotalLogin  #ok vindo do login
        frame.pack_forget() 
        janelaPrincipal(const.root)

    elif saida==1: # vindo do principal, dela mesma
        #recarrega para atualizar
        print("Recarreguei - Saindo de principal")
        return

    elif saida==3:
        
        return 

    elif saida==4:  
        return 
    
    elif saida==5:  
        print("Saindo de Vendas")
        frame=const.FrameTotalVendas
        frame.pack_forget() 
        janelaPrincipal(const.root)

        return 

    else:
        return 

    return 

def ExibeStatusLogin(ntext):

    label_result.config(text=ntext)
    
    return

def Mensagem(cod):

    if cod == 0:
        messagebox.showinfo("Cadastro realizado!","Cadastro feito com sucesso!")

    if cod == 1:
        messagebox.showinfo("Erro","O nome deve conter apenas letras e espaços, com no máximo 100 caracteres.")

    if cod == 2:
        messagebox.showinfo("Erro","A idade deve ser um número inteiro entre 18 e 120.")

    if cod == 3:
        messagebox.showinfo("Erro","A idade deve ser um número inteiro.")

    if cod == 4:
        messagebox.showinfo("Erro","O CPF deve ser um numero inteiro.")
   
    if cod == 5:
        messagebox.showinfo("Erro","O CPF deve conter exatamente 11 dígitos numéricos.")
        
    if cod == 6:
        messagebox.showinfo("Erro","CEP deve ser um número inteiro.")

    if cod == 7:
        messagebox.showinfo("Erro","O CEP deve conter exatamente 8 dígitos numéricos.")

    if cod == 8:
        messagebox.showinfo("Erro","Telefone deve ser um número inteiro.")

    if cod == 9:
        messagebox.showinfo("Erro","O telefone deve conter no máximo 11 caracteres.")

    if cod == 10:
        messagebox.showinfo("Erro","Preencha todos os campos corretamente!")

    if cod == 11:
        messagebox.showinfo("Erro","O chassi deve conter apenas letras e espaços, com no máximo 100 caracteres.")

    if cod == 12:
        messagebox.showinfo("Erro","A cor deve conter apenas letras e espaços, com no máximo 100 caracteres.")

    if cod == 13:
        messagebox.showinfo("Erro","Km deve conter entre 1 e 7 dígitos numéricos.")

    if cod == 14:
        messagebox.showinfo("Erro","KM deve ser um número inteiro.")

    if cod == 15:
        messagebox.showinfo("Erro","Ano deve ter no maximo 4 digtos.")

    if cod == 16:
        messagebox.showinfo("Erro","Ano deve ser um número inteiro.")

    if cod == 17:
        messagebox.showinfo("Erro","O modelo deve conter apenas letras e espaços, com no máximo 100 caracteres.")

    if cod == 18:
        messagebox.showinfo("Erro","Custo deve conter entre 1 e 7 dígitos numéricos.")

    if cod == 19:
        messagebox.showinfo("Erro","Custo deve ser um número inteiro.")

    if cod == 20:
        messagebox.showinfo("Erro","Preco deve conter entre 1 e 7 dígitos numéricos.")

    if cod == 21:
        messagebox.showinfo("Erro","Preco deve ser um número inteiro.")

    if cod == 22:
        messagebox.showinfo("Erro","Quantidade deve conter entre 1 e 7 dígitos numéricos.")

    if cod == 23:
        messagebox.showinfo("Erro","Quantiade deve ser um número inteiro.")




def MainView(root):


    #print("Tela de Login criada : 1")
    
    vLogin(root)

    return 





