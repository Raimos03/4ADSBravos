from conexaoBd import *
from validacaoInput import *

con = connector.connect(host='localhost', database='brutus', user='root', password='')

def cadastrar_cliente_banco_dados(nome, idade, cpf, endereco, cidade, cep, telefone, email, sexo):

    tentar_registrar = valida_cadastro_clientes(nome, idade, cpf, endereco, cidade, cep, telefone, email, sexo)
    print (tentar_registrar)

    if tentar_registrar == 0:
        cursor = con.cursor()

        query = "INSERT INTO clientes (nome, idade, cpf, endereco, cidade, cep, telefone, email, sexo, qtCompras) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nome, idade, cpf, endereco, cidade, cep, telefone, email, sexo, 0)

        # Execute the query
        cursor.execute(query, values)

        # Commit changes to the database
        con.commit()

        # Close the cursor and database connection
        cursor.close()

        # Show a success message or perform any additional actions
        print("Cliente cadastrado com sucesso!")
        return 0
    
    else:
        return tentar_registrar
    

def cadastrar_veiculo_banco_dados(chassi, cor, km, ano, modelo, custo, preco, qt):

    tentar_registrar = valida_cadastro_veiculos(chassi, cor, km, ano, modelo, custo, preco, qt)

    print (tentar_registrar)

    if tentar_registrar == 0:
        cursor = con.cursor()

        query = "INSERT INTO carros (chassi, cor, km, ano, modelo, custo, preco, qt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (chassi, cor, km, ano, modelo, custo, preco, qt)

        # Execute the query
        cursor.execute(query, values)

        # Commit changes to the database
        con.commit()

        # Close the cursor and database connection
        cursor.close()

        # Show a success message or perform any additional actions
        print("Veiculo cadastrado com sucesso!")
        return 0
    
    else:
        return tentar_registrar