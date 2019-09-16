import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

MQTT_HOST="172.20.0.2"
MQTT_PORT=1883
MQTT_TOPIC="hw3"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc))) 

mqttclient=mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST,MQTT_PORT,60)

face_cascade = cv.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(1)

while(True):

    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        face = frame[y:y+h,x:x+w]
        print("face detected ",face.shape,face.dtype)
        rc,jpg = cv.imencode(".png",face)
        msg = jpg.tobytes()
        mqttclient.publish(MQTT_TOPIC,payload=msg,qos=2,retain=False)
    
# When everything is done, release the capture
video_capture.release()
cv.destroyAllWindows()
