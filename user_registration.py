from argparse import ArgumentParser
from bluedot.btcomm import BluetoothClient
import json
import subprocess

def data_send(data):
    print(data)


parser = ArgumentParser()
parser.add_argument("-user" , "--U" , dest="user" , default="test")
user = parser.parse_args().user

with open('../item.json') as json_file:
    data = json.load(json_file)

if user not in data :
    newuser = {user:None}
    data.update(newuser)
    #message = ""; #send door picture
    #subprocess.run(["python" , "../bludtooth_send.py" , "-message" , message], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(user + " complete registration.")
    
else:
    print('Username has registered.')
    
with open("../item.json", "w") as outfile:
    json.dump(data, outfile)


