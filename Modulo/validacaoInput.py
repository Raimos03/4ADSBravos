'''
Modulo que faz a validação de entrada do usuário

'''
'''
x usuario 
    apenas letras
    
senha
    alphanuumerico (sem caractere especial)


nome (cliente, nome do funcionario)
cpf ( cliente, funcionario)
residencia
valor(float 0,00)
telefone
email

'''

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

    












