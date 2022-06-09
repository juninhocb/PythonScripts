import json

def carregaArq(nome):
    memoria = open(nome+'.json', 'r')
    lista = json.load(memoria)
    print(lista)

def criaArq (nome):
    memoria = open(nome + '.json', 'w')
    lista.append(nome)
    json.dump (lista, memoria)

lista = [] #lista de nomes a serem inseridos no arquivo JSON
nome = input("Insira o nome que desejas armazenar no arquivo JSON: ")
criaArq(nome)
carregaArq(nome)





