######################################################## Manejo de cadenas de texto ########################################################

### Imprime tu nombre en pantalla. ###
my_name = "Yilver Arlex"
print(my_name)

### Guarda una frase en una variable e imprímela en mayúsculas. ###

phrase = "Esto es un gran inicio"
print(phrase.upper())

### Cuenta cuántas letras tiene tu nombre usando len(). ###

my_name = "Yilver Arlex Jovel Angarita"
my_name = "".join(my_name.split()) # split(): separa las cadenas de texto en partes, y las devuelve como una lista. "".join(): join puede unir cadenas de textos en este caso unio las cadenas de la lista, la separación puede tener en el medio algo, se puede poner dentro de las "comillas", si no tiene nada no tendra separación y quedara pegada
print(len(my_name))

### Reemplaza la palabra "perro" por "gato" en la frase "Tengo un perro" ###

# Mi solción inicial
phrase = "Tengo un perro"
phrase_list = phrase.split()
phrase_list[-1] = "Gato"
print(" ".join(phrase_list))

# IA solución

phrase = "Tengo un perro"
print(phrase.replace("perro", "Gato")) # Replace(): remplasa solo partes en especificas de cadenas, y de listas pero con listas de compresión

### Extrae los 5 primeros caracteres de "Python es genial". ###

phrase = "Python es genial"
print(phrase[0:5])


### Une las palabras "Hola" y "Mundo" con un espacio en medio. ###

words = "Hola", "Mundo"
print(" ".join(words))

### Verifica si la palabra "Python" está en la frase "Me gusta Python". ###

# Hecho por mi
phrase = "Me gusta Python"
try:
    if phrase.index("Python"):
        print(f"La palabra \"Python\" si esta en la frase {phrase}")
except:
    print("Error")

# IA hecho:

phrase = "Me me gusta Python"

if "Python" in phrase:
    print(f"La palabra Pyton estaba en la palabra {phrase}")
else:
    print(f"La palabra Python si esta")


### Invierte la cadena "Hola".###
word = "Hola"
print(word[::-1])

### Separa la frase "rojo,verde,azul" en una lista por comas. ###

color_phrase = "rojo, verde, azul"
print(color_phrase.split(","))

### Une la lista ["rojo", "verde", "azul"] en una sola cadena separada por guiones. ###

color_list = ["rojo", "verde", "azul"]
print("-".join(color_list))
