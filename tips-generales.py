# ==============================
# TIPS GENERALES DE PYTHON
# ==============================

# 📌 VARIABLES
# Son espacios en memoria donde se guarda información.
# No necesitan declarar tipo, Python lo detecta automáticamente.

x = 10          # entero (int)
y = 3.14        # número decimal (float)
name = "Adrián" # cadena de caracteres (str)
is_active = True # valor booleano (bool)

# type() permite conocer el tipo de dato
print(type(x))       # <class 'int'>
print(type(name))    # <class 'str'>


# 📌 TIPOS DE DATOS PRINCIPALES
# str   -> texto (cadenas de caracteres)
# int   -> números enteros
# float -> números decimales
# bool  -> True / False
# list  -> colecciones ordenadas y modificables
# tuple -> colecciones ordenadas, inmutables
# set   -> colecciones no ordenadas, sin duplicados
# dict  -> pares clave:valor (similar a un mapa o JSON)


# 📌 OPERADORES BÁSICOS
a, b = 10, 3

print(a + b)  # suma -> 13
print(a - b)  # resta -> 7
print(a * b)  # multiplicación -> 30
print(a / b)  # división -> 3.333...
print(a // b) # división entera -> 3
print(a % b)  # módulo -> 1
print(a ** b) # potencia -> 1000

# Comparación
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True


# 📌 ESTRUCTURAS DE CONTROL
# IF (condicional)
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a y b son iguales")
else:
    print("b es mayor que a")

# BUCLES
# for -> iterar sobre elementos
for i in range(5):
    print("Iteración", i)

# while -> se repite mientras se cumpla una condición
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1


# 📌 FUNCIONES
# Sirven para reutilizar código
def saludar(nombre):
    return f"Hola {nombre}!"

print(saludar("Adrián"))


# 📌 MANEJO DE ERRORES
try:
    numero = int("abc")  # esto falla
except ValueError:
    print("Error: no se pudo convertir a número")
finally:
    print("Bloque terminado")


# 📌 COLECCIONES (resumen rápido)
lista = [1, 2, 3]                  # lista
tupla = (4, 5, 6)                  # tupla
conjunto = {1, 2, 2, 3}            # set (guarda {1,2,3})
diccionario = {"clave": "valor"}   # diccionario

print(lista, tupla, conjunto, diccionario)


# 📌 STRINGS
texto = "Python"
print(texto.upper())   # "PYTHON"
print(texto.lower())   # "python"
print(texto[0])        # "P"
print(texto[-1])       # "n"
print(len(texto))      # longitud = 6


# 📌 TIP PRÁCTICO
# Usar print() para depurar y entender el flujo del programa
# Usar comentarios (#) para documentar
# Dividir el código en funciones y módulos para mantener orden
# Usar nombres descriptivos en variables
