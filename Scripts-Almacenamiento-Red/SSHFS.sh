#!/bin/bash 

cd /tmp/

yum install -y epel-release > /dev/null

yum install -y sshfs > /dev/null

systemctl start sshd

systemctl enable sshd

echo "A qué IP te quieres conectar? "

read ip

echo "Con que usuario? "

read user

echo "Que ruta quieres montar? "

read ruta_server

echo "Donde quieres montarlo?"

read ruta_destino

echo "Ahora nos vamos a conectar: "

sshfs $user@$ip:$ruta_server $ruta_destino
