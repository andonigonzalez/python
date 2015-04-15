edad = input("cuantos años tienes?\n")
eleccion = input("a que quieres cambiar tu edad?\ndias horas segundos\n")
if eleccion == "dias":
	dias = int(edad) * 365
	print("tienes" , dias , "dias de edad")
elif eleccion == "horas":
	horas = (int(edad) * 365) * 24
	print("tienes" , horas , "horas de edad")
elif eleccion == "segundos":
	segundos = ((int(edad) * 365) * 24) * 3600
	print ("tienes" , segundos , "segundos de edad")

