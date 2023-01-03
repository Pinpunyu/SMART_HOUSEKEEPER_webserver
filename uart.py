'''
UART communication on Raspberry Pi using Pyhton
https://www.qutaojiao.com
'''
import serial
import time

Uart = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate'
Uart.reset_input_buffer()



#BassTab = [126, 127, 128, 128, 128]
BassTab = [1911,1702,1516,1431,1275,1136,1012]
#x = bin(BassTab[0]).zfill(8)
#print(x)


for i in BassTab:
    data = i.to_bytes(2, byteorder='big')
    Uart.write(data)
    time.sleep(0.1)


#Uart.write(b"121")

'''    
for i in BassTab:
    print(i)
    Uart.write(i)
   '''     
    
        
'''
if Uart.isOpen():
    print("Pi UART is already.")
    try:
        while True:
            Uart.write(b"Hello from Raspberry Pi!\n")
            print(BassTab)
            Uart.write(BassTab)
            time.sleep(1)
            #arduino.write(cmd.encode())
            #time.sleep(0.1) #wait for arduino to answer
            
            while arduino.inWaiting()==0: pass
            if  arduino.inWaiting()>0: 
                answer=arduino.readline()
                print(answer)
                arduino.flushInput() #remove data after reading
            
    except:
        print("error")
'''
'''
while True:
    
    Uart.write(BassTab)
    print(BassTab)
    sleep(5)
    
    for i in BassTab:
        print(i)
        Uart.write(i)
'''
        
'''
 UartSTR = Uart.readline()
 if len(UartSTR) > 2:
  print(UartSTR)
  Uart.write(UartSTR)



while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data.decode())                   #print received data
    #ser.write(received_data)                #transmit data serially 
'''
