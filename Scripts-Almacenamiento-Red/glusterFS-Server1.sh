#!/bin/bash

# Instalamos glusterfs  

yum search centos-release-gluster > /dev/null

yum install -y centos-release-gluster40.x86_64 > /dev/null

yum install -y glusterfs glusterfs-cli glusterfs-libs glusterfs-server > /dev/null

systemctl start glusterd > /dev/null

systemctl enable glusterd > /dev/null

yum update -y > /dev/null

# Desactivamos iptables y firewalld

systemctl stop firewalld

systemctl disable firewalld

iptables -F

# Desactivamos completamente SELinux.

echo "
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#   	enforcing - SELinux security policy is enforced.
#   	permissive - SELinux prints warnings instead of enforcing.
#   	disabled - No SELinux policy is loaded.
SELINUX=disabled
# SELINUXTYPE= can take one of these two values:
#   	targeted - Targeted processes are protected,
#   	mls - Multi Level Security protection.
SELINUXTYPE=targeted" > /etc/sysconfig/selinux

# Preguntamos los Hosts y la IP remota

echo "Que Hostname quieres utilizar? "

read hostname

echo "Que IP va a tener el otro servidor? "

read ip_server_remoto

echo "Cual es el Hostname de la otra máquina? "

read hostname_remoto

# Añadimos también el Hostname, lo hacermos en este archivo porque el /etc/hostname sólo
# lo lee al iniciar el sistema y tendriamos que reiniciar el sistema para que funcionara.

echo $hostname > /proc/sys/kernel/hostname

ip_user=`hostname -I`

# Añadimos en /etc/hosts en ambos servidores: (Las direcciones con los Hostname para que haga la resolución)

echo "127.0.0.1 localhost.localdomain localhost
$ip_user$hostname
$ip_server_remoto $hostname_remoto" > /etc/hosts

# Añadimos el Host remoto a nuestra pool

gluster peer probe $ip_server_remoto

# Creamos el volumen GlusterFS

echo "Que carpeta local quieres replicar como volumen? (Ruta completa)"

read  ruta_origen

echo "A que carpeta remota quieres replicarlo?"

read  ruta_destino

echo "Que nombre quieres darle al volumen? "

read  nombre_vol

mkdir -p $ruta_origen/nombre_vol > /dev/null

gluster volume create $nombre_vol replica 2 $hostname:$ruta_origen/$nombre_vol $hostname_remoto:/$ruta_destino/$nombre_vol force

gluster volume start $nombre_vol

# Ahora podriamos confirmar el estado del volumen si descomentamos esta línea.

# gluster volume info
 
# Montamos el volumen en un directorio bajo “/mnt”: (En server1)

echo "Ahora vamos a montar el volumen, en que directorio quieres montarlo? "

read directorio_montaje
 
umount $directorio_montaje > /dev/null

mount -t glusterfs $hostname:/$nombre_vol $directorio_montaje
