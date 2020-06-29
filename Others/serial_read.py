import serial

port = '/dev/ttyACM0'
brate = 9600 #boudrate
cmd = 'temp'

ser = serial.Serial(port, baudrate=brate, timeout=None)
print(ser.name)

while True:
    if ser.in_waiting != 0:
        content = ser.readline()
        print(content[:-2].decode())