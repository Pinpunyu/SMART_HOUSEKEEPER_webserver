from argparse import ArgumentParser
from bluedot.btcomm import BluetoothClient
import json

def data_send(data):
    print(data)
    

with open('../item.json') as json_file:
    data = json.load(json_file)

print("  user   item  weight")
print("------------------")

for i in data:
    
    if data[i] == None:
        print('%6s   NULL   NULL' %str(i))
        continue 
    
    for j in data[i]:
        print('%6s %6s %6s' %(str(i), str(j), str(data[i][j])))

