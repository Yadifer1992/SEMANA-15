# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Esteban Raul Moya Barragan",
    "edad": 29,
    "ciudad": "Quito",
    "profesion": "Médico General",
    "correo": "esteban.moya@example.com",
    "direccion": "Av. Orellana 2430, Quito, Ecuador"
}

# Función para modificar la ciudad
def modificar_ciudad(diccionario, nueva_ciudad):
    ciudad_anterior = diccionario["ciudad"]
    diccionario["ciudad"] = nueva_ciudad
    return ciudad_anterior

# Función para agregar teléfono si no existe
def agregar_telefono(diccionario, telefono):
    if "telefono" not in diccionario:
        diccionario["telefono"] = telefono
        return True
    return False

# Eliminar la clave "edad" del diccionario
def eliminar_edad(diccionario):
    diccionario.pop("edad", None)

# Función para imprimir el diccionario
def imprimir_diccionario(diccionario):
    print("\nInformación Personal:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

# Función principal
def main():
    global informacion_personal
    
    # Modificar la ciudad
    nueva_ciudad = input("Ingrese una nueva ciudad: ")
    ciudad_anterior = modificar_ciudad(informacion_personal, nueva_ciudad)
    print(f"La ciudad ha cambiado de {ciudad_anterior} a {informacion_personal['ciudad']}")
    
    # Agregar teléfono
    telefono = input("Ingrese su número telefónico: ")
    if agregar_telefono(informacion_personal, telefono):
        print("Número telefónico agregado correctamente.")
    else:
        print("El número telefónico ya existe en el diccionario.")
    
    # Eliminar edad
    eliminar_edad(informacion_personal)
    
    # Imprimir información final
    imprimir_diccionario(informacion_personal)

# Ejecutar el programa
if __name__ == "__main__":
    main()
