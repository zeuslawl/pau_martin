
# Tallafocs / Firewall

* * *
 
### *Tallafocs*

**Què es un sistema tallafocs? Quina és la seva finalitat?**  
 
 La seva finalitat es la de bloquejar l'accès al sistema, permet filtrar i bloquejar paquets segons les IP, els ports per on s'envien i els protocols utilitzats.  
   
**Quines generacions de tallafocs hi ha hagut i què millorava cadascun?**  

 *Primera generació: Filtrat de paquets, Xarxa.*  
 
És el primer sistema de tots, el més bàsic, la seva funció és inspeccionar els paquets que transfereixen dades, si el paquet no  compleix amb el necessari és destruit o retornat. La informació que es mira a la hora de filtrar és Protocol, numero de port i si es TCP o UDP. Actua a la 3a capa del model OSI. 

*Segona generació – L'estat del Firewall*  

La millora que introdueix s que els nous firewalls ara examinen els paquets de dins de les trames, i poden veure si el paquet es erròni, si es una primera connexió, si es correcte o si pot ser algún paquet no desitjat.  

*Tercera generació — Firewall d'aplicació*  

És la millora de l'anterior, ja que aquest a més també pot veure les aplicacions i els protocols, com per exemple un servidor DNS o d'un port 80. Per tant pot bloquejar per protocol i per port a la vegada.  
  
**Quines capes té el model OSI?**  
  
  El model OSI té un total de 7 capes. 
  
  1. Físic   
  2. Enllaç de dades  
  3. Xarxa  
  4. Transport  
  5. Sessió  
  6. Presentació  
  7. Aplicació
  
**Quines capes té el model TCP/IP? En aquest cas feu una breu descripció de les funcionalitats de cada capa.**  
  
  En té un total de 4.   
  1. Accés a Xarxa   
  2. Internet  
  3. Transport  
  4. Aplicació  
  
 **A quina capa/capes sol treballar tradicionalment un tallafocs?**   
  
  Sol treballar a la capa de Xarxa, el nivell 3 del model OSI, ja que normalment filtra entre les direccions IP, també pot fer-ho a la capa 4, de transport i filtrar per els ports des dels quals envien les trames.  
 
### *Tallafocs Linux*  
  
* * *  
  
**Busqueu quins són els tradicionals sistemes de tallafocs incorporats en linux i anomeneu-los**  
  
 Abans del Fedora 19 es configurava amb el iptables, despres, els sistemes ja integren el FirewallD.
 
 **Quins dels anteriors tallafocs estan instal.lats al fedora de classe? Com ho comproveu?**    
 
 El FirewallD està instal·lat, ho podem comprovar amb un *systemctl status firewalld.service*  
 
 **Algun dels anteriors tallafocs es troba activat?**  
  
  Ara mateix no, ho podem mirar amb la comanda iptables -L  
  
 **Instal.leu el servidor web httpd o nginx i activeu-ne el servei (dnf installl ...  ; systemctl ....). Indiqueu les comandes i comproveu que des d'una altra màquina podeu accedir via web a la vostra IP (digueu-li a un company). Hauria de sortir la plana per defecte.**  
 
 dnf -y install nginx, la meva IP és 192.168.4.02, el meu company hi pot accedir via web si desactivo el firewalld de Linux amb *systemctl stop firewalld.service*, si no diu que no troba cap servidor amb aquella IP.   
 
![](https://github.com/pmartinarnau/m01-2016-2017/blob/master/M01/fotos-lvm/nginx.png)  
  
  Ara mostra el servidor web del meu compay, amb la IP 192.168.4.7, el servidor nginx, al qual s'hi accedeix per el navegador web.  

 
 **Activeu el servei firewalld. Indiqueu com ho feu.**  
  
  systemctl start firewalld.system  
  
 **Comproveu si ara es pot seguir accedint.**  
 
 Ara ja no hi pot accedir, li denega l'accés.  
 
### *Win7*

* * *
 
 **Porta aquest SO algun tallafocs incorporat?**   
 
 Si, en porta, l'anomenen Windows Firewall.  
 
 **Arrenqueu una màquina win7 a isard.escoladeltreball.org. Indiqueu com arribar al tallafocs (passos i pantalles)**  
  Panel de Control --> Sistema y Seguridad --> Firewall de Windows  
  
![](https://github.com/pmartinarnau/m01-2016-2017/blob/master/M01/fotos-lvm/firewall.png)

  
**Es troba activat en aquest windows?**  

 Si, es troba activat per defecte.  
 
 **Busqueu un altre tallafocs per windows. Indiqueu la plana web i les prestacions que ens dona. Intenteu que NOMÉS sigui tallafocs.**  
  
  firewall hands down 
  
  * * *
    
 Pau Martin Arnau
 
