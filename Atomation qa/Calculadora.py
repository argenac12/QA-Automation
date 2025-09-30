#calculadora

#calculadora con funciones

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
     raise ValueError ('Error: no se puede dividir por cero')
    return a // b

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def calculadora_simple(operacion , a , b):

    if operacion == 'sumar':
        return sumar(a,b)
    elif operacion == 'restar':
        return restar(a,b)
    elif operacion == 'dividir':
        return dividir(a,b)
    elif operacion == 'multiplicar':
        return multiplicar(a,b)
    else:
        return KeyError('operacion NO valida')

print(calculadora_simple('multiplicar', 1391, 4))


