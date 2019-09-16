


## Object storage

	sudo s3fs w251bucket /mnt/w251bucket -o nonempty -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=http://s3.sjc.us.cloud-object-storage.appdomain.cloud


## MQTT broker on cloud
	docker build -t mosquito -f Dockerfile_broker .
	docker run --name mosquito --network hw03 -p 1883:1883 --rm -ti mosquito


## Image processor with volume mounted at /mnt/w251bucket

	docker build -t saver -f Dockerfile_saver .
	docker run --name saver -v /mnt/w251bucket/:/mnt/w251bucket/ --network hw03 --rm -ti saver