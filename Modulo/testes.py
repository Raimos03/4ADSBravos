import modValidacaoInput as vld

#teste de validacao de entrada ( nome)
'''

for x in ['pedro 2','pedrohenrique2','pedro',' pedro ','pedrohenr','thiago policarpo santos9','thiagopolicarposantos','pedro henrique', 'thiago policarpo santos']:
    entrada=x
    #input("Digite o nome:")
    tipo="input  nome"
    print("\n Tipode Teste: {} \n Entrada: {} \n Resposta {}  \n ".format(tipo,entrada,vld.vNome(entrada)))

'''