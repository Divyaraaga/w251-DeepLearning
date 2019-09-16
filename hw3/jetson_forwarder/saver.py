import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
import random

im = cv.imread('test.png')    
rc,jpg = cv.imencode(".png",im)

num = random.randint(1,101)

path = 'tmp/pic' + str(num) +'.png'
imagefile = open(path, 'wb')
imagefile.write(jpg.tobytes())
imagefile.close()


