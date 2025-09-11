####################### Tuplas ##################################

### Crea una tupla con 3 elementos.

my_tuple = (3, "Hola", 5.5, False)
print(type(my_tuple))

### Accede al primer elemento de la tupla.

print(f"Es es el primer elemento de la tupla: {my_tuple[0]}")

### Muestra el último elemento.

print(f"Este es el ultimo elemento de una la tupla: {my_tuple[-1]}")

### Cuenta cuántas veces aparece un valor.

my_tuple = [4, 3, 3, 2, 6, 7, 2, 5, 4, 4, 3, 4, 4, 9, 5]
value = 4
count = 0
for i in my_tuple:
    if i == 4:
        count += 1

print(f"El valor {value} aprace en la tupla un total de: {count} veces")

### Encuentra el índice de un valor.

print(f"El numero 9 esta ubicado en el indice: {my_tuple.index(9)}")

### Convierte la tupla en lista.

my_tuple = (3, 4.8, "Hola", False)
my_tuple_to_my_list = list(my_tuple)
print(f"my tuple ahora es una lista: {type(my_tuple_to_my_list)}")

### Convierte una lista en tupla.

my_list = [4, 6.2, True, "Holas"]
my_list_to_my_tuple = tuple(my_list)
print(f"my list ahora se convirtio en una tuple: {type(my_list_to_my_tuple)}")

### Desempaqueta la tupla en variables.

my_tuple = (1, 4, 7, 3, "hola")
a, b, c, d, e = my_tuple
print(a)
print(b)
print(c)
print(d)
print(e)

### Crea una tupla con un solo elemento.

single_value_tuple = 8, # Hay que ponerle una coma al final para que lo detecte como iterable
print(type(single_value_tuple))

### Une dos tuplas.

