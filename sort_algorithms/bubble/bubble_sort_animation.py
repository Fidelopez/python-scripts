"""
    SCRIPT PARA MOSTRAR UNA ANIMACIÓN DEL PROCESO DE ORDENAMIENTO
    DEL ALGORITMO BUBBLE SORT CON pygame
"""
import numpy as np
import pygame

pygame.init()

# Constantes
WHITE = (255,255,255)
RED = (255,0,0)
# Screen size
size = (700,500)

# Número de pasos a brincar cada frame en el ordenamiento
# Controla la velocidad de la animación
STEPS = 50

# Cantidad de datos a ordenar
DATA_TOP = 200

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bubble Sort")
running = True

clock = pygame.time.Clock()

# Datos a ordenar
data = np.array(range(DATA_TOP))
# Desordena los datos de forma aleatoria
np.random.shuffle(data)
sorted = False

# Algoritmo bubble sort como generador
def bubble_sort(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            yield nums

sort_algorithm = bubble_sort(data)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    w, h = pygame.display.get_surface().get_size()
    # Ancho de cada columna
    rect_width = w / DATA_TOP

    # Limpiamos pantalla
    screen.fill(WHITE)

    # Siguiente estado en el ordenamiento
    try:
        if not sorted:
            for i in range(STEPS):
                current_state = next(sort_algorithm)
    except StopIteration:
        sorted = True

    # Se normalizan los datos en el rango de la altura de la ventana
    normalized = [ np.interp(d, [0, DATA_TOP], [0, h]) for d in current_state]

    # Iteración para dibujar rectangulos normalizados
    for ix, dato in enumerate(normalized):
        pygame.draw.rect(screen, RED, [ix*rect_width, h, rect_width, -dato], 0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
