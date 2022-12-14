# Mayor que 
print(7 > 3)
# Menor que
print(7 < 3)
#Mayor o igual 
print(2 >= 3)
#Menor o igual
print(2 <= 3)
#Igual que
print(6 == 1)
#Diferente de
print(6 != 1)


#Strings
#Igual que
print("Manzana" == 'Manzana')

#Flotantes
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
#Comparacion da falso por precision de decimales
print(x == y)
#Convirtiendo a String
y_str = format(y, ".2g")
print('str => ', y_str)
print(y_str == str(x))
#Matematica
tolerancia = 0.00001
print(abs(x - y) < tolerancia)