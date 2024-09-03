def leap_year():
	año=input("Ingrese un año:")

	ye=float(año)
	yeeee=ye%100
	yee=ye%4
	yeee=ye%400
	if yee==0 and yeeee==0:
			print("El año ",año," es bisiesto")
	elif yee==0:
		print("El año ",año," es bisiesto")
	else:
		print("El año ",año," no es bisiesto")


leap_year()