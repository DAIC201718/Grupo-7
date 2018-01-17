#!/usr/bin/python
# -*- coding: utf-8 -*-
import math, signal, sys, os, time, requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
while True:
        if GPIO.input(21) == True:
                print "Necesitas recargar el nivel de liquido"
                time.sleep(1)
        else:
                print "El nivel de liquido es el adecuado"
                time.sleep(1)

        url = 'https://corlysis.com:8086/write'
        params = {"db": "raspberrypi7", "u": "token", "p": "693542bf37490ccfef5f1f33fd9827f0"}
        payload = "Liquido,place=L value={0:0.1f}".format(GPIO.input(21))
        r = requests.post(url, params=params, data=payload)

