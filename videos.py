import os

def renombrar_videos(directorio, prefijo="video"):
    """
    Renombra todos los videos en un directorio con un prefijo y un número secuencial.

    :param directorio: Ruta del directorio que contiene los videos.
    :param prefijo: Prefijo para el nuevo nombre de los archivos (por defecto "video").
    """
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return
    
    archivos = os.listdir(directorio)
    
    # Filtrar solo archivos de video (por extensión)
    extensiones_video = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv']
    videos = [f for f in archivos if os.path.isfile(os.path.join(directorio, f)) and os.path.splitext(f)[1].lower() in extensiones_video]
    
    if not videos:
        print("No se encontraron videos en el directorio.")
        return
    
    videos.sort()
    
    for i, video in enumerate(videos, start=1):
        _, extension = os.path.splitext(video)
        nuevo_nombre = f"{prefijo}{i}{extension}"
        ruta_original = os.path.join(directorio, video)
        ruta_nueva = os.path.join(directorio, nuevo_nombre)
        
        try:
            os.rename(ruta_original, ruta_nueva)
            print(f"Renombrado '{video}' a '{nuevo_nombre}'")
        except Exception as e:
            print(f"No se pudo renombrar '{video}': {e}")

# Cambia 'ruta/del/directorio' por la ruta del directorio que contiene tus videos
if __name__ == "__main__":
    directorio = r'C:\workspace\VENTAS PAGINAS WEB\Cumpleanos-ambar\assent\img'  # Usa una cadena sin formato
    renombrar_videos(directorio)
