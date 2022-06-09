from collections import Counter

with open ("text.txt", 'r') as t:
    text = t.read()
    
def func1(text):
    
    chars = []
    quantity = []
    
    for c in text:
        if not c in chars:
            chars.append(c)
            quantity.append(1)
        
        else:
            index = chars.index(c)
            quantity[index] += 1
        
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    
    return d

def func2(text):
    chars = set() #set só aceita caracteres distintos declaração análoga {} porém, preisa-se de valores 
    for c in text:
        chars.add(c)
    chars = list(chars)
    quantity = [text.count(c) for c in chars] #conceito de list comprehensions 
    d = {}
    for i in range (len(chars)):
        d[chars[i]] = quantity[i]
    
    return d

def func3(text):
    chars = list({c for c in text})
    quantity = [text.count(c) for c in chars]
    d = {}
    for i in range (len(chars)):
        d[chars[i]] = quantity[i]
    return d

def func4(text):
    chars = list({c for c in text})
    quantity = [(c,text.count(c)) for c in chars]
    return dict(quantity)

def func5(text):
    quantity = [(c, text.count(c)) for c in set(text)]
    return dict(quantity)

def func6(text):
    return {c: text.count(c) for c in set(text)}

def func7(text):
    return Counter(text).most_common(7)  #mostra os mais comuns, E.G: os 7 mais comuns 
        
print(func7(text))