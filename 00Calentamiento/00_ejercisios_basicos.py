################### Ejercicios Basicos para desperta ###########################

### Crea una clase Persona con nombre y edad Agrega un método saludar() que imprima un saludo con su nombre.###

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludar(self):
        print(f"Hola {self.name}, tienes {self.age} ¿verdad?")

persona1 = Persona("Sasueta", 15)

persona1.saludar()


### Crea una clase Foco con atributo encendido y métodos encender() y apagar(). ###

class Foco:
    def __init__(self):
        self.encendido = True

    def preguntar_encendido(self):
        if self.encendido:
            print("Esta el foco encendio")
        else:
            print("El foco esta apagado")

    def encender(self):
        if self.encendido:
            print("Ya estaba encendido el foco")
        else:
            self.encendido = True
            print("El Foco ha sido ensendido")

    def apagar(self):
        if not self.encendido:
            print("Ya estaba Apagado el foco")
        else:
            self.encendido = False
            print("El Foco ha sido Apagado")

foco1 = Foco() # Incializamos la clase foco

foco1.preguntar_encendido()
foco1.apagar()
foco1.apagar()
foco1.preguntar_encendido()
foco1.encender()
foco1.encender()

### Crea una clase CuentaBancaria con saldo y métodos depositar() y retirar().

class BankAccount:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.activada = False
        self.mi_dinero = 0
        
    def activar_cuenta(self):
        if not self.activada:
            self.activada = True
            print("La cuenta fue activada")
        else:
            print("La cuenta ya estaba activada")

    def desactivar_cuenta(self):
        if self.activada:
            self.activada = False
            print("La cuenta fue desactivada")
        else:
            print("La cuenta ya estaba desactivada")

    def depositar(self, cantidad):
        if self.activada:
            self.mi_dinero += cantidad
            print(f"Se depositaron {cantidad}$, tu dinero total es de {self.mi_dinero}$")
        else:
            print(f"No tiene cuenta activa")

    def retirar(self, cantidad):
        if self.activada:
            if not self.mi_dinero - cantidad <= 0:
                self.mi_dinero -= cantidad
                print(f"Se retiraron {cantidad}$, tu dienro total es de {self.mi_dinero}$")
            else:
                print("No te alcanza viejo es demasiado dinero de acuerdo con tu cantidad de dinero")
        else:
            print("No tienes una cuenta activa")

    def ver_mi_dinero(self):
        if self.activada:
            print(f"La cuenta tiene un total de {self.mi_dinero}$")
        else:
            print("No tienes una cuenta activa")

cuenta1 = BankAccount("Jermo", "103423333")
cuenta2 = BankAccount("Ossareta", "334234233")

cuenta1.ver_mi_dinero()
cuenta1.activar_cuenta()
cuenta1.ver_mi_dinero()
cuenta1.depositar(3434)
cuenta1.desactivar_cuenta()
cuenta1.activar_cuenta()
cuenta1.retirar(567)
cuenta1.ver_mi_dinero()
print("\nSeparación entre los 2 ejemplo\n")
cuenta2.activar_cuenta()
cuenta2.depositar(56000)
cuenta2.retirar(90000000)
cuenta2.retirar(3422)
cuenta2.ver_mi_dinero()



### Crea clases Motor y Auto donde el auto use un motor para encender o apagar.

class Motor:
    def __init__(self):
        self.activado = False

    def encender(self):
        if not self.activado:
            self.activado = True
            print("Ha sido encendido")
        else:
            print("Ya estaba encendido")

    def apagar(self):
        if self.activado:
            self.activado = False
            print("Ha sido apagado")
        else:
            print("Ya estaba apagado")

    def saber_estado(self):
        if self.activado:
            print("Esta encendido")
        else:
            print("Esta Apagado")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def encender_carro(self):
        print("Encendiendo el carro")
        self.motor.encender()

    def apagar_carro(self):
        print("Apagando el carro")
        self.motor.apagar()

    def estado(self):
        self.motor.saber_estado()


mi_carro = Carro()

mi_carro.encender_carro()
mi_carro.encender_carro()
mi_carro.apagar_carro()
mi_carro.apagar_carro()
mi_carro.estado()


### Crea clases Estudiante y Curso que se relacionen e inscriban estudiantes.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inscrito = []

    def inscripcion_a_un_curso(self, curso):
        self.inscrito.append(curso)

    def mi_info(self):
        print(f"Yo {self.name} estoy inscrito a:")
        for c in self.inscrito:
            print(f"- {c.name_del_curso}")


class Curso:
    def __init__(self, name_del_curso):
        self.name_del_curso = name_del_curso
        self.list_students = []

    def inscripcion(self, student):
        self.list_students.append(student)
        student.inscripcion_a_un_curso(self)

    def studiantes_inscritos(self):
        print(f"Los estudiantes inscritos al curso de {self.name_del_curso} son:")
        for s in self.list_students:
            print(f"- {s.name}")

# Cursos
c1 = Curso("Matematicas")
c2 = Curso("Programación")
c3 = Curso("Gestión Empresariasl")

# Estudiantes
s1 = Student("Jose", 23)
s2 = Student("Xelra", 32)
s3 = Student("Da", 19)
s4 = Student("Yolver", 17)

# Inscripcion

c1.inscripcion(s1)
c2.inscripcion(s2)
c3.inscripcion(s3)
c2.inscripcion(s4)
c1.studiantes_inscritos()
c2.studiantes_inscritos()
c3.studiantes_inscritos()
s1.mi_info()


### Crea tienda que guarda productos con nombre y precio, y muestra su lista completa.

class Producto:
    def __init__(self, name_p, precio):
        self.name_p = name_p
        self.precio = precio
        self.pertenece = []

class Tienda:
    def __init__(self):
        self.productos = []

    def introducir_producto(self, producto):
        self.productos.append(producto)
        print(f"Se agrego {producto.name_p} con un precio de {producto.precio}$")

    def retirar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Se retiro {producto.name_p}")
        else:
            print(f"No habia {producto.name_p}, nada que retirar")
        
    def mostrar_productos(self):
        print("Los productos con los que cuenta la tienda son:")
        for c in self.productos:
            print(f"- {c.name_p} a {c.precio}$")

tienda = Tienda()

p1 = Producto("Peras", 34)
p2 = Producto("Manzanas", 22)
p3 = Producto("Ramillete de Uva", 30)
p4 = Producto("Banano", 12)

tienda.introducir_producto(p1)
tienda.introducir_producto(p2)
tienda.introducir_producto(p3)
tienda.introducir_producto(p4)

tienda.retirar_producto(p3)
tienda.retirar_producto(p3)

tienda.mostrar_productos()

### Crea autores con libros asociados; al crear un libro, agréguelo automáticamente al autor.

class Autor:
    def __init__(self, name):
        self.name = name
        self.libros_del_autor = []

    def recopilacion_libros(self, libro):
        self.libros_del_autor.append(libro)

    def mostrar_libros_del_autor(self):
        print(f"Los libros escritos por {self.name}:")
        for l in self.libros_del_autor:
            print(f"- {l.name_libro}")

class Libro:
    def __init__(self, name_libro, autor):
        self.name_libro = name_libro
        self.autor = autor
        autor.recopilacion_libros(self)

    def mostrar_autor(self):

        print(f"El autor de {self.name_libro} es {self.autor.name}")

a1 = Autor("Carleto Ancheloti")
a2 = Autor("Sasueta")

l1 = Libro("Eu misteir", a1)
l2 = Libro("La gloria", a2)
l3 = Libro("Liri Bori", a1)
l4 = Libro("La Losi", a2)
l5 = Libro("Eu misteir Two", a1)
l6 = Libro("La gloria return black", a2)

a1.mostrar_libros_del_autor()
a2.mostrar_libros_del_autor()

l3.mostrar_autor()
l6.mostrar_autor()
