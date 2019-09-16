
## Face detector on Jetson
   	docker build -t detector -f Dockerfile_fd .
   	docker run --name detector --network hw03 -e DISPLAY=$DISPLAY --privileged -v /tmp:/tmp --rm -ti detector

   Detector is publishing png of faces to broker with topic: hw3 and QoS 2, which is send the message Exactly once 
    
## MQTT broker on jetson
	docker build -t mosquitto -f Dockerfile_broker .
   	docker run --name mosquitto --network hw03 -p 1883:1883 --rm -ti mosquitto
	
## Forwarder on jetson
	docker build -t mosquitto -f Dockerfile_broker .
   	docker run --name mosquitto --network hw03 -p 1883:1883 --rm -ti mosquitto    
   
   Forwarder is subscribing messages for the topic hw3 from detector with QoS 2 and publishing messages to MQTTbroker in cloud    with topic facedetection and QoS 2.
    
## MQTT broker on cloud
	docker build -t mosquito -f Dockerfile_broker .
	docker run --name mosquito --network hw03 -p 1883:1883 --rm -ti mosquito

## Image processor with volume mounted at /mnt/w251bucket

	docker build -t saver -f Dockerfile_saver .
	docker run --name saver -v /mnt/w251bucket/:/mnt/w251bucket/ --network hw03 --rm -ti saver
 
  Image processor is subscribing messages for the topic facedetection with QoS 2 and saves the faces in object storage bucket with the name w251bucket.
  
Location of bucket: 
 
## Object storage

	sudo s3fs w251bucket /mnt/w251bucket -o nonempty -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=http://s3.sjc.us.cloud-object-storage.appdomain.cloud


