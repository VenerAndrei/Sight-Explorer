import socket
import RPi.GPIO as GPIO
import time

HOST = '192.168.0.106'  # The server's hostname or IP address
PORT = 1234        # The port used by the server

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

left = GPIO.PWM(24,50);
left.start(0);
right = GPIO.PWM(25,50);
right.start(0);

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    raw_data = s.recv(1024)
    while raw_data:
        raw_data = s.recv(1024)
        if not raw_data:
            break
        data = raw_data.decode("utf-8")
        print(data + '\n')
        data = data.split(';');
        right_x = float(data[1]);
        left_x = float(data[3]);
        print(data[1]+ '\t' + data[3] + '\n');

        if(right_x < -0.2):
            GPIO.output(12,GPIO.LOW)
            GPIO.output(16,GPIO.HIGH)
            right.ChangeDutyCycle(-right_x*100)
        elif(right_x > 0.2):
            GPIO.output(16,GPIO.LOW)
            GPIO.output(12,GPIO.HIGH)
            right.ChangeDutyCycle(right_x*100)
        else:
            right.ChangeDutyCycle(0);



        if(left_x < -0.2):
            GPIO.output(20,GPIO.LOW)
            GPIO.output(21,GPIO.HIGH)
            left.ChangeDutyCycle(-left_x*100)

        elif(left_x > 0.2):
            GPIO.output(21,GPIO.LOW)
            GPIO.output(20,GPIO.HIGH)
            left.ChangeDutyCycle(left_x*100)
        else:
            left.ChangeDutyCycle(0);


print('Connection ended. Exit encoded string:   ', repr(data))
