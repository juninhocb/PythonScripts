class Chatbot():
    
    teste = 3
    
    def __init__(self, nome): #primeira função que irá rodar quando instanciar um objeto
        self.nome = nome
    
    def fala(self):   #tem que ter o self
        print('oi, meu nome é ' + self.nome)
        print(f'oi, meu nome é {self.nome}')


a = Chatbot('chat1')
a.fala()
print(a.teste)
a.teste = 5

b = Chatbot('chat2')
b.fala()
print(b.teste)
print(b.nome)
b.teste = 4
print(b.teste)

'''
self é a maneira do python saber qual dos chats bots ele está rodando

'''

