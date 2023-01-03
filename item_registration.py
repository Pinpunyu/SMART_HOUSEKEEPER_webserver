from argparse import ArgumentParser
from bluedot.btcomm import BluetoothClient
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
            print(weight)
        weight /= 3
    except Exception as e:
        print(e)
	#print("end")
    finally:
        GPIO.cleanup()
    return weight


parser = ArgumentParser()
parser.add_argument("-user" , "--U" , dest="user" , default="test")
parser.add_argument("-item" , "--I" , dest="item" , default="test")
user = parser.parse_args().user
item = parser.parse_args().item

with open('../item.json') as json_file:
    data = json.load(json_file)

if user not in data:
    print("User not exist.")
elif item in data[user]:
    print("Item has registered")
else:
    weight = getweight()
    newitem = {item: weight}
    data[user].update(newitem)
    
    #python ../object_detection_yolov5/logIn_obj.py --label eleven --num 10 --root ../object_detection_yolov5  --save ../object_detection_yolov5/object_detect_dataset
    print(newitem)
    #reg = subprocess.run(["pwd"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print(reg.stdout.decode())
    reg = subprocess.run(["python" , "object_detection_yolov5/logIn_obj.py" , "--label",item, "--num",10 ,"--root","object_detection_yolov5", "--save","object_detection_yolov5/object_detect_dataset"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(reg.stderr.decode())
    print(reg.stdout.decode())
    #reg = subprocess.run(["python" , "../object_detection_yolov5/client.py" , "--data","../object_detection_yolov5/object_detect_dataset", "--ip",8888, "--port","192.168.0.63"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print(reg.stdout.decode())
    #python3 client.py --root <根目錄> --data <要訓練資料集的路徑 --ip <連線ip addr>  --port <連線port>
    print(user+": "+ item+" complete registration.")

with open("../item.json", "w") as outfile:
    json.dump(data, outfile)


