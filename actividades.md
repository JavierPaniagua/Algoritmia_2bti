# Metodos comunes de str

## Cambios de mayusculas/minusculas
~~~
print(nombre.lower())       # pedro
print(nombre.capitalize())  # Pedro
print(nombre.title())       # Pedro (cada palabra en mayúscula)
print(nombre.swapcase())    # pEDRO
~~~
## Longitud y busqueda
~~~
print(len(nombre))                   # 5 (cantidad de caracteres)
print(nombre.startswith("Pe"))       # True
print(nombre.endswith("ro"))         # True
print(nombre.find("e"))              # 1 (posición donde aparece "e")
~~~
## Reemplazar y dividir
~~~
print(nombre.replace("Pedro", "Juan"))        # Juan
print(nombre.split("e"))                      # ['P', 'dro'] (divide por "e")
~~~
## Eliminar espacios
~~~
texto = "   Hola Pedro   "
print(texto.strip())   # "Hola Pedro"
print(texto.lstrip())  # "Hola Pedro   " (quita izquierda)
print(texto.rstrip())  # "   Hola Pedro" (quita derecha)
~~~
## Unir cadenas
~~~
letras = ["P", "e", "d", "r", "o"]
print("".join(letras))              # Pedro
print("-".join(letras))             # P-e-d-r-o
~~~
## Validaciones
~~~
print(nombre.isalpha())         # True (solo letras)
print("123".isdigit())          # True (solo números)
print("Pedro123".isalnum())     # True (letras y números)
print("   ".isspace())          # True (solo espacios)
~~~