
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Programa que permite obtener la lectura de un se$
# Lenguaje     : Python
# Autor        : Jose Zorrilla <jzorrilla@iot.cl>
# Dependencias : Libreria de Adafruit https://github.com/adafruit$
# Web          : http://internetdelascosas.cl/

# Importa las librerias necesarias
import RPi.GPIO as GPIO
import sys
import time
import Adafruit_DHT
import datetime
import requests
# Configuracion del tipo de sensor DHT
sensor = Adafruit_DHT.DHT11

# Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
pin = 23
#instance = dht11.DHT11(pin=23)

# Intenta ejecutar las siguientes instrucciones, si falla va a la
while True:

        # Obtiene la humedad y la temperatura desde el sensor
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        # Imprime en la consola las variables temperatura y humed
        print('Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad))



        if (temperatura) >= 22:
                humedad, temperatura = Adafruit_DHT.read_retry(sensor,pin)
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(17, GPIO.OUT)
                GPIO.output(17,True)
                print('El ventilador esta activado')
                url = 'https://corlysis.com:8086/write'
                params = {"db": "raspberrypi7", "u": "token", "p": "693542bf37490ccfef5f1f33fd9827f0"}
                payload = "Temperatura,place=T value={0:0.1f}".format(temperatura)
                r = requests.post(url, params=params, data=payload)
                payload2 = "Humedad,place=H value={0:0.1f}".format(humedad)
                r2 = requests.post(url, params=params, data=payload2)

        if (temperatura) <= 21:
                humedad, temperatura = Adafruit_DHT.read_retry(sensor,pin)


