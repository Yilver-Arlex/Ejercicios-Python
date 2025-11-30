############################## Ejercicios 50 de Logica#############################################

########################################## Calentamiento

### 1. Mostrar los numeros del 1 al 100 ###

for i in range(1, 101):
    print(f"- {i}")

### Mostrar los numeros pares del 1 al 100 ###

for i in range(1, 101):
    if i % 2 == 0: # se usa modulo %: si i es divisible entre 2 y el resultado de residuo es 0 imprime, solo son los numeros pares los que dan 0 al divirse por 2
        print(f"{i} Par")

# Mostrar la suma de los numeros del 1 al 50
# 1
suma = sum(range(1, 51))
print(f"La suma de los numeros del 1 al 50 es {suma}")
# 2

numeros = range(1, 51)
resultado = 0
for i in numeros:
    resultado += i
    print(f"+ {resultado}")

### Pedir un numero y decir si es positivo, negativo o cero ###

numero = 0

if numero < 0:
    print(f"El numero {numero} es negativo")
elif numero == 0:
    print(f"El numero {numero} es 0")
else:
    print(f"El numero {numero} es positivo")


### Pedir 2 numeros y mostrar el mayor ###

n1 = 34
n2 = 455

if n1 == n2:
    print(f"Los numeros {n1} y {n2} son iguales")
elif n1 < n2:
    print(f"{n1} es menor que {n2}")
else:
    print(f"{n1} es mayor que {n2}")


### Pedir un numero y generar la tabla de multiplicar del 1 al 10 ###

numero = 3

for n in range(1, 11):
    print(f"{numero} X {n} = {numero * n}")


### Verificar si un numero es par o impar ###

numero = 3

if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

### Contar cuantas vocales hay en una palabra ###

palabra = "traidor"
vocales = ["a", "e", "i", "o", "u"]
cantidad_de_vocales = 0

for vocal in palabra:
    if vocal in vocales:
        cantidad_de_vocales += 1

print(f"La palbra <<{palabra}>> tiene {cantidad_de_vocales} vocales")


### Invertir una palbra sin usar [::-1]

palabra = "sasueta"
c_l = len(palabra)
palabra_invertida = ""

for l in range(c_l):
    palabra_invertida += palabra[-l -1]

print(f"Palabra invertida: {palabra_invertida}")


### Contar cuantas veces aparece la letra a en un texto ###

texto = "Hola esto es un texto, es increible como todo llega hasta un punto sabes?, no se que mas decir, estoy improvisando para este ejercicio, Adios, hasta la proxima XD"
cantidad = 0

for t in texto:
    if t == "a":
        cantidad += 1

print(f"En el texto: --{texto}-- aparece un total de {cantidad} veces la letra A")


########################################## Logica Basica
