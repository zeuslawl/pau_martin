#coding: utf-8

def my_range(inici,fi,increment):
	while (inici <= fi):
		yield inici
		inici = inici + increment
		
binari=input("Quin és el teu nombre binari? ")
decimal = 0
	
for adresa in my_range(0,7,1):
	if adresa == 0:
		if binari % 10 == 1: 
			decimal = 2**adresa
		resultat = binari // 10
	else: 
		if resultat % 10 == 1:
			decimal = decimal + 2**adresa
		resultat = resultat // 10 

print "El nombre aquest a decimal és:", str(decimal)
