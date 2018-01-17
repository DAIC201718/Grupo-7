
#!/usr/bin/python
# -*- coding: utf-8 -*-
import math, signal, sys, os, time, requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
vuelta = 0
max = 10
while vuelta < max:
        if GPIO.input(24) == False:
                print "No detecta"
                print vuelta
                time.sleep(1)
        else:
                print "Detecta"
                vuelta = vuelta + 1
                print vuelta
                time.sleep(1)
        url = 'https://corlysis.com:8086/write'
        params = {"db": "raspberrypi7", "u": "token", "p": "693542bf37490ccfef5f1f33fd9827f0"}
        payload = "Bateria,place=V value={0:0.1f}".format(vuelta)
        r = requests.post(url, params=params, data=payload)

print "Bateria llena"

