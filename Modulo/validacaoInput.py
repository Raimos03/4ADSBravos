import re

def vNome(input):
    #Retorna True or False
    #Tamanho minimo de 10 caracteres
    #Pelo menos um espaço

    if not input.replace(' ','').isalpha() :
        print('ERRO numero')
        return False

    if len(input)<10 : 
        print('ERRO tamanho')
        return False

    espaco = str.count(input,' ')
    if  espaco < 1 :
        print('ERRO espaco')
        return False

    return True  

    

def vNome(input):
    #Retorna True or False
    #Tamanho minimo de 10 caracteres
    #Pelo menos um espaço

    if not input.replace(' ','').isalpha() :
        print('ERRO numero')
        return False

    if len(input)<10 : 
        print('ERRO tamanho')
        return False

    espaco = str.count(input,' ')
    if  espaco < 1 :
        print('ERRO espaco')
        return False

    return True  


def valida_cadastro_clientes(nome, idade, cpf, endereco, cidade, cep, telefone, email, sexo):

    if nome and idade and cpf and endereco and cidade and cep and telefone and email and sexo:
       
        # Validação nome deve conter apenas letras e espaços, no máximo 100 caracteres
        if not re.match(r'^[a-zA-Z\s]{1,100}$', nome):
            print("O nome deve conter apenas letras e espaços, com no máximo 100 caracteres.")
            return 1

        # Validação da idade: Deve ser um número inteiro entre 1 e 99
        try:
            idade = int(idade)
            if idade < 1 or idade > 120:
                print("A idade deve ser um número inteiro entre 18 e 120.")
                return 2    
        except ValueError:
            print("A idade deve ser um número inteiro.")
            return 3

        #Validação CPF deve ser numero inteiro
        try:
            cpf = int(cpf)  
            cpf= str(cpf)
        except ValueError:
            print("CPF deve ser um número inteiro.")
            return 4
        
        # Validação do CPF: Deve conter 11 dígitos numéricos
        if not re.match(r'^\d{11}$', cpf):
            print("O CPF deve conter exatamente 11 dígitos numéricos.")
            return 5
        
        # Validação CEP deve ser número inteiro
        try:
            cep = int(cep)  
            cep = str(cep)
        except ValueError:
            print("CEP deve ser um número inteiro.")
            return 6
        
        # Validação do CEP: Deve conter 8 dígitos numéricos
        if not re.match(r'^\d{8}$', cep):
            print("O CEP deve conter exatamente 8 dígitos numéricos.")
            return 7

        #validação telefone deve ser numero inteiro
        try:
            telefone = int(telefone)  
            telefone = str(telefone)  
        except ValueError:
            print("Telefone deve ser um número inteiro.")
            return 8

        # Validação do telefone: No máximo 11 caracteres
        if len(telefone) > 11:
            print("O telefone deve conter no máximo 11 caracteres.")
            return 9
        
        return 0

    else:
        # validação de todos os campos preenchidos
        print("Preencha todos os campos corretamente!")
        return 10
    
def valida_cadastro_veiculos(chassi, cor, km, ano, modelo, custo, preco, qt):
    if chassi and cor and km and ano and modelo and custo and preco and qt:
       
        # Validação chassi deve conter apenas letras e espaços, no máximo 100 caracteres
        if not re.match(r'^[a-zA-Z\s]{1,100}$', chassi):
            print("O chassi deve conter apenas letras e espaços, com no máximo 100 caracteres.")
            return 11
        
        # Validação cor deve conter apenas letras e espaços, no máximo 100 caracteres
        if not re.match(r'^[a-zA-Z\s]{1,100}$', cor):
            print("A cor deve conter apenas letras e espaços, com no máximo 100 caracteres.")
            return 12

        
        try:
            km = int(km)
            km = str(km)
            # Validação da km Deve ter entre 1 e 7 digitos
            if not re.match(r'^\d{1,7}$', km):
                print("Km deve conter entre 1 e 7 dígitos numéricos.")
                return 13
        except ValueError:
            # Validação da km Deve ser um número inteiro
            print("KM deve ser um número inteiro.")
            return 14

        try:
            ano = int(ano)
            ano = str(ano)
            if not re.match(r'^\d{1,4}$', ano):
                print("Ano deve ter no maximo 4 digtos.")
                return 15
        except ValueError:
            # Validação da ano Deve ser um número inteiro
            print("Ano deve ser um número inteiro.")
            return 16

        # Validação modelo deve conter apenas letras e espaços, no máximo 100 caracteres
        if not re.match(r'^[a-zA-Z\s]{1,100}$', modelo):
            print("O modelo deve conter apenas letras e espaços, com no máximo 100 caracteres.")
            return 17
        
        try:
            custo = int(custo)
            custo = str(custo)
            # Validação custo Deve ter entre 1 e 7 digitos
            if not re.match(r'^\d{1,7}$', custo):
                print("Custo deve conter entre 1 e 7 dígitos numéricos.")
                return 18
        except ValueError:
            print("Custo deve ser um número inteiro.")
            return 19

        try:
            preco = int(preco)
            preco = str(preco)
            # Validação preco Deve ter entre 1 e 7 digitos
            if not re.match(r'^\d{1,7}$', preco):
                print("Preco deve conter entre 1 e 7 dígitos numéricos.")
                return 20
        except ValueError:
            # Validação preco Deve ser um número inteiro
            print("Preco deve ser um número inteiro.")
            return 21

        try:
            qt = int(qt)
            qt = str(qt)
            # Validação preco quantidade ter entre 1 e 7 digitos
            if not re.match(r'^\d{1,7}$', qt):
                print("Quantidade deve conter entre 1 e 7 dígitos numéricos.")
                return 22
        except ValueError:
            # Validação quantidade Deve ser um número inteiro
            print("Quantidade deve ser um número inteiro.")
            return 23
        
        return 0

    else:
        # validação de todos os campos preenchidos
        print("Preencha todos os campos corretamente!")
        return 10
    












