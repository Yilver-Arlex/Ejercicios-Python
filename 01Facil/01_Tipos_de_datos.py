##################################################### Tipos de datos ########################################################

### Declara una variable entera y otra flotante. ###

var_float =  1.4545
var_int = 4
print(type(var_float))
print(type(var_int))

### Convierte el número 5 a flotante. ###

var_int = 5
transform_to_float = float(var_int)
print(f"El entero {var_int} fue transformado a un float: {transform_to_float}")

### Convierte 3.14 a entero. ###

var_float = 3.14
transform_to_integer = int(var_float)
print(f"El numero flotante {var_float} fue transformado a un entero: {transform_to_integer}")

### Muestra el tipo de dato de la variable "hola". ###

greeting = "Hello"
print(type(greeting))

### Verifica si 5 es del tipo int usando isinstance(). ###

number = 5
print(isinstance(number, int)) # isinstance(); verifica si un valor es de una clase o un tipo de dato en especifico, si es correcto suelta un true si no suelta un false.

### Convierte el número 10 a cadena. ###

number = 10
transform_to_string = str(number)
print(type(transform_to_string))

### Convierte la cadena "45" a entero. ###

string_text = "45"
transform_to_integer = int(string_text)
print(type(transform_to_integer))

### Declara una variable booleana con valor True. ###

var_true = True
print(var_true)

### Verifica si 4.5 es flotante. ###

number = 4.5
print(isinstance(number, float))

### Cambia el tipo de dato de True a entero. ###

var_boolean = True
transform_to_float = float(var_boolean)
print(transform_to_float)
print(type(transform_to_float))
