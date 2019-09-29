

"""
SCRIPT PARA CALCULAR UN NÚMERO DE LA SERIE
FIBONACCI SEGÚN SU POSICIÓN USANDO
LA FORMULA EXPLÍCITA
Wikipedia:
    https://cutt.ly/9wImDmB
"""
@author fidev.blog

# sqrt para calcular raices cuadradas
from math import sqrt

#Constante con el valor de número áureo
PHI = (1+sqrt(5)) / 2

def fibonacci(n):
    if n < 2:
        return n
    else:
        f = ( PHI**n-(1-PHI)**n ) / sqrt(5)
        # round redondea numeros flotantes
        return round(f)


"""
PRUEBA DE LA FUNCIÓN fibonacci()
"""


for i in range(10):
    print(fibonacci(i))
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
