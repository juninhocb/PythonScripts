import json

def carregaArq():
    global lista
    memoria = open('save.json', 'r')
    lista = json.load(memoria)

def addArq (nome):
    memoria = open('save.json', 'w')
    lista.append(nome)
    print(lista)
    json.dump (lista, memoria)


lista = [] #lista de nomes a serem inseridos no arquivo JSON
nome = input("Insira o nome que desejas armazenar no arquivo JSON: ")
carregaArq()
addArq(nome)




