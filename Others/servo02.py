import RPi.GPIO as GPIO
import time

servoPin = 23
SERVO_MAX_DUTY = 12 # 서보 최대180도 위치 주기
SERVO_MIN_DUTY = 3  # 써뽀 최쏘0도 위치 쭈끼

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)

m = GPIO.PWM(servoPin, 50)
m.start(0)

def setServoPos(degree):
    if degree > 180:
        degree = 180
    
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    print('Degree {} to {}'.format(degree, duty))
    m.ChangeDutyCycle(duty)

if __name__ == '__main__':
    setServoPos(0)
    time.sleep(3)
    setServoPos(90)
    time.sleep(3)
    setServoPos(180)
    time.sleep(3)

    m.stop()
    GPIO.cleanup()