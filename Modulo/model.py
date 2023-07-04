"""
Implementacao da arquitetura do modulo e utilizacao da conexao
"""
from consulta import* 
from utilidade import*
import constantes as const

def modValidaUsuario(login, senha):

    tpResultadoBanco=consulta_pesquisa_usuario(login,senha) #sucesso retorna uma tupla
    #print(tpResultadoBanco)

    if(len(tpResultadoBanco)==0):
        return 0

    else:
        rid,rlogin,rsenha=tpResultadoBanco[0]

        if comparaS(rlogin,'admin')  and comparaS(rsenha,'admin'): #admin
            return 1

        elif (g in rologin):    #gerente
            return 2

        else:   #vendedor
            return 3

    return 