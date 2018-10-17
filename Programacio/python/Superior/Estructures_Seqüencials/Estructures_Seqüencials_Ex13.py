#!/usr/bin/python3
# -*-coding: utf8-*-

# Pau Martín Arnau
# isx46420653
# 11/10/18
# Primera versió

# Convertir un nombre binari de 3 xifres a un nombre decimal. 

# Entrar un numero enter que sigui 0 o 1. El resultat serà
# el nombre en format decimal. 

a_binari = int(input("Primer dígit? "))
b_binari = int(input("Segon dígit? "))
c_binari = int(input("Tercer dígit? "))

a_decimal = a_binari * 2**2
b_decimal = b_binari * 2**1
c_decimal = c_binari * 2**0

resultat = a_decimal+b_decimal+c_decimal

print ("El teu nombre binari a decimal és el:", resultat)
