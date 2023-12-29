import mysql.connector 
from mysql.connector import errorcode

#Conexão com o banco de dados

def connectionDB(self):
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='',database='estoque')
        print('Conexão com o BD estabelecida')

    except mysql.connector.Error as error:
        
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print('BD inexistente')
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuário ou senha inválida')
        else:
            print(error)

    #else:
    #    connection.close()
    