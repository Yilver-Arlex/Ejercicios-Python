####################### Copiar listas sin compartir memoria con slicing ###################################

### Crea una lista de números.

my_list = [1, 3, 4, 5, 6, 7, 3]
print(my_list)

### Copia la lista con [:].

copy_list = my_list[:]
print(copy_list)

### Modifica la lista original y verifica que la copia no cambió.

my_list.insert(4, "añadi un nuevo valor")
del my_list[2]
print(f"Lista original: {my_list}, Copia de la lista: {copy_list}")

### Copia solo los primeros 3 elementos de una lista.

copy_list = my_list[:3]
print(copy_list)

### Copia los elementos desde el índice 2 hasta el final.

copy_list = my_list[2:]
print(copy_list)

### Copia la lista en orden inverso.

copy_list_inversed = my_list[::-1]
print(copy_list_inversed)

### Copia una sublista del índice 1 al 3.

copy_sublist = my_list[1:3] #Una sublista es parte de otra lista, conservando orden.
print(copy_sublist)

### Copia toda la lista y añade un elemento nuevo a la copia.

copy_list = my_list[:]
copy_list.insert(6, True)
print(copy_list)

### Verifica que id(lista1) != id(lista2) para listas copiadas.

my_list = [545, "Hola", True, 6.4]
copy_list = my_list[::]

if id(my_list) != id(copy_list):
    print(f"Las IDs son totalmente diferente, entre la copia y la original")
else:
    print("Son totalmente iguales los valores entre el original y la copia")
### Haz una copia y cámbiale un valor sin afectar a la original.

my_list = [3, 5, 2.6, "hola", False]
copy_list = my_list[:]
copy_list[1] = True
print(f"La Original: {my_list}, La copia: {copy_list}")