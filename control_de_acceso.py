'''
Decorador de Control de Acceso:
n ejemplo de una posible entrada y salida de la solucion:
Entrada Salida
- entorno : produccion / desarrollo
- subir_documento("Documento1")
-eliminar_documento("Documento1")
- Acceso permitido / rechazado :
- Documento subido
- Documento eliminado
'''


def decorador_verificar_acceso_entorno(funcion):
    """
    Decorador que controla el acceso a una función según el entorno de ejecución.
    Solo permite el acceso en el entorno 'produccion'.
    """
    def wrapper(entorno):
        if entorno == "produccion":
            print(f"Acceso aprobado.")
            funcion(entorno)  # Ejecuta la función si el entorno es producción.
        else:
            print(f"Acceso denegado")  # Deniega el acceso en otros entornos.
    return wrapper

@decorador_verificar_acceso_entorno
def subir_documento(entorno):
    """Simula la subida de un documento."""
    print("Subiendo el documento")

@decorador_verificar_acceso_entorno
def eliminar_documento(entorno):
    """Simula la eliminación de un documento."""
    print("Eliminando el documento")

# Prueba del decorador en el entorno 'produccion'
entorno = "produccion"
subir_documento(entorno)
eliminar_documento(entorno)

# Prueba en otro entorno
entorno = "desarrollo"
subir_documento(entorno)
eliminar_documento(entorno)
