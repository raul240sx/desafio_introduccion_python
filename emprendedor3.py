
precio_sus = int(input('\nIngrese el valor de la suscripción en pesos chilenos: '))
usuarios = int(input('\nIngrese la cantidad de usuarios: '))
gasto_total = int(input('\nIngrese el gasto total en pesos chilenos: '))
utilidades_anterior = int(input('\nDe cuanto fueron las utilidades del año anterior en pesos chilenos pesos chilenos (el valor NO puede ser cero): '))

utilidades = (precio_sus * usuarios) - gasto_total

razon = utilidades / utilidades_anterior

print(f'\nLas utilidades generadas son de {utilidades} pesos chilenos y la razon de utilidades con respecto al año anterior es de {razon:.2f}\n')