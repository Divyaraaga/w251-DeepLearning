import paho.mqtt.client as mqtt
import random

MQTT_HOST="169.61.16.130"
MQTT_PORT=1883
MQTT_TOPIC="facedetection"

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " (rc))


def on_message(client, userdata, msg):
    print("on message received")
    num = random.randint(1,1001)

    path = '/mnt/w251bucket/face' + str(num) +'.png'
    imagefile = open(path, 'wb')
    imagefile.write(msg.payload)
    imagefile.close()


mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect 
mqttclient.on_message = on_message 

mqttclient.connect(MQTT_HOST,MQTT_PORT,60)
mqttclient.subscribe(MQTT_TOPIC, qos=1)

mqttclient.loop_forever()  # Start networking daemon

