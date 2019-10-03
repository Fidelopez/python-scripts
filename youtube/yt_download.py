"""
    SCRIPT PARA DESCARGAR VIDEOS DESDE YOUTUBE CON
    EL USO DE pytube Y click
"""
@author fide.dev

# click para administrar los argumentos del script
import click
# Manipulación de videos con pytube
from pytube import YouTube
# Se establecen los argumentos necesarios para usar el script
@click.command()
@click.argument('video_url')
@click.argument('output')
def download(video_url, output):
    def progress_check(stream, chunk, file_handle, remaining):
    	# Obtiene el porcentaje que ya fue descargado
    	percent = (100*(file_size-remaining))/file_size
    	print(f"{percent:00.0f}% downloaded")

    global file_size
    # Busca el video en YouTube
    video = YouTube(video_url, on_progress_callback=progress_check)
    # Selecciona la primera fuente de stream que existe
    video_stream = video.streams.first()
    print(f'Your video "{video_stream.title}" will be downloaded to "{output}"')
    # Ajusta el tamaño del archivo para medir progreso
    file_size = video_stream.filesize
    # Descarga en el path de salida
    video_stream.download(output)
    print("Video downloaded!")

if __name__ == '__main__':
    file_size = 0
    download()
