#!/usr/bin/python3
# coding: utf8

# Pau Martín Arnau
# isx46420653
# 05/10/18
# Versió acabada

# Calcular l'àrea i el perímetre d'un quadrat
# Entrar 3 nombres Float més grans que 0

# Llegim el costat introduit per l'usuari. 
costat = float(input("Quina és la longitud del costat del quadrat? "))

# Calculem l'area i el perimetre del quadrat. 
area = costat**2

perimetre = costat*4

# Fem uns prints resolent el problema, ensenyem l'area i el perimetre,
# també fem un print amb la finalitat de deixar-ho més estètic.

print ("L'àrea del quadrat és " + str(area))

print ("El perimetre del quadrat és " + str(perimetre))

print ("")

print ("El quadrat és semblant a aquest: ")

print (" ")

# Finalment farem un quadrat amb el costat que ha introduit l'usuari. 

for base in range(0,int(costat),1):
	for altura in range(0,int(costat),1):
		print ("*", end=' ')
	
	print ("")
