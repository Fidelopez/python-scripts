"""
    SCRIPT PARA TRANSFORMAR UNA IMAGEN A COLOR EN UNA
    EN BLANCO Y NEGRO USANDO PIL Y CLICK
"""
@author fide.dev

# click para administrar los argumentos del script
import click
# Manipulación de imágenes con paquete pillow
from PIL import Image

# Se establecen los argumentos necesarios para usar el script
@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('output')
def black_and_white(filename, output):
    # Lee la imagen original
    original_image = Image.open(filename)

    # Se convierte en blanco y negro
    bw_image = original_image.convert('L')

    # Se guarda la nueva imagen
    bw_image.save(output)
    print("Image saved!")


if __name__ == '__main__':
    black_and_white()
