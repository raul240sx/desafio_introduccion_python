
precio_sus = int(input('\nIngrese el valor de la suscripción en pesos chilenos: '))
usuarios_normal = int(input('\nIngrese la cantidad de usuarios con suscripción normal: '))
usuarios_premium = int(input('\nIngrese la cantidad de usuarios con suscripción premium (valor de suscripción + 50%): '))
gasto_total = int(input('\nIngrese el gasto total en pesos chilenos: '))



utilidades = ((precio_sus * usuarios_normal) + ((precio_sus * 1.5) * usuarios_premium)) - gasto_total

print(f'\nLas utilidades generadas son de {utilidades} pesos chilenos')