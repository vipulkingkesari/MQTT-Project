import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

import json

def on_message(client,userData,message):
	vipul=str(message.payload.decode("utf-8"))
	# print(vipul)

mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client("Client1")
print("client1 connected to broker!!")
client.connect(mqttBroker)
x=[]
x=[int(item) for item in input("Enter the parameters : ").split()]
# x=[1,2,3]
n=int(input("Enter the req_id : "))
# n=1234
operation=input("Enter the operation which need to perform : ")
# operation="+"


d={"req_id":n,"reqMethod":operation,"params":x}
d=json.dumps(d)
# print(d)
client.publish("CALCULATOR",d)
client.loop_start()
client.subscribe("CALCULATOR")
client.on_message=on_message
time.sleep(10)
client.loop_stop()