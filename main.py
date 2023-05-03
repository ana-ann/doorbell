#!/usr/bin/python3
# Also Compatible with Pi HQ Camera. This can be modified to suit your application.
#Implented for one client device to stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
from time import sleep
import threading
import os
import sys
from signal import pause, signal, SIGTERM, SIGHUP
import gpiozero
from gpiozero import Button, LED
import subprocess
import http.client, urllib
import time as t
from multiprocessing import Process
import pygame
pygame.init()


button = Button(4)
DOOR_LOCK_PIN = 26
IR_PIN = 19

door_lock = gpiozero.OutputDevice(DOOR_LOCK_PIN, active_high=False, initial_value=False)
ir = gpiozero.OutputDevice(IR_PIN, active_high=False, initial_value=False)


def safe_exit(signum, frame):
    exit(1)

# App Globals (do not edit)
app = Flask(__name__)


#my_sound = pygame.mixer.Sound('path/to/my/soundfile.wav')

#background process happening without any refreshing
@app.route('/lock')
def lock():
    print ("Close")
    sleep(3)
    stop()
    return ("nothing")

@app.route('/unlock')
def unlock():
    print ("Open")
    door_lock.on()
    sleep(5)
    door_lock.off()
    sleep(5)
    stop()       
    return ("nothing")

@app.route('/post')
def post():
    print ("Open")
    my_sound.play()
    door_lock.on()
    sleep(5)
    door_lock.off()
    sleep(5)
    stop()       
    return ("nothing")


@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def stop():
    print("This is stop")
    button.close()
    ir.off()
    sys.stdout.flush()
    sleep(1)
    subprocess.run(['./script.sh'])
        
def start():
    app.run(host='0.0.0.0', debug=False)
    print ("i am here")
    
def handy():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": "your_token",	#put your token here
            "user": "your_username",	#put your username here
            "message": "http://raspberry_pi_ip:5000",   #put your Raspberry IP here
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    
def tablet():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": "your_token",	#put your token here
            "user": "your_username",	#put your username here
            "message": "http://raspberry_pi_ip:5000",    #put your Raspberry IP here
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    

try:
    
    p1 = Process(target=start)  
    p2 = Process(target=tablet)
    p3 = Process(target=handy)
    
    button.wait_for_press()
    p2.start()
    p1.start()
    ir.on()
    sleep(40)
    p3.start()
    sleep(150)
    print ("try here")
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    
    
except KeyboardInterrupt:
    print ("Interrupted with Ctrl+C!")
    

finally:
    button.close()
    ir.off()
    sys.stdout.flush()
    sleep(1)
    subprocess.run(['./script.sh'])
    

   
