#if
mascota = input('Cual es tu mascota favorita: ')

if mascota == 'perro':
	print("guau!")
elif mascota == 'gato':
	print("miau!")
elif mascota == 'pez':
	print("glu glu!")
else:
	print("oink!")


numero = int(input('Elige un numero'))
if numero % 2 == 0:
	print("El numero es par")
else:
	print("El numero es impar")