#!/usr/bin/env python3
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
import time

GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
hx = HX711(dout_pin=5, pd_sck_pin=6)  # create an object
#first = hx.get_raw_data_mean()
#print(first)
weight  = 0
try :
	for i in range(0,100):
		ori = hx.get_raw_data_mean()
		print(ori)  # get raw data reading from hx711
		#weight += (hx.get_raw_data_mean())
		#time.sleep(1);
	weight /= 10
	print("weight: ")
	print(weight)
	

except Exception as e:
    print(e)
	#print("end")
finally:
	GPIO.cleanup()
