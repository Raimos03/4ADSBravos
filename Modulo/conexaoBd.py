from mysql import connector

#Conexão com o banco 
con = connector.connect(host='localhost', database='brutus', user='root', password='')

#Verificando conexão
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado com sucesoo")
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados", linha)

#fechando o banco
#if con.is_connected():
#   cursor.close()
#    con.close()
#    print("Conexão com o banco encerrada")