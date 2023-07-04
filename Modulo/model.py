"""
Implementacao da arquitetura do modulo e utilizacao da conexao
"""
from consulta import* 
from utilidade import*

def modValidaUsuario(login, senha):

    tpResultadoBanco=consulta_pesquisa_usuario(login,senha)

    if(len(tuplalogin)==0):

        return 0;

    
    # else:
        
    #     if login  and senha : #admin


    #         return 1

    #     elif ():    #gerente



    #         return 2


    #      else:   #vendedor

    #         return 3


    return 