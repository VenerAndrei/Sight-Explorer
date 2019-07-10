import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(12,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.LOW)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

s = GPIO.PWM(24,50);
s.start(0);
d = GPIO.PWM(25,50);
d.start(0);

s.ChangeDutyCycle(35)
d.ChangeDutyCycle(35)
while(1):
    x = raw_input()
    if(x=='w'):
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
    if(x=='s'):
        GPIO.output(16,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(20,GPIO.HIGH)
    if(x=='p'):
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
    if(x=='a'):
        GPIO.output(16,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(21,GPIO.HIGH)
        GPIO.output(20,GPIO.LOW)
    if(x=='d'):
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(20,GPIO.HIGH)
