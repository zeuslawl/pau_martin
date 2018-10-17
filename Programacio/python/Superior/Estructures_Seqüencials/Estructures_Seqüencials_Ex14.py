#!/usr/bin/python3
# -*-coding: utf8-*-

# Pau Martín Arnau
# isx46420653
# 11/10/18
# Primera versió

# Demanar un nombre de base i convertir els nombres de 3 xifres
# d'aquella base a un nombre decimal. 

# Entrar un numero enter > 0 que sigui la base, també entrar 3 nombres enters > 0 i 
# que el nombre no sigui major a la base.
 
# El resultat será el nombre introdüit pero en base decimal.

base = int(input("Quina base vols fer servir? "))

a_base = int(input("Primer dígit? "))
b_base = int(input("Segon dígit? "))
c_base = int(input("Tercer dígit? "))

a_decimal = a_base * base**2
b_decimal = b_base * base**1
c_decimal = c_base * base**0

resultat = a_decimal+b_decimal+c_decimal

print ("El teu nombre de base", base, "a decimal és el:", resultat)
