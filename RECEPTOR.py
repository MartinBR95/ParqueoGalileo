import serial
import time

ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout=1) #COM6     = es el puerto en el que entra los datos en modo serial del arduino
                                                        #baudrate = debe estar en la misma velocidad para
                                                        #timeout  = tiempo a esperar

time.sleep(3)                                           #tiempo para que el Arduino inicialice 
dataFile = open('dataFile.txt', 'w')
dataFile.close()


def EscrituraTXT():                                     #aqui esta la funcion que va a generar el txt
    dataFile = open('dataFile.txt', 'w')
    for i in range(0,8):
        Lectura = ser.readline().decode('ascii')        #decode('ascii') hace que se coloquen estos datos como ascii
        dataFile.write(Lectura)

    dataFile.close()
    
        
while (1):
    
    arduinoData = ser.readline()

    if arduinoData == "hola\r\n":
        Data = EscrituraTXT()

        
