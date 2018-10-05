#coding: utf-8

def my_range(inici,fi,increment):
	while (inici <= fi):
		yield inici
		inici = inici + increment

decimal = input("Quin numero vols convertir a binari? ")
a = ""
for adresa in my_range(1,8,1):
	if adresa == 1:		
		if decimal % 2 == 0:
			a="0"+a
		else: 
			a="1"+a
		resultat = decimal // 2 
	else: 
		if resultat % 2 == 0:
			a="0"+a
		else: 
			a="1"+a
		resultat = resultat // 2

print a
