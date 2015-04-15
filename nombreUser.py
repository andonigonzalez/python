num = 0

while num < 1:
	nombre = input("Escoja un nombre de usuario: ")
	if len(nombre) < 6:
		print("Ese nombre es muy corto escoja otro mas largo")
	elif len(nombre) > 8:
		print("Ese nombre es muy largo escoja otro mas corto")
	else:
		num+=1
		print("Bienvenido" , nombre)