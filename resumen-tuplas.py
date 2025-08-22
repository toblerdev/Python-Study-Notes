# RESUMEN TUPLAS

# ¿QUE ES UNA TUPLA?

# Una tupla es una colección de elementos ordenados e inmutables (no se pueden modificar después de creadas).
# Se utilizan para agrupar datos que no deben cambiar.
# Se parecen a las listas, pero la diferencia es que no permiten modificación.
# Características principales:
# Ordenadas → los elementos mantienen la posición en la que fueron creados.
# Inmutables → no se pueden cambiar, agregar ni eliminar elementos después de definirse.
# Permiten elementos duplicados.
# Se definen con paréntesis ( ) en lugar de corchetes [ ].

# CASOS DE USO COMUN

# Datos que no deben modificarse, como coordenadas geográficas (lat, long)
# Valores constantes agrupados (ej: colores RGB → (255, 0, 0))
# Mejor rendimiento que las listas en búsquedas y almacenamiento

# EJEMPLOS PRACTICOS 

# Crear una tupla
tupla1 = (10, 20, 30, 40)
print(tupla1)  # (10, 20, 30, 40)

# Tupla con distintos tipos de datos
tupla2 = ("Hola", 25, 3.14, True)
print(tupla2)  # ('Hola', 25, 3.14, True)

# Acceder a un elemento por índice
print(tupla1[0])  # 10

# Slicing (subconjunto de la tupla)
print(tupla1[1:3])  # (20, 30)

# Verificar si un elemento está en la tupla
print(20 in tupla1)  # True
print(50 in tupla1)  # False

# Longitud de la tupla
print(len(tupla1))  # 4

# Tupla con un solo elemento (se necesita coma al final)
tupla3 = (5,)
print(type(tupla3))  # <class 'tuple'>

# Concatenar tuplas
nueva_tupla = tupla1 + tupla2
print(nueva_tupla)
# (10, 20, 30, 40, 'Hola', 25, 3.14, True)

# Repetir tupla
print(tupla1 * 2)  # (10, 20, 30, 40, 10, 20, 30, 40)

# Convertir lista a tupla
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print(tupla_convertida)  # (1, 2, 3)

# Desempaquetado de tupla
a, b, c, d = tupla1
print(a, b, c, d)  # 10 20 30 40


# TIPS 
# - Son inmutables (no se pueden modificar después de creadas).
# - Usalas cuando necesitás que los datos sean fijos y no cambien.
# - Admiten elementos repetidos y de cualquier tipo.
# - Ocupan menos memoria que listas (más eficientes).
# - Podés desempacar tuplas: a, b, c = (1, 2, 3).
# - Si tienen un solo elemento, deben llevar coma: (5,)
# - Son hashables: pueden usarse como claves en diccionarios.
