edad = int(input("cuantos años tienes?\n"))
eleccion = input("a que quieres cambiar tu edad?\ndias horas segundos\n")
if eleccion == "dias":
	dias = edad * 365
	print("tienes" , dias , "dias de edad")
elif eleccion == "horas":
	horas = (edad * 365) * 24
	print("tienes" , horas , "horas de edad")
elif eleccion == "segundos":
	segundos = ((edad * 365) * 24) * 3600
	print ("tienes" , segundos , "segundos de edad")

