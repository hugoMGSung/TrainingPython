import serial

port = '/dev/ttyACM0'
brate = 9600 #boudrate
cmd = 'temp'

ser = serial.Serial(port, baudrate=brate, timeout=None)
print(ser.name)

while True:
    key = input('Enter count : ')
    ser.write(int(key))