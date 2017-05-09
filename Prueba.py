def mayor(lista):
    for m in lista:
        l = m
    print(m)


def cambiar(lista, a, b):
    print("lista original:", lista)
    for i in lista:
        if i < a:
            l = lista.index(i)
            lista.remove(i)
            lista.insert(l, b)
    print("nueva lista:", lista)


a = 0
b = 0
lista = [1, 2, 3, -2, 4, 7, 3, -4, 3]
cambiar(lista, a, b)
mayor(lista)