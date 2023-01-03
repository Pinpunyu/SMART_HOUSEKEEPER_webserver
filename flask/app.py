from flask import Flask , render_template , request
import json
import subprocess
from argparse import ArgumentParser
from bluedot.btcomm import BluetoothClient
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
import time

app = Flask(__name__)

app.static_folder = "./templates/static"

def getweight():
	
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    hx = HX711(dout_pin=5, pd_sck_pin=6)  # create an object
    weight  = 0
    try:
        for i in range(0,2):
            now_wei = hx.get_raw_data_mean()
            print(now_wei)
            weight += now_wei
        weight /= 2
    except Exception as e:
        print(e)
	#print("end")
    finally:
        GPIO.cleanup()
    return weight

def user_register(user):
    
    with open('../item.json') as json_file:
        data = json.load(json_file)

    if user not in data :
        newuser = {user:None}
        data.update(newuser)
        message = "test"; #send door picture
        reg = subprocess.run(["sudo","python" , "../bludtooth_send.py" , "-message" , message], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        try:
            print(reg.stderr.decode())
            print(reg.stdout.decode())
            with open("../item.json", "w") as outfile:
                json.dump(data, outfile)
            return user + " complete registration."
        
        except:
            return user + " register fail."
        
    else:
        return 'Username has registered.'



def item_register(user, item):

    with open('../item.json') as json_file:
        data = json.load(json_file)

    if user not in data:
        return "User not exist."
    elif item in data[user]:
        return "Item has registered"
    else:
        weight = getweight()
        newitem = {item: weight}
        data[user].update(newitem)
        
        print(newitem)
        reg = subprocess.run(["python" , "../object_detection_yolov5/logIn_obj.py" , "--label",item, "--num","10" ,"--root","../object_detection_yolov5", "--save","../object_detection_yolov5/object_detect_dataset"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        login_result = reg.stdout.decode()
        print(login_result)
        
        if login_result:
            return user+": "+ item+" register fail."
        else:
            with open("../item.json", "w") as outfile:
                json.dump(data, outfile)
                
            return user+": "+ item+" complete registration."

    






@app.route("/")
def hello():
    
    #reg = subprocess.run(["python" , "../total_data.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #data = reg.stdout.decode()
    
    with open('../item.json') as json_file:
        data = json.load(json_file)
    
    return render_template('index.html', data = data)

    
@app.route('/', methods=['POST'])
def main_page(result=None):
    
    funct = request.values['user_input']
    if funct == '1':
        username = request.values['username']
        result = user_register(username)
        
    elif funct == '2':
        username = request.values['username']
        itemname = request.values['itemname']
        result = item_register(username, itemname)
        
    else:
        return 'Hello'+funct
        
    
    with open('../item.json') as json_file:
        data = json.load(json_file)
   
    
    return render_template('index.html', data = data, result = result)


@app.route("/person/<string:user>", methods=['GET'])
def personItem(user):
    
    with open('../item.json') as json_file:
        item = json.load(json_file)
        print(item)
    
    if item[user] == None:
        return "No"
    
    
    detect_item = open("../object_detection_yolov5/detect_result.txt", "r").read()
    detect_item = detect_item.split('\n')
    
    flag = 0
    total_weight = 0
    ori_weight = 0
    for data in detect_item:
        
        print("detect: " + data)
        for item_name in item[user]:
            if item_name == data:
                print(item_name)
                ori_weight += item[user][item_name]
                weight = getweight()
                total_weight += weight
                print(item_name+" weight: "+str(weight))
                
                
    if (ori_weight*0.2) < total_weight and total_weight < (ori_weight*1.8):
        print("BiBi")
        return "Yes"
    else:
        return "No"
    
    
    

if __name__ == "__main__":
    app.run(host="192.168.0.221" , port = 80)
