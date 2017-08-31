# -*- coding: utf-8 -*-

Yellow = "\033[93m"
Green = "\033[92m"
Blue = "\033[94m"
Red = "\033[91m"
EndColor = "\033[0m"

def printError(errCode):
	if errCode == 1:
		print(Red + "Must have '=' character" + EndColor)
	elif errCode == 2:
		print(Red + "SyntaxError\nAllowed characters : '0-9 =+ Xx'\nCorrect form : 'n*x^n'" + EndColor)
	elif errCode == 3:
		print(Red + "ArgumentError." + EndColor)

def printEquation(eq):
	print(Blue + "Equation: " + Yellow + eq.equation + EndColor)

def printDegree(degree):
	print(Blue + "Polynomial degree: " + Yellow + str(degree) + EndColor)

def printPolynomialDegree(degree):
	if degree >= 3:
		print(Blue + "The polynomial degree is stricly greater than 2, I can't solve." + EndColor)
		return -1
	elif degree < 0:
		print(Blue + "The polynomial degree is stricly smaller than 0, I can't solve." + EndColor)
		return -1

def printReduceForm(eq):
	reduceForm = ""
	if eq.a != 0:
		reduceForm += str(eq.a) + "x2"
	if eq.b != 0:
		tmp = eq.b
		if eq.a != 0 and eq.b > 0:
			reduceForm += " + "
		elif eq.a != 0 and eq.b < 0:
			reduceForm += " - "
			tmp *= -1
		reduceForm += str(tmp) + "x1"
	if eq.c != 0:
		tmp = eq.c
		if eq.b != 0 or eq.a != 0:
			if eq.c > 0:
				reduceForm += " + "
			elif eq.c < 0:
				reduceForm += " - "
				tmp *= -1
		reduceForm += str(tmp)

	if eq.nt != "":
		reduceForm += " + " + eq.nt
	if reduceForm == "":
		reduceForm = "0"
	reduceForm += " = 0"
	print(Blue + "Reduced form: " + Yellow + reduceForm + EndColor)

def printDiscriminant(eq):
	if eq.degree != 2 or eq.a == 0 or eq.a == 0.0:
		return
	print(Blue + "a : " + Yellow + str(eq.a) + Blue + "\nb : " + Yellow + str(eq.b) + Blue + "\nc : " + Yellow + str(eq.c) + EndColor)
	print(Blue + "Discriminant : " + Yellow + "b² − 4ac" + EndColor + Blue + " = " + Yellow + str(eq.discriminant) + EndColor)
	if eq.discriminant > 0:
		print(Blue + "Discriminant is strictly positive, the two solutions are:" + EndColor)
	elif eq.discriminant < 0:
		print(Blue + "Discriminant is strictly negative, the two solutions are:" + EndColor)
	else:
		print(Blue + "Discriminant is 0, the solution is:" + EndColor)

def printSolution(eq):
	try:
		float(eq.solve)
	except:
		print(Blue + eq.solve)
		return
	solution = ""
	if eq.degree == 1:
		solution = Blue + "Solution: \n"
		solution += Blue + "x = " + Yellow + str(eq.c) + " / " + str(eq.b) + Blue + " = " + Yellow + str(eq.solve) + EndColor
	elif eq.degree == 2:
		if eq.discriminant >= 0:
			solution += Blue + "x = " + Yellow + " (-b - √Δ) / 2a" + Blue + " = " + Yellow + str(eq.solve) + EndColor
		if eq.discriminant > 0:
			solution += "\n" + Blue + "x^2 = " + Yellow + " (-b + √Δ) / 2a" + Blue + " = " + Yellow + str(eq.solveBis) + EndColor
		if eq.discriminant < 0:
			solution += Blue + "x = " + Yellow + " (-b - i√-Δ ) / 2a" + Blue + " = " + Yellow + str(eq.solve) + " - " + str(eq.delta) + "i"
			solution += "\n" + Blue + "x^2 = " + Yellow + " (-b + i√-Δ ) / 2a" + Blue + " = " + Yellow + str(eq.solveBis) + " + " + str(eq.delta) + "i" + EndColor
	print(solution)

def printInfiniteSolution():
	print("Infinite solutions")

def printNoSolution():
	print("No solutions")