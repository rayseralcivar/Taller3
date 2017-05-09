def delPar(lista):
    for i in lista:
        if lista.index(i)%2 == 0:
            lista.remove(i)
    print(lista)


a = 0
b = 0
lista = [1, -2, 3, -2, 4, 7, 0, -4, -3]


delPar(lista)


print("lista original:", lista)
for i in lista:
    if i < a:
        l = lista.index(i)
        print ("se va a eliminar el elemento",i,"con indice",l)
        lista.remove(i)
        lista.insert(l, b)
print("nueva lista:", lista)

l=0
for m in lista:
    if m > l:
        l = m
print("el numero mayor es,",l)



a = 0
b = 0
lista2 = [1, -2, 3]
delPar(lista2)


print("lista original:", lista2)
for i in lista2:
    if i < a:
        l = lista2.index(i)
        print ("se va a eliminar el elemento",i,"con indice",l)
        lista2.remove(i)
        lista2.insert(l, b)
print("nueva lista:", lista2)

l=0
for m in lista2:
    if m > l:
        l = m
print("el numero mayor es,",l)




a = 0
b = 0
lista3 = [55, 9, -3, 60, 99, -4,-5, 6, 7, 88, 65, 4, -12, 20, 30, -40, 15, -43, 50, 12, 30, 33, -23, 15]
delPar(lista3)


print("lista original:", lista3)
for i in lista3:
    if i < a:
        l = lista3.index(i)
        print ("se va a eliminar el elemento",i,"con indice",l)
        lista3.remove(i)
        lista3.insert(l, b)
print("nueva lista:", lista3)

l=0
for m in lista3:
    if m > l:
        l = m
print("el numero mayor es,",l)
