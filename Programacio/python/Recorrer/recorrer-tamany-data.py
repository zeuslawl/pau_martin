# !/usr/bin/python
# coding:utf-8

import os, stat, time

#Ruta a explorar
path_to_explore="../cartes-i-daus/"

#Variable de pes total 
pes_arxiu=0

#Dia d'avui, en format de dia i d'any
dia_avui=int(time.strftime("%y"))
        
# Mostrem ruta tot    
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
		
		#Juntem la ruta amb el nom de l'arxiu
        name_path=os.path.join(root, name)
        
        #Pes del fitxer
        pes_arxiu=os.stat(name_path).st_size
        
        #Última data d'accés.
        ultim_acces=time.ctime(os.path.getatime(name_path))
        
        #Agafem els dos caràcters que diuen l'any
        any_ultim=ultim_acces[22:24]
        
        #Fem la resta dels dos últims números de l'any. Si és major d'un any dona 1, sinò 0.
        temps_total = int(dia_avui) - int(any_ultim)
 
        
        #Fem la condició de més d'1G i més d'1 any des de l'ultima modificació
        #El < a 0, és per si per exemple, fos l'any 2100 i l'arxiu del 2099, o menys, també el mostraria. 
        if ((pes_arxiu > 2**30) and (temps_total >= 1 or temps_total < 0)):
			
			#Imprimim la ruta de l'arxiu
			print(name_path) ,
			
			#Imprimim el que pesa
			print "pesa" ,
			#Dividim el pes, per a que ens ho doni en GB.
			pes = os.stat(name_path).st_size / 1073741824
			print pes
			print "GB"
			
			#Imprimim la última data de modificació.
			print ultim_acces
			
			#Fem un separador
			print
			
