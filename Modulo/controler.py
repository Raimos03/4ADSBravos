from view import*
from model import* 
from constantes import* 
from utilidade import* 

def ctlrLoginESenha(login,senha): #usa o model para validar

    r= modValidaUsuario(login, senha)

     

    return usuario



def IniciaApp(r):

    rLogin=const.tipoUsr # 1 2 ou 3 dependendo do usuario. 0 para erro. 
    inputLogin=const.inputLogin
    inputSenha=const.inputSenha
    usuarioA=const.usuarioAut


    #MainView(r)

    if (tipoUsr==0 or tipoUsr==1 or tipoUsr==2):
        janelaPrincipal(r)

    else:
        print("Usuario nao autorizado ou nao existente\nTente Novamente.")
        #cria janela de usuario invalido
    
    
    

    janelaPrincipal(r)
    #vConsultaCarros(r)
    #vCadastroCarro(r)
    #vConsultaClientes(r)
    #vCadastroCliente(r)
    
  
    return 

    