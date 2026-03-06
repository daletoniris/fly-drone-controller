import RPi.GPIO as GPIO
import dht11

import json
import MySQLdb
from datetime import date
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import time
import numpy as np
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
pin = rapi = raw_input("Puts pin input raspberry select: ")
instance = dht11.DHT11(pin)
result = instance.read()
fecha = (time.strftime('%d/%m/%y'))
#win = pg.GraphicsWindow()
#win.setWindowTitle('Temp y humedad plotting')

#p1 = win.addPlot()
#win.nextRow()
#p2 = win.addPlot()
#data1 = [0] * 300
#data2 = [0] * 300

#curve1 = p1.plot(data1, name="temp", pen=(255,0,0))
#curve2 = p1.plot(data2, name="hum", pen=(0,255,0))

#def update1():

           #global data1, curve1, result
          # t = float(instance.read['timestamp'])
   # t = float(result.temperature['timestamp'])
    #temp = result.temperature['temp']
    #hum = result.humidity['hum']

           #data1[:-1] = data1[1:]
           #data1[-1] = result.temperature
           #data2[:-1] = data2[1:]
           #data2[-1] = result.humidity
           #curve1.setData(data1)
           #curve2.setData(data2)
#def update():
          # update1()
#timer = pg.QtCore.QTimer()
#timer.timeout.connect(update)
#timer.start(10)
#update1()
while    result.is_valid():
   try:
    #for i in range(0,50): 
       #result = instance.read()
       
       print("Temperature: %d C" % result.temperature)
    
       print("Humidity: %d %%" % result.humidity)
       time.sleep(5)
       db = MySQLdb.connect("localhost","root","1234","temperatura1")
       curs = db.cursor()    
       curs.execute("""INSERT INTO temps(fecha,hum,temp)values(%s,%s,%s)""",(fecha, result.humidity, result.temperature))
       db.commit()
       
   except:
       print("Error: %d" % result.error)
#p1 = win.addPlot()
#win.nextRow()
#p2 = win.addPlot()
#data1 = [0] * 300
#data2 = [0] * 300

#curve1 = p1.plot(data1, name="temp", pen=(255,0,0))
#curve2 = p1.plot(data2, name="hum", pen=(0,255,0))


#def update1():
         
          # global data1, curve1, result
          # t = float(instance.read['timestamp'])
   # t = float(result.temperature['timestamp'])
    #temp = result.temperature['temp']
    #hum = result.humidity['hum']

           #data1[:-1] = data1[1:]
           #data1[-1] = result.temperature
           #data2[:-1] = data2[1:]
           #data2[-1] = result.humidity
           #curve1.setData(data1)
           #curve2.setData(data2)
#def update():
 #          update1()
#timer = pg.QtCore.QTimer()
#timer.timeout.connect(update)
#timer.start(10)
#update1()

