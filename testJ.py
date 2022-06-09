import json

listajson = '{"nome":"flavio", "idade":3}'
print(type(listajson))
listadict = json.loads(listajson) #load -> pega string do JSON e joga pra DICT
print(type(listadict))
print(listadict['nome'] + '\n' + str(listadict['idade']))
listaconv = json.dumps(listadict) #dumps -> pega DICT e joga pra String JSON
#pega dict e joga para JSON o acento não funciona corretamente
print(type(listaconv))
print(listaconv)

listajson2 = {"nome": "jefferson", "idade": 25} #é um dict
conv2 = json.dumps(listajson2) #string
print(type(conv2))
lista = ["lay", "you", "down"]
print(type(lista))
print(lista)
conv3 = open('test.json', 'r')
lista2 = json.load(conv3) #Carrega um IO para converter em DICT
print (type(lista2))
lista.append("lara")
print(lista2["nome"])
print(lista2)
conv3.close()
conv4 = open('test2.json', 'w')
json.dump(["luciano", "antunes", "gabriela"], conv4)
conv4.close()
conv3 = open('test.json', 'w')
json.dump({"nome": "ismael", "idade": 15}, conv3)
conv3.close()
print('---------------------------------')
dict1 = {"nome": "daniel", "idade": 6}
print(dict1)
print("\n")
dict2 = {"nome": "artur", "idade": 7}
dict1.update(dict2)
print(dict1)
dict3 = {"nome", "nome2"}
dict4 = {"joao", "pedro"}
d = dict(zip(dict3, dict4))
print(d)
print('-------------------------------')
class Pessoa():
    nome = ""
    idade = None

obj1 = Pessoa()
obj1.nome = "roberto"
obj1.idade = 3

obj2 = Pessoa()
obj2.nome = "ana"
obj2.idade = 17

obj = obj1.__dict__ #conversão objeto para dicionário
objj = obj2.__dict__

var1 = json.dumps(obj)
var2 = json.dumps(objj)
dict5 = {var1, var2}
print(dict5)
list5 = [var1, var2]
print(list5)

print(type(obj1))
print(type(obj))


catch = list5[0]
json.loads(catch)
catch2 = json.dumps(catch)
print(catch2)












'''
Dumps -> utilizado para conversão de Dict para String JSON
Dump -> utilizado para subistituir JSON na variável de interesse que está
escrevendo no arquivo JSON

'''



