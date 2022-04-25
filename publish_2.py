import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import json


flag=0

def mul(l):
	f=1
	for i in l:
		f=f*i
	return f


def subtract(l):
	f=l[0]
	for i in range(1,len(l)):
		f=f-l[i]
	return f


def div(l):
	f=l[0]

	if(len(l)==2 and l[1]!=0):
		f=l[0]/l[1]
	else:
		flag=-1
		# print(flag)
		print("Not possible!!")
	return f



def calculator(l,symbol):
	ans=0
	# if(symbol=="+"):
	# 	ans=0
	# if(symbol=="-"):
	# 	ans=l[0]
	# if(symbol=="*"):
	# 	ans=1
	# if(symbol=="/"):
	# 	ans=l[0]
	
	if(symbol=="+"):
		# ans=0
		for i in l:
			ans=ans+i
		# return ans
	elif(symbol=="-"):
		# ans=l[0]

		# for i in l:
		# 	ans=ans-i
		ans=subtract(l)
		# return ans
	elif(symbol=="*"):
		# ans=1
		# for i in l:
		# 	ans=ans*i
		# return ans
		ans=mul(l)

	elif(symbol=="/"):
		# ans=l[0]
		ans=div(l)
		# if(len(l)==2):
		# 	if(l[1]==0):
		# 		print("divide by zero error!!")
		# 	else:
		# 		ans=l[0]/l[1]
		# else:
		# 	print("length isn not compatible for divide!!")
		# return ans
	return ans


		




def on_message(client,userData,message):
	vipul=str(message.payload.decode("utf-8"))
	king=json.loads(vipul)
	bh=[]

	bh=king["params"]
	op=king["reqMethod"]
	ans=calculator(bh,op)
	p=0
	if(flag==-1):
		p=-1
		ans="Not possible!!"
	d={"code":p,"req_id":king["req_id"],"result":ans}
	xyz="0"
	xyz=str(ans)
	client.publish("CALCULATOR",xyz)
	# client.publish("CALCULATOR",d)
	print(ans)
	# print(flag)
	print(d)


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Client2")
print("client2 connected to broker!")
client.connect(mqttBroker)

client.loop_start()
# print("sending data")
client.subscribe("CALCULATOR")
client.on_message=on_message
time.sleep(20)
client.loop_stop()
