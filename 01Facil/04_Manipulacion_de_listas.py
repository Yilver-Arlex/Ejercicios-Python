################################################# Manipulación de listas ##############################################################

### Crea una lista con 5 elementos. ###

this_is_a_list = [1, 2, 3, 4, 5]
print(this_is_a_list)

### Agrega un elemento al final de la lista. ###

this_is_a_list = [1, 3, 5, 6, 1, "f"]
this_is_a_list.append("Este es el ultimo elemento de la lista")
print(this_is_a_list)

### Inserta un elemento en la posición 2. ###

my_list = [1, 3, 5, 2, False, "Hola"]
my_list.insert(1, "Esto es algo")
print(my_list)

### Elimina un elemento por su valor. ###

the_best_players = ["Sasueta", "Zlatam", "Sharawi", "Roberto Carlos","Madareta", "Zoomer", "Lewandosky"]
the_best_players.remove("Roberto Carlos")
print(the_best_players)

### Elimina un elemento por su índice. ###

my_list = ["Hola", 43, 34, True, "Esto sera eliminado", 3.45]
del my_list[4]
print(my_list)

### Ordena la lista de menor a mayor. ###

my_list = [3, 2, 6, 12]
my_list_order = []

while my_list: # Mientras la lista este llena
    minimo = min(my_list)
    my_list_order.append(minimo)
    my_list.remove(minimo)

print(my_list_order)

### Ordena la lista de mayor a menor. ###

my_list = [3, 2, 6, 12]
my_list_order = []

while my_list: # Mientras la lista este llena
    maximo = max(my_list)
    my_list_order.append(maximo)
    my_list.remove(maximo)

print(my_list_order)

### Encuentra el valor máximo de la lista. ###



### Encuentra el valor mínimo de la lista. ###

### Cuenta cuántas veces aparece un valor en la lista. ###

