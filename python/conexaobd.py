import mysql.connector 
from mysql.connector import errorcode

#Conexão com o banco de dados

class connectionDB():
    
    def __init__(self,database,password):
        
        self.__database = database
        self.__password = password
        self.connection = None
        self.cursor = None
        self.result = None
        
    def getDB(self):
        
        return self.__database

    def getPassword(self):
        
        return self.__password
    
    def getCursor(self):
        
        return self.cursor
    
    def commitBD(self):
        try:
            self.connection.commit()
            print('Commit realizado')
            return True
        except:
            print('Não foi possível realizar o commit')
            return False
        
        
    def connectDB(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',user='root',password=self.getPassword(),database=self.getDB())
            self.cursor = self.connection.cursor()
            print('Conexão com o BD estabelecida')

        except mysql.connector.Error as error:
            
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print('BD inexistente')
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Usuário ou senha inválida')
            else:
                print(error)
    
    def disconnectDB(self):
       if self.connection:
           self.connection.close()
           print('Conexão com o BD fechada')
                
    def consultBD(self,command):
        try:
            self.cursor.execute(command)
            self.result = self.cursor.fetchall()
        except:
            print('Não foi possível realizar a consulta')
            
    
        
        
    
    
    