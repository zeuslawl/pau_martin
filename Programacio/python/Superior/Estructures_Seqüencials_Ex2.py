#!/usr/bin/python3
# coding: utf8

# Pau Martín Arnau
# isx46420653
# 05/10/18
# Versió acabada

# Calcular el sou d'un treballador que cobra un preu fix per hora pero que el redueix en 
# un 10% per als impostos.
# S'ha de llegir el nom del treballador, les hores treballades 
# i el preu que cobra per hora. 

nom = input("Com es diu el treballador? ")
hores = float(input("Quantes hores ha treballat a la setmana? "))
preu = float(input("Quin import cobra per hora treballada? "))

sou = preu * hores * 4
impostos = sou * 10/100
salari = sou - impostos

print ("")
print ("El/La", nom, "ha treballat", hores, "hores i cobra", preu, "€ a la hora, per tant: ")
print ("Cobra en total", sou, "€ al mes, pero paga en impostos", impostos, "€ al mes")
print ("aleshores el seu salari a final de mes és:", salari, "€")
print ("")
