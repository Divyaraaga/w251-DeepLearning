import paho.mqtt.client as mqtt

MQTT_HOST="172.20.0.2"
MQTT_PORT=1883
MQTT_TOPIC="hw3"

CLOUD_MQTT_HOST="169.61.16.130"
CLOUD_MQTT_PORT=1883
CLOUD_MQTT_TOPIC="facedetection"

def on_connect(client, userdata, flags, rc):
    print("Connected to jetson")

def on_connect_cloud(client, userdata, flags, rc):
    print("Connected to cloud")

def on_message(client, userdata, msg):
    print("on message received")
    cloudmqttclient.publish(CLOUD_MQTT_TOPIC,payload=msg.payload,qos=0,retain=False)

cloudmqttclient = mqtt.Client()
cloudmqttclient.connect(CLOUD_MQTT_HOST,CLOUD_MQTT_PORT,60)
cloudmqttclient.on_connect = on_connect_cloud 

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect 
mqttclient.on_message = on_message 

mqttclient.connect(MQTT_HOST,MQTT_PORT,60)
mqttclient.subscribe(MQTT_TOPIC, qos=1)

mqttclient.loop_forever()  # Start networking daemon
