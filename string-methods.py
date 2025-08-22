texto = "Hola muNdo"
texto_con_espacios = "                texto con espacios       "
texto_separado = "Python,Javascript,Django,React"
lista = ["Hola", "Juan", "Carlos"]
numero = "1992"
letras = "abcd"
espacio = "     "
repeticion = "Manzana, Naranja, Manzana"

print("capitalize:", texto.capitalize())   # Convierte la primera letra en mayúscula (el resto en minúscula)
print("upper:", texto.upper())             # Convierte todo en mayúsculas
print("lower:", texto.lower())             # Convierte todo en minúsculas
print("strip:", texto_con_espacios.strip()) # Elimina espacios al inicio y al final
print("replace:", texto.replace("muNdo", "Mundo"))  # Reemplaza una palabra por otra
print("split:", texto_separado.split(",")) # Divide en lista usando separador coma
print("join:", ",".join(lista))            # Une lista en un string con comas
print("find:", texto.find("muNdo"))        # Primera posición de la subcadena (o -1 si no existe)
print("rfind:", repeticion.rfind("Manzana")) # Última posición de la subcadena
print("index:", texto.index("muNdo"))      # Igual que find, pero lanza error si no existe
print("startswith:", texto.startswith("Hola"))  # ¿Empieza con "Hola"?
print("endswith:", texto.endswith("muNdo"))    # ¿Termina con "muNdo"?
print("isdigit:", numero.isdigit())        # True si todos son dígitos
print("isalpha:", "HolaMundo".isalpha())   # True si todos son letras (sin espacios)
print("isalnum:", "abc123".isalnum())      # True si todos son alfanuméricos
print("isspace:", espacio.isspace())       # True si solo hay espacios
print("count:", repeticion.count("Manzana")) # Cuenta cuántas veces aparece "Manzana"
