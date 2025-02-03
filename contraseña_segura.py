import string
import random

# --- Función para validar la contraseña
def validar_contraseña(contraseña):
    """
    Valida si la contraseña cumple con los requisitos:
    - Longitud mínima de 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial
    """
    longitud = 8
    mayuscula = False
    minuscula = False
    numero = False
    caracter_especial = False
    
    # Comprobación de longitud mínima (8 caracteres)
    if len(contraseña) < longitud:
        return False

    for caracter in contraseña:
        # Comprobar presencia de letras mayúsculas
        if caracter.isupper():
            mayuscula = True
        # Comprobar presencia de letras minúsculas
        elif caracter.islower():
            minuscula = True
        # Comprobar presencia de números
        elif caracter.isnumeric():
            numero = True
        # Comprobar presencia de caracteres especiales
        else:
            caracter_especial = True
    
    # La contraseña debe cumplir todas las condiciones
    return mayuscula and minuscula and numero and caracter_especial

# --- Función para generar una contraseña segura
def generar_contraseña(longitud=9, mayuscula=True, minuscula=True, numero=True, caracter_especial=True):
    """
    Genera una contraseña segura aleatoria basada en los criterios dados:
    - Longitud
    - Incluir mayúsculas, minúsculas, números y caracteres especiales
    """
    nueva_contraseña = ""
    if mayuscula:
        nueva_contraseña += string.ascii_uppercase
    if minuscula:
        nueva_contraseña += string.ascii_lowercase
    if numero:
        nueva_contraseña += string.digits
    if caracter_especial:
        nueva_contraseña += string.punctuation
    
    # Generar la contraseña aleatoria
    contraseña_generada = "".join(random.choice(nueva_contraseña) for i in range(longitud))
    
    return contraseña_generada

# --- Solicitar y validar la contraseña
def main():
    contraseña = input("Introduce tu contraseña nueva: ")
    
    # Validar la contraseña
    if validar_contraseña(contraseña):
        print("Tu contraseña es segura.")
    else: 
        print("Tu contraseña no es segura.")
        # Generar una nueva contraseña segura
        contraseña_generada = generar_contraseña()
        print(f"Tu contraseña sugerida es: {contraseña_generada}")

# Ejecutar el script
if __name__ == "__main__":
    main()
