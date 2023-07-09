from view import*
import view as vw
from model import* 
import constantes as const
from utilidade import* 

def ctrlCadastraVenda(lvalores):
    return modCadastraVeiculos(lvalores)

def ConsultaValorTotalBanco():
    return  modCalculaValorVendas()

def ConsultaVendedores():
    return modConsultaVendedores()

def ConsultaClientes():
    return modConsultaClientes()

def ctlrLoginESenha(login,senha): #usa o model para validar
    
    print(login,senha)

    r= modValidaUsuario(login, senha)
    const.tipoUsr=r

    #print("Tipo usr",const.tipoUsr)

    if (r==1 or r==2 or r==3):
        vw.trocaFramePrincipali(0)
        
    else:
        print("Usuario nao autorizado ou nao existente\nTente Novamente.")
        vw.ExibeStatusLogin("Usuario Invalido")

    return 



def IniciaApp(r):

    rLogin=const.tipoUsr # 1 2 ou 3 dependendo do usuario. 0 para erro. 
    inputLogin=const.inputLogin
    inputSenha=const.inputSenha
    usuarioA=const.usuarioAut



    MainView(r) #- ok



    #janelaPrincipal(r)
    #testeJanelas(r,5)

    #vVendas(r)

    #vCadastroCarro(r)
    #vConsultaClientes(r)
    #vCadastroCliente(r)
    
    #r.mainloop()
    return 

    