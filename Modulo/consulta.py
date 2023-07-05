from conexaoBd import *
con = connector.connect(host='localhost', database='brutus', user='root', password='')

def pesquisar_no_banco_dados(modelo, chassi, cor, km, preco, ano):
    # Criação do cursor para executar comandos SQL
    
    
    cursor = con.cursor()


    # Construção da consulta SQL com base nos campos preenchidos
    consulta = "SELECT * FROM carros WHERE 1=1"
    valores = []

    if modelo:
        consulta += " AND modelo = %s"
        valores.append(modelo)
    if chassi:
        consulta += " AND chassi = %s"
        valores.append(chassi)
    if cor:
        consulta += " AND cor = %s"
        valores.append(cor)
    if km:
        consulta += " AND km = %s"
        valores.append(km)
    if preco:
        consulta += " AND preco = %s"
        valores.append(preco)
    if ano:
        consulta += " AND ano = %s"
        valores.append(ano)

    # Execução da consulta no banco de dados
    cursor.execute(consulta, valores)

    # Obter os resultados da consulta
    resultados = cursor.fetchall()

    # Fechamento do cursor e da conexão com o banco de dados
    cursor.close()
        

    # Exibir os resultados em uma nova janela
    return resultados


def exibe_Resultados_Busca(resultado):
    #print(resultado)
    for x in resultado:
        print(x)
    #print(resultado)
    return


def consulta_pesquisa_usuario(inplogin, inpsenha):

    cursor= con.cursor()
   
    query=f"SELECT * FROM usuarios WHERE login='{inplogin}' and senha='{inpsenha}' " 
    #print(query)
    try:
        cursor.execute(query)

    except:
        print('--> Excecao Conexao')
        

    resultado = cursor.fetchall()
    exibe_Resultados_Busca(resultado)

    #fechamento conexao
    cursor.close()
       
    return resultado


def consulta_pesquisa_totalvendas():

    cursor= con.cursor()
   
    query=f"SELECT * FROM vendas" 
    #print(query)
    try:
        cursor.execute(query)

    except:
        print('--> Excecao Conexao')
        

    resultado = cursor.fetchall()
    exibe_Resultados_Busca(resultado)

    #fechamento conexao
    cursor.close()


    return resultado


def consulta_pesquisa_vendedores():

    cursor= con.cursor()
   
    query=f"SELECT * FROM usuarios where conta = 'vendedor'" 
    #print(query)
    try:
        cursor.execute(query)

    except:
        print('--> Excecao Conexao')
        

    resultado = cursor.fetchall()
    #exibe_Resultados_Busca(resultado)

    #fechamento conexao
    cursor.close()

    return resultado

#consulta_pesquisa_usuario('admin', 'admin')
#consulta_pesquisa_totalvenda()
consulta_pesquisa_vendedores()