#!/usr/bin/python
# coding: utf8

print ("Digues els números que vols posar per a fer l'equació")

a = input("A: ")
b = input("B: ")
c = input("C: ")

solucio_suma = (-b + (b**2 - 4*(a*c))**0.5)/2*a

solucio_resta = (-b - (b**2 - 4*(a*c))**0.5)/2*a

print ("La solució de l'operació sumant és: ") + str(solucio_suma)

print ("La solució de l'operació restant és: ") + strsolucio_resta)
