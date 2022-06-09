import json

class IncluiArqTxt ():
    def __init__(self, nome):
        self.nome = nome
    
    def incluir(self):
        arquivo = open ('arquivo.txt', 'w')
        arquivo.write(self.nome)
        arquivo.close()
        main()
        
def lerArq ():
    arquivo = open('arquivo.txt', 'r')
    print(arquivo.read())
    arquivo.close()
    main()

def addJson ():
    global lista
    memoria = open('memoria.json', 'r')
    lista = json.load(memoria)
    n = input('favor, inserir o nome que deseja adicionar ao JSON: ')
    lista.append(n)
    print(lista)
    memoria = open ('memoria.json', 'w')
    json.dump(lista, memoria)
    memoria.close()
    main()

def verJson():
    ver = open('memoria.json', 'r')
    listaVer = json.load(ver)
    print(listaVer)
    ver.close()
    main()

def main ():
    val = input('Digite: \n 1 Escrever nome no arquivo \n 2 Ler o que está no arquivo \n 3 Escrever no arquivo JSON \n 4 Ler arquivo JSON \n Qualquer outro valor para sair: ')
    print(f'valor digitado {val}')
    if val == '1':
        n = input('favor, inserir o nome que deseja adicionar ao arquivo TXT: ')
        print(f'nome digitado: {n}')
        add = IncluiArqTxt (n)
        add.incluir()
    elif val == '2':
        lerArq()
    elif val == '3':
        addJson()
    elif val == '4':
        verJson()
    else:
        print('Nos vemos, Até logo!!!')
n = ""
lista = []
main()


    