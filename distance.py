'''
UART communication on Raspberry Pi using Pyhton
https://www.qutaojiao.com
'''
import serial
import time
    
import threading

ser = serial.Serial ("/dev/ttyS0", 38400)    #Open port with baud rate'
#ser.reset_input_buffer()

def sendSound():
    BassTab = [1911,1702,1516,1431,1275,1136,1012]
   
    for i in BassTab:
        data = i.to_bytes(2, byteorder='big')
        ser.write(data)
        time.sleep(0.01)


#t = threading.Thread(target = sendSound)

dis = 0;
while True:
    received_data = ser.read()              #read serial port
    time.sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    
    if dis > 50 and float(received_data.decode()) < 50:
        sendSound()
        
    dis = float(received_data.decode())
        
    print (received_data.decode())                   #print received data
    #ser.write(received_data)                #transmit data serially 

