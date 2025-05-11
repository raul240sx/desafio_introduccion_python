import math as m


radio = float(input('\nIngrese el radio en expresado en [km] (pueden ser números decimales) : ')) * 1000

gravi = float(input('\nIngrese el valor de la constante gravitacional a utilizar expresado en [m/s²] pueden ser números decimales: '))

v_escape = m.sqrt(2 * gravi * radio)

print(f'\nLa velocidad de escape es de {v_escape:.3f} [m/s]')

