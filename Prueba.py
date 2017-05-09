def delPar(lista):
    for i in lista:
        if lista.index(i)%2 == 0:
            lista.remove(i)
    print(lista)


a = 0
b = 0
lista = [1, 2, 3, -2, 4, 7, 0, -4, 3]


delPar(lista)


print("lista original:", lista)
for i in lista:
    if i < a:
        l = lista.index(i)
        lista.remove(i)
        lista.insert(l, b)
print("nueva lista:", lista)

l=0
for m in lista:
    if m > l:
        l = m
print("el numero mayor es,",l)
