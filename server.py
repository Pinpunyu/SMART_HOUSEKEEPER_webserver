from bluedot.btcomm import BluetoothServer
from signal import pause
import json
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
import time
import subprocess

def getweight():
	
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    hx = HX711(dout_pin=5, pd_sck_pin=6)  # create an object
    first = hx.get_raw_data_mean()
    weight  = 0
    try:
        for i in range(0,3):
            weight += (hx.get_raw_data_mean()-first)
        weight /= 3
    except Exception as e:
        print(e)
	#print("end")
    finally:
        GPIO.cleanup()
    return weight

def data_received(data):
    print(data)
    s.send(data)

#s = BluetoothServer(data_received)
user = "Yui"
with open('item.json') as json_file:
    item = json.load(json_file)
print(item[user])

for idx in range(0,1):
    detect_item = open("object_detection_yolov5/detect_result.txt", "r").read()
    detect_item = detect_item.split('\n')[0]
    print(detect_item)
    
    
    for name in item[user]:
        print(name)
        print(item[user][name])
        if name == detect_item:
            ori_weight = item[user][name]
            weight = getweight()
            print("weight: ")
            print(weight)
            if (ori_weight*0.1) < weight and weight < (ori_weight*1.9):
                print("BiBi")
                message = ""
                reg = subprocess.run(["python" , "bludtooth_send.py" , "-message" , message], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.1)

#pause()
