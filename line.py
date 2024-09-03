import
def line():
	a=input("Ingrese el coeficiente A:")
	b=input("Ingrese el coeficiente B:")
	x1=input("Ingrese el coeficiente X1:")
	x2=input("Ingrese el coeficiente X2:")
	A=float(a)
	B=float(b)
	X1=float(x1)
	X2=float(x2)
	print("El coeficiente A de su ecuación de la recta es:", A)
	print("El coeficiente B de su ecuación de la recta es:", B)
	print("El coeficiente X1 de su ecuación de la recta es:", X1)
	print("El coeficiente X2 de su ecuación de la recta es:", X2)

	y1=A*X1+B
	y2=A*X2+B

	dist= math.sqrt(((X2-X1)**2)+((y2-y1)**2))
	print("La distancia entre ellos es:", dist)

line()






