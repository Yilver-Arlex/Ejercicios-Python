##################################################### Operaciónes matematicas ########################################################

### Suma 2 números. ###

number1, number2 = 34, 54
print(f"La suma entre {number1} y {number2} es igual a: {number1 + number2}")

### Resta 2 números. ###

number1, number2 = 54, 34
print(f"La resta entre los numeros {number1} y {number2} es igual a: {number1 - number2}")

### Multiplica 3 números. ###

number1, number2, number3 = 3, 5, 2
print(f"{number1} X {number2} X {number3} = {number1 * number2 * number3}")

### Divide 10 entre 2. ###

divicion = 10 / 2
print(f"La divición: 10 / 2 es igual a {divicion}")

### Calcula el resto de dividir 10 entre 3. ###

resto_de_una_division = 10 % 3
print(f"El resto entre la división es: {resto_de_una_division}")

### Eleva 2 a la potencia 4. ###

elevacion = 2 ** 4
print(f"2 elevado a la potencia de 4: {elevacion}")

### Calcula la raíz cuadrada de 25 con **0.5. ###

raiz_cuadrada_de_25 = 25 ** 0.5
print(f"La raiz cuadrada de 25 es: {raiz_cuadrada_de_25}")

### Usa math.sqrt() para la raíz de 36. ###

import math
print(f"La raiz cuadrada de 36 es: {math.sqrt(36)}")

### Calcula el promedio de 4, 8, 10. ###

numbers = 4, 8, 10
print(f"El promedio de {numbers} es: {(sum(numbers)) / len(numbers)}")

### Redondea 3.14159 a 2 decimales. ###

valor = 3.15159
print("Valor {:.2f}".format(valor)) # {}: lo que hay dentro de aqui es la platilla del formato, averigualo un poco porque es un poco complejo

