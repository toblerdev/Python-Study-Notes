# RESUMEN DE LISTAS, APLICACIONES Y COMENTARIOS (CADA ITEM ESTA INDIVIDUALIZADO)

# Una lista en Python es como una “caja organizada” donde podés guardar distintos 
# objetos en un orden específico y tener la libertad de sacar, meter o cambiar cosas
# cuando quieras.

# CREAR UNA LISTA

# Una lista se define con corchetes [ ]
frutas = ["manzana", "banana", "pera"]

print(frutas)  # ['manzana', 'banana', 'pera']

# ACCEDER A ELEMENTOS

frutas = ["manzana", "banana", "pera"]

print(frutas[0])   # manzana  -> primer elemento
print(frutas[1])   # banana
print(frutas[-1])  # pera     -> último elemento

# MODIFICAR UN ELEMENTO

frutas = ["manzana", "banana", "pera"]

frutas[1] = "naranja"  
print(frutas)  # ['manzana', 'naranja', 'pera']

# AGREGAR ELEMENTOS

frutas = ["manzana", "banana"]

frutas.append("pera")  
# agrega al final
print(frutas)  # ['manzana', 'banana', 'pera']

frutas.insert(1, "uva")  
# inserta en la posición 1
print(frutas)  # ['manzana', 'uva', 'banana', 'pera']

# ELIMINAR ELEMENTOS

frutas = ["manzana", "banana", "pera"]

frutas.remove("banana")  
# elimina por valor
print(frutas)  # ['manzana', 'pera']

frutas.pop(0)  
# elimina por índice
print(frutas)  # ['pera']

frutas.clear()  
# borra todo
print(frutas)  # []

# RECORRER UNA LISTA

frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    print(fruta)  # imprime uno por uno


# LARGO DE LA LISTA

frutas = ["manzana", "banana", "pera"]

print(len(frutas))  # 3 

# SLICING (REBANADAS)

frutas = ["manzana", "banana", "pera", "uva", "melon"]

print(frutas[1:3])   # ['banana', 'pera'] -> desde índice 1 hasta 2
print(frutas[:2])    # ['manzana', 'banana']
print(frutas[2:])    # ['pera', 'uva', 'melon']
print(frutas[-2:])   # ['uva', 'melon']

# ORDENAR Y ORGANIZAR

numeros = [3, 1, 4, 2]

numeros.sort()  
print(numeros)  # [1, 2, 3, 4]

numeros.sort(reverse=True)  
print(numeros)  # [4, 3, 2, 1]


# OTRAS OPERACIONES UTILES

frutas = ["manzana", "banana", "pera"]

print("banana" in frutas)   # True
print("uva" not in frutas)  # True

# Concatenar
otras = ["melon", "sandia"]
todas = frutas + otras
print(todas)  # ['manzana', 'banana', 'pera', 'melon', 'sandia']

# Copiar lista
copia = frutas.copy()
print(copia)  # ['manzana', 'banana', 'pera']

# TIPS 
 
# - Permiten elementos duplicados y de distintos tipos.
# - Son mutables: podés cambiar, agregar o eliminar elementos.
# - Muy útiles con for, list comprehension y funciones como map(), filter().
# - Usá slicing [inicio:fin:paso] para copiar o recorrer parcialmente.
# - append() agrega 1 elemento, extend() agrega varios.
# - copy() o list() para clonar listas sin afectar la original.
# - len(lista) da la cantidad de elementos.
