# -*- coding: utf-8 -*-

import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('FLY & HACK 1.0', font='starwars'),
       'white',  attrs=['bold'])
print """
Fly & Hack is a complete laboratory created to help the world understand
more about drones.
Drone Lab lets you create everything you want with the drone, make hacking
sensors integrate him, blow it up from any device and learn all
you need to move forward with the development and research open drones.

Author: Daniel Dieser daletoniris@gmail.com
web: www.niperia.com

============================================================================

"""

import os
import sys

ans=True
while ans:
    print ("""
    1.Control joystick pc/Rasp-Pi
    2.Control Joystick pc/pc
    3.Plot acc gcc
    4.Sensor temp/hum
    5.Sensor gas/others
    6.Wep pentest
    7.Wps pentest
    8.Wpa/Wpa2 pentest
    9.A.I / Camera actions
    10.Exit
    """)
    ans=raw_input("Que es lo quieres hacer? ") 
    if ans=="1":
      os.system("sudo python mw-joystick.py")
 
      print("\n Cliente iniciando...") 
    elif ans=="2":
      os.system("sudo python send-joystick.py")
      print("\n Server pilot start..") 
    elif ans=="3":
      print("\n plot sensor...")
      os.system("sudo python modules/test-imu-plot2.py")
    elif ans=="6":
      os.system("sudo python /usr/bin/wifite -wep")
      print("\n buscando target...")
    elif ans=="8":
      os.system("sudo python /usr/bin/wifite -wpa")
      print("\n buscando target...")

    elif ans=="9":
      print " 9.1. Streaming video"
      print " 9.2. Deteccion de rostro"
      print " 9.3. Deteccion de movimiento"
      print " 9.4. Trackeo de objetos"
      print " 9.5. Re/Training de maquina"
      print " 9.6. Reconocimiento automatico"
      print("\n ")
    elif ans=="9.1":
      os.system("sudo raspivid -n -t 0 -w 640 -h 480 -fps 10 -o - | nc -u 192.168.1.102 5001")
      print("\n Iniciando streaming...")
    elif ans=="9.2":
      os.system("sudo python modules/camera/rpi-opencv/face-detection.py")
    elif ans=="9.5":
      os.system("sudo python tensor/retrain.py --image_dir=tensor/flower_photos")

    elif ans=="9.6":
      os.system("sudo python final.py flower_photos/margarita/9350942387_5b1d043c26_n.jpg ")    
    elif ans !="":
      print("\n No esta disponible intente otra")
      
 
    elif ans=="4":
      print " 4.1. Setup base de datos"
      print " 4.2. Leer temperatura y humedad" 
      print " 4.3. Exportar lecturas a csv"
      print " 4.4. Plot de lecturas"         
      print("\n ")
    elif ans=="4.1":
      os.system("sudo python New/DHT11_Python-master/csvplot.py") 
    elif ans=="4.2":
      os.system("sudo python Adafruit_Python_DHT-master/examples/dhtprueba.py")
    elif ans !="":
      print("\n No esta disponible intente otra") 


    
