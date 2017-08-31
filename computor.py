#!/usr/bin/python

import sys
import re
import os
from printComputor import *
from carreComputor import *

class Equation:
	degree = 0
	solve = 0.0
	solveBis = 0.0
	a = 0.0
	b = 0.0
	c = 0.0
	nt = ""
	discriminant = 0.0
	delta = 0
	def __init__(self, equation):
		self.equation = equation.lower().replace(" ", "")#clean

#check syntax
def syntaxError(eq):
	result1 = re.findall('([^xX\s0-9\-\.\=\+\*\/\^])', eq.equation)
	result2 = re.findall("\=", eq.equation)
	result3 = ""
	result3 = re.sub('(\d\.\d\*x\^\d)|(\d\*x\^\d)|(\d\.\d)|\d|\+|\-|\=', "", eq.equation)
	if not result2 or len(result2) != 1 or len(result3) > 0 or len(result1) > 0:
		printError(2)
		return -1


def syntaxX(myTab):
	newTab = []
	for n,i in enumerate(myTab):
		s = None
		if "*x^0" in i:
			s = re.sub("(x\^0)|\*", "", str(i)) + "x0"
		elif "*x^1" in i:
			s = re.sub("(x\^1)|\*", "", str(i)) + "x1"
		elif "*x^2" in i:
			s = re.sub("(x\^2)|\*", "", str(i)) + "x2"
		elif "x" in i:
			s = str(i)
		elif i != "-":
			newTab.append(str(float(i)))
		if s != None:
			newTab.append(s)
		if n > 0 and myTab[n-1] == "-":
			if i != "-":
				if n == 1 or myTab[n-2] != "-":
					newTab[-1] = "-" + newTab[-1]
	return newTab

def splitter(s):
	patern = '([-+])'
	table = re.split(patern, s)
	while None in table:
		table.remove(None)
	while "" in table:
		table.remove("")
	while "+" in table:
		table.remove("+")
	ret = syntaxX(table)
	return ret

#parser
def parser(eq):
	eqcopie = eq.equation
	tab = eqcopie.split("=")
	if len(tab) > 2:
		printError(2)
		return -1
	eq.left = splitter(tab[0])
	eq.right = splitter(tab[1])
	if eq.left == None or eq.right == None or len(eq.left) == 0 or len(eq.right) == 0:
		printError(2)
		return -1

#degree
def getDegree(eq):
	if eq.nt == "":
		if eq.a == 0:
			if eq.b == 0:
				eq.degree = 0
			else:
				eq.degree = 1
		else:
			eq.degree = 2
	else:
		split = re.split('(x\^\d*)', str(eq.nt))
		xInSplit = []
		for n, i in enumerate(split):
			toto = ""
			if "x^" in i:
				toto = str(i).replace("x^", "")
			if toto:
				xInSplit.append(int(toto))
		if len(xInSplit) > 0:
			eq.degree = max(xInSplit)

#solver
def reduceEquation(eq):
	eqB = []
	for n,i in enumerate(eq.right):
		if str(i) == '0' or str(i) == "0.0":
			continue
		if "-" not in str(i):
			s = "-" + str(i)
			eqB.append(s)
		else:
			s = str(i).replace("-", "")
			eqB.append(s)
	for n,i in enumerate(eq.left):
		if str(i) == '0' or str(i) == "0.0":
			continue
		if "-" not in str(i):
			eqB.append(str(i))
		else:
			eqB.append(str(i))
	for n, i in enumerate(eqB):
		if "x2" in str(i):
			eq.a += float(i.replace("x2", ""))
		elif "x1" in str(i):
			eq.b += float(i.replace("x1", ""))
		elif "x0" in str(i):
			eq.c += float(i.replace("x0", ""))
		elif "x" not in str(i):
			eq.c += float(i)
		else:
			index = str(i).index('*')
			tmp = str(i)[0:index]
			if float(tmp) == 0:
				continue
			else:
				eq.nt += str(i)

def solver(eq):
	if eq.a != 0 and eq.degree == 2:
		eq.degree = 2
		eq.discriminant = (ft_carre(eq.b)) - 4 * eq.a * eq.c
		if eq.discriminant > 0:
			eq.solve = (((eq.b * -1) - ft_sqrt(eq.discriminant))) / (2 * eq.a)
			eq.solveBis = (((eq.b * -1) + ft_sqrt(eq.discriminant))) / (2 * eq.a)
		elif eq.discriminant == 0:
			eq.solve = (eq.b * -1) / (2 * eq.a)
		else:
			eq.delta = ft_sqrt(eq.discriminant * -1) / 2 * eq.a
			eq.solve = ((eq.b * -1) / (2 * eq.a))
			eq.solveBis = ((eq.b * -1) / (2 * eq.a))
	elif eq.b != 0:
		eq.degree = 1
		if eq.c != 0:
			if eq.b != 0:
				eq.b *= -1
				print(str(eq.b))
				eq.solve = (float(eq.c)/float(eq.b))
			else:
				eq.solve = "No solution"
		else:
			if eq.c != 0:
				eq.solve = 0
			elif eq.degree == 1:
				eq.solve = "Infinite solutions"
	if eq.a == 0 and eq.b == 0:
		eq.degree = 0
		if eq.c == 0:
			eq.solve = "True, infinite solution"
		else:
			eq.solve = "False, no solution"
	if eq.solve == -0:
		eq.solve = 0
	if eq.solveBis == -0:
		eq.solveBis = 0

def StartComputor(param):
	eq = Equation(param)
	if syntaxError(eq) == -1:
		return -1
	printEquation(eq)
	if parser(eq)== -1:
		return -1
	reduceEquation(eq)
	getDegree(eq)
	printDegree(eq.degree)
	printReduceForm(eq)
	printPolynomialDegree(eq.degree)
	if eq.degree >= 0 and eq.degree <=2:
		solver(eq)
		printDiscriminant(eq)
		printSolution(eq)
	return

def main():
	if len(sys.argv) != 2:
		printError(3)
		return
	s = str(sys.argv[1])
	StartComputor(s)
main()