
#variable y tipo de datos 

#Nombre = "argenis"
#edad = 30
#altura = 1.83
#EsmayordeEdad = True

#entrada y salida de datos


#print( nombre )

#Ejemplo 2

#convertir tipos de datos


#print(type(AnioDeNacimiento))

#resultado = 4 + 2
#potencia = 2**2
#division = 10 // 5
#resto = 4 % 2

#result = 5 > 2



#puntuacion

#puntuacion = int(input ("ingrese una nota - (0-10)"))

#if puntuacion >= 9:
    #print ("excelente")
#elif puntuacion >= 8:
    #print ("bien")
#elif puntuacion >= 5:
    #print ("regular")
#else:
    #print("insuficiente")

###

#range (stop)
#range(star, stop) 2 - 11
#range(star, stop, step) 2 - 11 -- 2 


###


#for i in range(10, 11, 2):
   # print(i)

#for i in range(120):
    #if i == 100:
        #continue
    #print (i)



#clase 2-3
#i = 1

#while i <= 5:
    #print(i) 
    #i = i + 1

#listas 

#mi_lista = ['argentina', 200, True]
            #0, 1,2
#mi_lista.append(5000)
#mi_lista.insert(1, "Paises Bajos")
#print(mi_lista)

#tuplas
#mi_tupla = ("celeste", 200, "rojo")
#INMUTABLE

#mi_tupla[1] = 400

#print(mi_tupla)

#dicc
#persona = {
    #"nombre" : "jaime",
    #"apellido": "desconocido",
    #"edad": 34
#}

#print(persona.keys())
#print(persona.values())
#print(persona.items())

#listas2

#mi_lista = ['argentina', 200, True]

#for i in mi_lista:
    #print(i)

#funciones 

#def saludo( nombre ):
    #print(f'Hola {nombre}')

#saludo('omaira')
#saludo('Daniel')

#def saludo( nombre ):
    #return f'hola {nombre}'
#print(saludo('omaira'))



#def sumar(a, b):
    #return a + b

#def calculadora_simple(operacion , a , b):
    #if operacion == 'sumar':
        #return sumar(a,b)
    #else:
        #return 'operacion no valida'
#print(calculadora_simple('sumar', 1, 1))

#try:
    #resultado = 10 / 0
#except ZeroDivisionError as e:
    #print(f'error: {e}')    

persona = {
    'nombre' : 'Argenis', 
    'edad' : '30'
}

try:
    print(persona['nombre'])
except KeyError as e:
    print('la clave no existe')
    