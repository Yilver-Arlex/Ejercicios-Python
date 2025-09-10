############################################ Entrada de información y manejo de tipos con input() ################################################

### Pide tu nombre y muestralo ###

my_name = str(input("Mi nombre es: "))
print(my_name)

### Pide tu edad y muéstrala. ###

my_age = int(input("Mi edad es: "))
print(my_age)

### Pide un número y muéstralo multiplicado por 2. ###

number = int(input("Ingresa un numero, el cual se multiplicara por 2: "))
print(f"{number} X 2 = {number * 2}")

### Pide dos números y muéstralos sumados. ###

numbers = (input("Ingresa 2 numero separados por comas: "))
numbers_list = [int(num) for num in numbers.split(",")] # Se le coloca un , en split para indicar que desde ese pundo separara la cadena de texto
print(numbers_list)
print(f"La suma entre {numbers_list[0]} y {numbers_list[1]} es igual a: {numbers_list[0] + numbers_list[1]}")

### Pide una palabra y muéstrala en mayúsculas. ###

word_upper = input("Escribe un palabra:")
print(word_upper.upper())

### Pide un número flotante y muéstralo como entero. ###

number_float = float(input("Escribe un numero decimal: "))
print(f"El numero {number_float} ahora se conviertio en un entero: {int(number_float)}")

### Pide un número entero y muéstralo como flotante. ###

number_interger = float(input("Escribe un numero entero: "))
print(f"El numero {number_interger} ahora se conviertio en un flotante: {float(number_interger)}")

### Pide tu nombre y tu edad y muéstralos juntos en una frase. ###

print(f"My nombre es {my_name} y mi edad es {my_age}")

### Pide un número y verifica si es mayor que 10. ###

number = int(input("Ingresa un numero mayor que diez: "))
if number >= 10:
    print(f"El numero {number} es mayor que 10")
else: 
    print(f"El numero {number} es menor que 10")

### Pide dos números y muestra cuál es mayor. ###

numbers2 = input("Ingresa 2 numeros separados por comas: ")
numbers_list1 = [int(numb) for numb in numbers2.split(",")]
print(f"El numero mas grande es {max(numbers_list1)}")
