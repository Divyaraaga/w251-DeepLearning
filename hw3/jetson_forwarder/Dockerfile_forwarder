From alpine

RUN apk update
RUN apk add mosquitto-clients
RUN apk add py2-paho-mqtt

RUN mkdir forwarder
COPY . /forwarder
WORKDIR /forwarder

ENTRYPOINT ["python" ]
CMD ["forwarder.py" ]
