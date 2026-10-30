def somarmultiplosnumeros(lista):
    total = 0
    for numero in lista:
        total = total + numero
    return total

def multiplicarmultiplosnumeros(lista):
    total = 1
    for numero in lista:
        total = total * numero
    return total

def ehinteiro(numero):
    if isinstance(numero, int):
        return True
    elif isinstance(numero, float) and numero.is_integer():
        return True
    else:
        return False

def ehpar(numero):
    if ehinteiro(numero) == True:
        if numero % 2 == 0:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    lista_soma = [5, 10, 15]
    lista_misturada = [0.5, -4, 2]
    lista_mult = [-1, 3, 2.5]
    
    print(somarmultiplosnumeros(lista_soma))
    print(somarmultiplosnumeros(lista_misturada))
    print(multiplicarmultiplosnumeros(lista_mult))
    print(ehinteiro(10))
    print(ehinteiro(4.2))
    print(ehpar(8))
    print(ehpar(2.5))
