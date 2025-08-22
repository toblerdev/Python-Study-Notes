# RESUMEN DE BUCLES

# Un bucle permite repetir instrucciones varias veces sin tener que escribir el mismo código una y otra vez.

# Resumen teórico:

# Los bucles sirven para repetir tareas.
# for → recorre secuencias o un rango definido.
# while → repite mientras la condición sea verdadera.
# Control extra: break, continue, pass.
# Se pueden anidar bucles.

# En Python hay principalmente dos tipos:
# for → Se usa cuando sabemos cuántas veces queremos repetir.
# while → Se usa cuando queremos repetir hasta que se cumpla (o deje de cumplirse) una condición.

# BUCLE for 
# Se usa para recorrer una secuencia (lista, cadena, rango, etc.).

# Ejemplo 1: recorrer una lista
frutas = ["manzana", "banana", "pera"]
for fruta in frutas:
    print(fruta)  # Imprime cada fruta

# Ejemplo 2: usar range()
for i in range(5):  
    print(i)  # Imprime 0, 1, 2, 3, 4

# Ejemplo 3: range con inicio y fin
for i in range(2, 6):
    print(i)  # Imprime 2, 3, 4, 5

# BUCLE while 
# Se ejecuta mientras la condición sea verdadera

# Ejemplo 1: contador
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Importante, si no se actualiza es un bucle infinito

# Ejemplo 2: pedir input hasta que el usuario escriba 'salir'
entrada = ""
while entrada != "salir":
    entrada = input("Escribe algo (o 'salir'): ")
    print("Ingresaste:", entrada)


# PALABRAS CLAVES UTILES DENTRO DE BUCLES

# break → corta el bucle antes de que termine
for i in range(10):
    if i == 5:
        break
    print(i)  # Imprime 0,1,2,3,4

# continue → salta a la siguiente iteración
for i in range(5):
    if i == 2:
        continue
    print(i)  # Imprime 0,1,3,4 (salta el 2)

# pass → no hace nada, sirve como "relleno"
for i in range(3):
    pass  # Aquí no pasa nada, solo mantiene la estructura


# BUCLE ANIDADO 

# Ejemplo: imprimir combinaciones
for i in range(3):      # Bucle externo
    for j in range(2):  # Bucle interno
        print(i, j)
# Salida: 
# (0,0), (0,1), (1,0), (1,1), (2,0), (2,1)

# TIPS 

# - for recorre secuencias (listas, cadenas, rangos, etc.).
# - while se usa cuando no sabés cuántas iteraciones habrá.
# - break corta el bucle, continue salta a la siguiente iteración.
# - else en un bucle se ejecuta solo si no hubo break.
# - range(inicio, fin, paso) es muy usado con for.
# - Evitá bucles infinitos (while True) sin condición de salida.
# - Usá enumerate() en for si necesitás índice y valor a la vez.
