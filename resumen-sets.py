# RESUMEN SETS (CONJUNTOS)

# Un set es una colección no ordenada de elementos únicos.
# No permite elementos repetidos.
# Es mutable: puedes agregar o eliminar elementos, pero no se puede acceder por índice (porque no tiene orden).
# Se define con llaves { } o usando set().
#No se puede acceder por índice → si necesitas orden, usa lista o tupla.

# CARACTERISTICAS PRINCIPALES

# No ordenados → no tienen índice, no se pueden recorrer por posición.
# Elementos únicos → los duplicados se eliminan automáticamente.
# Mutables → se pueden agregar o quitar elementos, pero los elementos dentro deben ser inmutables (números, strings, tuplas, etc.).


# Crear un set
frutas = {"manzana", "banana", "pera"}
print(frutas)  # {'pera', 'banana', 'manzana'} -> el orden puede variar

# Set vacío
vacio = set()
print(vacio)  # set()

# Elementos duplicados se eliminan automáticamente
numeros = {1, 2, 2, 3, 4, 4}
print(numeros)  # {1, 2, 3, 4}

# Agregar elementos
frutas.add("uva")
print(frutas)  # {'pera', 'banana', 'manzana', 'uva'}

# Eliminar elementos
frutas.remove("banana")  # si no existe, da error
frutas.discard("kiwi")   # si no existe, no da error
print(frutas)

# Longitud del set
print(len(frutas))  # cantidad de elementos

# Verificar si un elemento está en el set
print("pera" in frutas)  # True
print("banana" in frutas)  # False

# Operaciones de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))        # {1, 2, 3, 4, 5, 6} -> unión
print(A.intersection(B)) # {3, 4} -> intersección
print(A.difference(B))   # {1, 2} -> elementos de A que no están en B
print(A.symmetric_difference(B)) # {1, 2, 5, 6} -> elementos en A o B pero no en ambos

# TIPS 

# - No admiten elementos duplicados.
# - Son desordenados: no tienen índices.
# - Muy buenos para eliminar duplicados rápidamente.
# - Se pueden hacer operaciones matemáticas: unión (|), intersección (&), diferencia (-).
# - add() agrega un elemento, update() agrega varios.
# - remove() da error si no existe, discard() no.
# - set() puede convertir listas en conjuntos para filtrar repetidos.
