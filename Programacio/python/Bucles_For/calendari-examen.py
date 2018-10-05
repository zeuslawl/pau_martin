#coding:utf-8

def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment
		
cont = 1

mes = raw_input('A quin mes estas? Ex: ("Gener") ')

comensa_mes = {"Gener":7,"Febrer":3,"Març":3,"Abril":6,"Maig":1,"Juny":4,"Juliol":6,"Agost":2,"Septembre":5,"Octubre":7,"Novembre":3,"Desembre":5}

acaba_mes = {"Gener":31,"Febrer":28,"Març":31,"Abril":30,"Maig":31,"Juny":30,"Juliol":31,"Agost":31,"Septembre":30,"Octubre":31,"Novembre":30,"Desembre":31}

for fila1_espais in my_range(1, comensa_mes [mes] - 1,1):
	print "  ",
	
for fila1_nums in my_range(comensa_mes [mes],7,1):
	print str(cont) + ' ',
	cont = cont + 1
	
print ""

for files in my_range(1,5,1):
	
	for col in my_range(1,7,1):
		
		
		if cont > acaba_mes [mes]:
			print " ",
		else:
			if (cont < 10):
				print str(cont) + ' ', 
			else: 
				print cont,
		cont = cont + 1
		
	print ""
		
		
		
		
		
		
