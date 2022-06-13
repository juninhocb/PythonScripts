import paho.mqtt.client as mqtt
import time

'''
Para fazer os testes das conexões, precisa ligar um MQTT broker e monitorá-lo

Neste exemplo utilizei o mosquitto verbose (endereço de rede local) para testes e consegui obter as informações pelo log do CMD

'''
class Client ():
    
    def __init__(self,idt, name):
        self.__idt = idt
        self.__name = name
   
    def __call__ (self):
        self.__conectar()
  
    def __conectar (self):
        
        if isConnected(self.__name):
            print(f'Cliente {self.__name} já está conectado com o Broker!')
        else:
            try:
                self.client = mqtt.Client(self.__name)
                self.__idt = self.client
                self.client.on_connect= on_connect
                self.client.connect('127.0.0.1', 1883)
                self.client.loop_start()
                listCli.append(self.client)
            except:
                print('Broker recusou a conexão ou não está \'online\' ')
        
    def disconnect (self, index):
        
        self.obj = listCli[int(index)]
        self.name = listCli[int(index)]._client_id.decode()
        listCli.pop(index)
        print(f'desconectando o cliente! \n nome: {self.name}')
        self.obj.loop_stop()
        self.obj.disconnect()
        self.__idt = ''
    
    def getID (self):
        
        return self.__idt
    
    def getName(self):
        
        return self.__name
        
#funções
def on_connect(client, userdata, flags, rc, properties=None):
    
    if rc != 0:
        print(f'Problema ao conectar-se com o broker RC = {rc}')
    else:
        print(f'Sucesso ao conecater-se RC = {rc}')

def listConnected():
    
    print('-------------------------')
    if listCli == []:
        print('Não há clientes conectados!')
    else:
        print('Clientes conectados \n')
        for i in listCli:
            print(i._client_id.decode() + '\n')
    
    print('-------------------------')
    

def isConnected (name):
    
    for i in listCli:
        if i._client_id.decode() == name:
            return True
    return False

def addClient (name):
    
    concVarName = 'c'+'name'
    concVarName = Client ('', name)
    concVarName()
    addName.append(concVarName)

def verifyName (name):
    index = -1
    for i in listCli:
        if i._client_id.decode() == name:
            index = index + 1
            return index
        else:
            index = index + 1
    print (f'Cliente {name} não conectado')
    return index 
    
#variáveis
listCli = []
addName = []

switch = 0

#objetos 
c1 = Client('', 'joao')

c2 = Client ('', 'ana')

c3 = Client ('', 'roberto')

while(int(switch) != 5):
    time.sleep(2)
    print("Tamanho da Lista: " + str(len(listCli)))
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    switch = input('Digite 1 Conectar-se, 2 Desconectar-se, 3 Listar conectados, 5 Sair! \n')   
    
    if switch == '1':
        conn = input ('Digite 1 Conectar Joao, 2 Conectar Ana ou 3 Conectar Roberto ou 4 Conectar um cliente a sua escolha \n')
        if conn == '1':
            c1()
        elif conn == '2':
            c2()
        elif conn == '3':
            c3()
        elif conn == '4':
            newName = input('Digite o nome do novo cliente que deseja conectar: ')
            if isConnected(newName):
                print('Este nome já esta sendo usado por um cliente, favor usar outro!')
            else:
                addClient(newName)
                
            
        else:
            print('Valor inválido, tente novamente \n')
            
    elif switch == '2':
        key = True
        indice = 0
        count = 0
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        conn = input ('Digite 1 Desconectar João, 2 Desconectar Ana, 3 Desconectar Roberto, 4 Desconectar Outro  \n')
        if conn == '1':
            for i in listCli:
                if i == c1.getID():
                    c1.disconnect (count)
                    key = False
                    break
                else:
                    count = count + 1
                    if i == listCli [-1]:
                        print("Cliente 1 desconetado")
                        break
            if key:
                print('Cliente 1 já está desconectado')
            
        
        elif conn == '2':
            for i in listCli:
                if i == c2.getID():
                    c2.disconnect (count)
                    key = False
                    break
                else:
                    count = count + 1
                    if listCli[-1]:
                        print("Cliente 2 desconectado")
                        break
            if key:
                print("Cliente 2 desconectado")
    
        elif conn == '3':
            for i in listCli:
                if i == c3.getID():
                    c3.disconnect (count)
                    key = False
                    break
                else:
                    count = count + 1
                    if listCli[-1]:
                        print("Cliente 3 desconectado")
                        break
            if key:
                print("Cliente 3 desconectado")
            
        elif conn == '4':
            nameDel = input('Digite o nome do cliente que quer desconectar: ')
            index = verifyName(nameDel)
            if isConnected(nameDel):
                addName[index].disconnect (index)
                addName.pop(index)
            else:
                print(f'Cliente {nameDel} não está conectado')
            '''
            if index != -1:
                for i in listCli:
                    if i == addName[index].getID():
                        addName[index].disconnect (index)
                        addName.pop(index)
                        key = False
                        break
                    else:
                        count = count + 1
                        if addName[-1]:
                            print(f"Cliente {nameDel} desconectado ")
                            break
                if key:
                    print(f'Cliente com nameDel: {nameDel}')
            else:
                print(f'Cliente {nameDel} não conectado')
        '''
        else:
            print('Valor inválido, tente novamente')
    
    elif switch == '3':
        listConnected()   
     
    elif switch == '5':
        print('Bye!')
        
    else:
        print('Digite um valor válido! \n')
        
    
    
    
    



    