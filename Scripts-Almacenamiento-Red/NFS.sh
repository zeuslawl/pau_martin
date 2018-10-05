#!/bin/bash

apt-get update & apt-get upgrade

apt-get install nfs-kernel-server nfs-common

echo "Quina ruta vols compartir? Es compartira a tothom com a (rw), però segons els teus permisos només serà (ro)"
echo
echo "Format: /ruta"
read ruta

echo "
# /etc/exports: the access control list for filesystems which may be exported
#           	to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes   	hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4    	gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#

# Compartir la carpeta que ens demani l'usuari amb permisos rw.
$ruta *(rw)" > /etc/exports

# Si et surt que el servei nfs-common està "Masked", activa les següents líneas:

#cat >/etc/systemd/system/nfs-common.service <<\EOF
#[Unit]
#Description=NFS Common daemons
#Wants=remote-fs-pre.target
#DefaultDependencies=no
#
#[Service]
#Type=oneshot
#RemainAfterExit=yes
#ExecStart=/etc/init.d/nfs-common start
#ExecStop=/etc/init.d/nfs-common stop
#
#[Install]
#WantedBy=sysinit.target
#EOF
systemctl restart nfs-kernel-server.service
systemctl restart nfs-common.service
