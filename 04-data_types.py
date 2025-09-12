# Tipos de datos
# String (cadenas de texto, texto)
nombre = "Pedro"
apellido = "Paniagua"
saludo = "Hola Mundo"

#int (enteros)
numero = 500
edad = 30
curso = 3

#float (Flotantes, Decimales)
decimal = 20.45
temperatura = 32.8

#Bool (Boleanos)
booleano = True
booleano_falso = False
is_gamer = True

#Datos especiales
#listas (arrays) (colección de algo, conjunto)
lista = [1,2,3]
lista_abc = ['a', 'b', 'c']

#Tupla - similar a lista
tupla = (1,2,3)

# Set - parece lista pero con atrito especiales
set_variable = {1, 2, 3}

# Diccionario
diccionario = {
    'hello': 'hola',
    'bye': 'adios',
}

informacion_persona = {
    'name' : 'Pedro',
    'age' : 30,
    
}

## ver tipo de dato
print(nombre)
print(type(nombre))

#otra variable
print(edad)
print(type(edad))

#que podemos hacer con la variable

print(nombre.upper())