nombre = "andoni"
password = "123"
num = 0

while num < 3:
	inombre = input("introduce el nombre de usuario: ")
	ipassword = input("introduce la contraseña: ")
	if inombre == nombre and ipassword == password:
		print ("Bienvenido andoni")
		break
	else:
		print ("Nombre o contraseña incorrectos")
		num += 1
		
if num == 3:
	print("Logeo fallido vuelva a intentarlo mas tarde")