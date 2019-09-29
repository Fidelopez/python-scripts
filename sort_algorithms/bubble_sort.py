"""
    SCRIPT PARA ORDENAR UNA LISTA DE NÚMEROS
    USANDO EL ALGORITMO BUBBLE SORT
"""
# @author fide.dev

def bubble_sort(nums):
    len_nums = len(nums)
    # Itera por toda la lista
    for i in range(len_nums):
        # Los últimos elementos i ya están ordenados
        for j in range(len_nums - i - 1):
            # Si el número actual es mayor al siguiente, cámbialos de lugar
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Si es el archivo principal prueba el algoritmo
if __name__ == '__main__':

    # Random para generar la lista de números
    import random

    # Lista de 15 números aleatorios entre 0 y 99
    random_list = random.sample(range(100), 15)

    # Imprime la lista original y la ordenada ejecutando la función
    print("\nORIGINAL:", " ".join(map(str, random_list)))
    print("\nSORTED:  ", " ".join(map(str, bubble_sort(random_list))))
