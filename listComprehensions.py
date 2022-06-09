lista = []

for v in range (10):
    lista.append(v+1)
    
print(lista)

lista2 = []

for v in range (1,11):
    lista2.append(v)
    
print(lista2)

lista3 = [ v+1 for v in range (10)] #list comprehension
print(lista3)

lista4 = []

for v in 'sfisjdf':
    lista4.append(v)

print(lista4)

lista5 = [v for v in 'sifsdfjii' ]
print(lista5)

lista6 = []

for v in [1,2,3]:
    for b in [4,5,6]:
        lista6.append((v,b))

print(lista6)

lista7 = [(v,b) for v in [1,2,3] for b in [4,5,6]]
print(lista7)

lista8 = [(v,b)
          for v in [1,2,3]
          for b in [4,5,6]]
print(lista8)

lista9 = []
for v in [1,2,3]:
    for b in [4,5,6]:
        if v % 2 == 0:
            lista9.append((v,b))
        
print(lista9)

lista10 = [(v,b) for v in [1,2,3] for b in [4,5,6] if v % 2 == 0]
print(lista10)


lista11 = [(v,b) for v in [1,2,3] if v % 2 == 0 for v in [4,5,6]]
print(lista11)

lista12 =[[i for i in range (4)] for v in range(3)] 
print(lista12)

lista13 = [[i for i in range(4)] for v in range(3) if v % 2 == 0] 
print(lista13)

lista14 = [[i for i in range (4) if i % 2 == 0] for v in range(3)]
print(lista14)

