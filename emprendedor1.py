
precio_sus = int(input('\nIngrese el valor de la suscripción en pesos chilenos: '))
usuarios = int(input('\nIngrese la cantidad de usuarios: '))
gasto_total = int(input('\nIngrese el gasto total en pesos chilenos: '))

utilidades = (precio_sus * usuarios) - gasto_total

print(f'\nLas utilidades generadas son de {utilidades} pesos chilenos')