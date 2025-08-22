# RESUMEN DICCIONARIOS

# Un diccionario es una colección no ordenada de pares clave-valor.
# Cada elemento se almacena como clave: valor.
# Las claves deben ser únicas e inmutables (strings, números, tuplas), mientras que los valores pueden ser de cualquier tipo.
# Se define con llaves {}

# # CARACTERISTICAS PRINCIPALES 

# No ordenado → hasta Python 3.6 no mantenían el orden de inserción; en versiones recientes sí, pero se recomienda no depender del orden.
# Mutable → se pueden agregar, modificar o eliminar elementos.
# Acceso rápido → permite obtener valores directamente mediante su clave.
# Claves únicas → no pueden repetirse; si se repite, sobrescribe el valor.

# Crear un diccionario
persona = {
    "nombre": "Adrián",
    "edad": 31,
    "profesion": "Analista de datos"
}
print(persona)  
# {'nombre': 'Adrián', 'edad': 31, 'profesion': 'Analista de datos'}

# Acceder a un valor por clave
print(persona["nombre"])  # Adrián

# Modificar un valor
persona["edad"] = 32
print(persona)  # {'nombre': 'Adrián', 'edad': 32, 'profesion': 'Analista de datos'}

# Agregar un nuevo par clave-valor
persona["pais"] = "Uruguay"
print(persona)

# Eliminar un par clave-valor
del persona["profesion"]
print(persona)

# Métodos útiles
print(persona.keys())    # dict_keys(['nombre', 'edad', 'pais'])
print(persona.values())  # dict_values(['Adrián', 32, 'Uruguay'])
print(persona.items())   # dict_items([('nombre', 'Adrián'), ('edad', 32), ('pais', 'Uruguay')])

# Recorrer un diccionario
for clave, valor in persona.items():
    print(clave, ":", valor)

# Verificar si una clave existe
print("nombre" in persona)  # True
print("profesion" in persona)  # False

# Diccionario vacío
vacio = {}
print(vacio)  # {}


# CASOS DE USO COMUN

# Almacenar información estructurada de manera rápida (ej.: usuarios, productos, configuraciones).
# Contar ocurrencias de elementos:

palabras = ["hola", "mundo", "hola", "python"]
contador = {}
for p in palabras:
    if p in contador:
        contador[p] += 1
    else:
        contador[p] = 1
print(contador)  # {'hola': 2, 'mundo': 1, 'python': 1}

# TIPS 

# - Clave → valor, no admite claves repetidas.
# - Las claves suelen ser str o números (tipos inmutables).
# - get(clave, valor_por_defecto) evita errores si la clave no existe.
# - keys(), values(), items() son útiles para recorrer.
# - dict comprehension es muy potente para crear diccionarios rápido.
# - podés anidar diccionarios (dict dentro de dict).
# - copy() para clonar, update() para actualizar varias claves a la vez.
