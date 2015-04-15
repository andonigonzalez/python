nombre = "andoni"
password = "123"
num = 0

while 0 < 1:
	inombre = input("introduce el nombre de usuario: ")
	ipassword = input("introduce la contraseña: ")
	
	if inombre == nombre and ipassword == password:
		num += 1
		print ("Bienvenido andoni")
		break
	else:
		print ("Nombre o contraseña incorrectos")