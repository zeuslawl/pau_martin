#!/usr/bin/python
# coding: utf8

sequencia = 0
actual = 0
siguiente = 1
limit = input("Quantes voltes? ")
Sortir = False

while Sortir == False:
	print actual
	print siguiente
	
	if (sequencia == limit):
		Sortir = True
	
	actual = actual + siguiente
	siguiente = siguiente + actual
	sequencia = sequencia + 1
