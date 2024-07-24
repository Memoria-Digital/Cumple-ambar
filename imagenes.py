import os

def renombrar_fotos(directorio, prefijo="imagen"):
    """
    Renombra todas las fotos en un directorio con un prefijo y un número secuencial.

    :param directorio: Ruta del directorio que contiene las fotos.
    :param prefijo: Prefijo para el nuevo nombre de los archivos (por defecto "imagen").
    """
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return
    
    archivos = os.listdir(directorio)
    
    # Filtrar solo archivos de imagen (por extensión)
    extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif']
    fotos = [f for f in archivos if os.path.isfile(os.path.join(directorio, f)) and os.path.splitext(f)[1].lower() in extensiones_imagen]
    
    if not fotos:
        print("No se encontraron fotos en el directorio.")
        return
    
    fotos.sort()
    
    for i, foto in enumerate(fotos, start=1):
        _, extension = os.path.splitext(foto)
        nuevo_nombre = f"{prefijo}{i}{extension}"
        ruta_original = os.path.join(directorio, foto)
        ruta_nueva = os.path.join(directorio, nuevo_nombre)
        
        try:
            os.rename(ruta_original, ruta_nueva)
            print(f"Renombrado '{foto}' a '{nuevo_nombre}'")
        except Exception as e:
            print(f"No se pudo renombrar '{foto}': {e}")

# Cambia 'ruta/del/directorio' por la ruta del directorio que contiene tus fotos
if __name__ == "__main__":
    directorio = r'C:\workspace\VENTAS PAGINAS WEB\Cumpleanos-ambar\assent\img'  # Usa una cadena sin formato
    renombrar_fotos(directorio)
