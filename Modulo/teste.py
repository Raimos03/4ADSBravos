from mysql import connector
import tkinter as tk
import mysql


con = connector.connect(host='localhost', database='brutus', user='root', password='')

def exibir_resultados(resultados): 
    # Criação da janela de exibição dos resultados
    janela_resultados = tk.Tk()
    janela_resultados.title("Resultados da pesquisa")
        
    # Criação de uma área de texto para exibir os resultados
    resultados_text = tk.Text(janela_resultados)
    resultados_text.pack()

    # Preencher a área de texto com os resultados
    if resultados:
        for resultado in resultados:
            print( f"ID: {resultado[0]}\nChassi: {resultado[1]}\nCor: {resultado[2]}\nKm: {resultado[3]}\nAno: {resultado[4]}\nModelo: {resultado[5]}\nCusto: {resultado[6]}\nPreço: {resultado[7]}\nQuantidade: {resultado[8]}\n")
    else:
            print("Nenhum resultado encontrado.")

modelo = ""
chassi = ""
cor = "Branco"
km = 0
preco = 0
ano = 0

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
con.close()

# Exibir os resultados em uma nova janela
exibir_resultados(resultados)
print("terminou")
