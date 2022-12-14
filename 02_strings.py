nombre = "Hancel"
apellido = "Vallejo"

#Deja el espacio entre la string y la variable
print("Hola", nombre)
#No deja el especio entre la string y la variable
print("Hola" + nombre)

#Formato
#Concatenacion basica
formato1 = "Mi nombre es " + nombre + " Y mi apellido es " + apellido
print("1", formato1)
#Concatenacion con Format
formato2 = "Mi nombre es {} y mi apellido es {}".format(nombre, apellido)
print("2",formato2)
#Concatenacion simple con f
formato3 = f"mi nombre es {nombre} y mi apellido es {apellido}"
print("3",formato3)

#Metodos
#Buscar una cadena dentro de otra, responde booleanos
texto = 'sabe programar en Python'
print('Java' in texto)
print('Python' in texto)
#cuenta el total de los caracteres
#len(cadena)
print(len(texto))
#Todo a Mayuscula
mayuscula = texto.upper()
print(mayuscula)
#Todo en minuscula
minuscula = texto.lower()
print(minuscula)
#Contar numero de apariciones en una cadena
print(texto.count('a'))
#minusculas a mayusculas y viceversa
print(texto.swapcase())
#Si inicia con algo en especifico
print(texto.startswith('Sabe'))
print(texto.endswith('C#'))
#Reemplazar algo en especifico
print(texto.replace('Python', 'Java'))
#Primer caracter en mayuscula
print(texto.capitalize())
#Iniciales mayusculas
print(texto.title())
#Valida si la string puede convertirse a numero
#Responde Booleano
print('256'.isdigit())