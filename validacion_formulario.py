
def validar_formulario(nombre, correo_electronico, numero_telefono):
    """
    Valida los campos de un formulario: nombre, correo electrónico y número de teléfono.
    Requisitos:
    - Nombre: mínimo 3 caracteres.
    - Correo: debe contener un '@' y un '.'.
    - Teléfono: debe tener 9 dígitos y ser numérico.
    """
    # Verificar que el nombre tenga al menos 3 caracteres
    if len(nombre) < 3:
        print("El nombre debe tener un mínimo de 3 caracteres.")
        return False
    
    # Verificar que el correo tenga '@' y '.'
    if "@" not in correo_electronico or "." not in correo_electronico:
        print("El correo electrónico debe contener un punto (.) y un arroba (@).")
        return False
    
    # Verificar que el teléfono tenga 9 dígitos y sea numérico
    if len(str(numero_telefono)) != 9 or not str(numero_telefono).isdigit():
        print("El número de teléfono debe contener 9 dígitos numéricos.")
        return False
    
    print("El formulario es válido.")
    return True

# Ejemplo de uso:
nombre = input("Ingresa tu nombre: ")
email = input("Ingresa tu email: ")
tel = input("Ingresa tu teléfono: ")

validar_formulario(nombre, email, tel)