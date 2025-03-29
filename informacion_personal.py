# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Esteban Moya",
    "edad": 29,
    "ciudad": "Quito",
    "profesion": "Médico General"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave-valor para la profesion (ya existe, pero se asegura que esté presente)
informacion_personal["profesion"] = "Cirujano General"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0959271431"  # Número ficticio

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print(informacion_personal)