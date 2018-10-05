#!/usr/bin/python3
# -*-coding: utf8-*-

# Pau Martín Arnau
# isx46420653
# 05/10/18
# Versió acabada

# Que demani el preu d'algun article i calculi el seu valor aplicant-li un 13% d'IVA.

# S'ha de llegir el preu de l'article i mostrar el preu final, ho farem amb valors float

preu = float(input("Quin es el preu de l'article? "))

preu_total = (preu*13/100)+preu

print ("")
print ("El preu total de l'article aplicant-li el 13% d'IVA és: ", preu_total)
print ("")
