# !/usr/bin/python
# coding:utf-8

import os, stat

#Ruta a explorar
path_to_explore="../cartes-i-daus/"
        
print "Aquest fitxers poden tenir errors de seguretat: "
print ""
print "Els others tenen permisos activats, es perillós"
print ""

# Mostrem ruta tot    
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
		
		#Juntem la ruta amb el nom de l'arxiu
        name_path=os.path.join(root, name)
               
        #Detectem els permisos i els imprimim en octal  
        permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
        permisos = str(oct(permissions))
                
        #Ara fem un substring i ens quedem amb l'ultim nombre. 
        # 0770 --> Del 3r al 4t - 1 == 0
        others = permisos[3:4]
		
        if not(others == "0"):
		
			#Juntem la ruta amb el nom de l'arxiu
			name_path=os.path.join(root, name)
			#Imprimim la ruta amb el nom de l'arxiu
			print(name_path) ,
			print ""
			#Adjuntem el pes de l'arxiu al final 
			#Detectem els permisos i els imprimim en octal  
			permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
			permisos = str(oct(permissions))
			print "Permisos: ", permisos

