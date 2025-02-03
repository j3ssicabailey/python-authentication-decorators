"""
Verificación de Inicio de Sesión con Decorador
# Sistema de autenticación para validar las credenciales del usuario y proporcionar
# información personal una vez que se haya iniciado sesión correctamente.
"""

# 1. Registro de usuarios con información adicional como nombre completo y correo electrónico.
usuarios = {
    "usuario1": {"nombre": "José Jimenez", "contraseña": "abc123", "correo": "jose@mail.com"},
    "usuario2": {"nombre": "Ana Álcaraz", "contraseña": "def456", "correo": "ana@mail.com"},
    "usuario3": {"nombre": "Pepa Pérez", "contraseña": "ghi789", "correo": "pepa@mail.com"},
}

# 2. Decorador para verificar las credenciales de inicio de sesión.
def verificar_inicio_sesion(funcion):
    """
    Decorador que verifica si las credenciales del usuario son válidas.
    Si son válidas, ejecuta la función y pasa la información personal del usuario.
    """
    def wrapper(nombre, contraseña):
        if nombre in usuarios and contraseña == usuarios[nombre]["contraseña"]:
            print("Inicio de sesión completado.")
            info_usuario = usuarios[nombre]
            return funcion(info_usuario)
        else:
            print("--- Nombre o contraseña incorrecta ---")
            return None
    return wrapper

# 3. Función que muestra la información personal del usuario.
@verificar_inicio_sesion
def mostrar_informacion(usuario):
    """
    Muestra la información personal del usuario si el inicio de sesión es exitoso.
    """
    print(f"Información Personal:\nNombre: {usuario['nombre']}\nCorreo: {usuario['correo']}")

# Ejemplo de ejecución:
mostrar_informacion("usuario3", "ghi789")  # Inicio de sesión exitoso
mostrar_informacion("usuario2", "123")     # Nombre o contraseña incorrecta
