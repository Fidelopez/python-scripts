"""
    SCRIPT PARA ORDENAR UNA LISTA DE NÚMEROS
    USANDO EL ALGORITMO QUICK SORT CON RECURSIVIDAD
"""
# @author fide.dev

def quick_sort(nums):
    less = []
    equal = []
    greater = []

    # Condición para terminar la recursividad, si solo hay un elemento, regresa
    if len(nums) > 1:
        # Pivote siempre será el primero
        pivot = nums[0]
        for x in nums:
            # Coloca el número en su lista correspondiente según el pivote
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Ordena los números más pequeños y los mayores, regresalos el orden
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return nums

# Si es el archivo principal prueba el algoritmo
if __name__ == '__main__':
    import random # Random para generar la lista de números
    # Lista de 15 números aleatorios entre 0 y 99
    random_list = random.sample(range(100), 15)
    # Imprime la lista original y la ordenada ejecutando la función
    print("\nORIGINAL:", " ".join(map(str, random_list)))
    print("\nSORTED:  ", " ".join(map(str, quick_sort(random_list))))
