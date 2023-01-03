from bluedot.btcomm import BluetoothClient
from signal import pause
from argparse import ArgumentParser
import time

parser = ArgumentParser()
parser.add_argument("-message" , "--M" , dest="msg" , default="test")


msg = parser.parse_args().msg

def data_send(data):
    print(data)

c = BluetoothClient("E4:5F:01:C5:94:78", data_send)
c.send(msg)

time.sleep(10)
