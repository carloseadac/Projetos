# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:40:22 2021

@author: DISRCT
"""
import paho.mqtt.client as mqtt
import time
import socket

socket.getaddrinfo('localhost', 8080)

def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("Cliente conectado ao Broker!\n")
		try:
			client.subscribe("Treinamento/ets/leonardo", qos=0)
			print("Cliente inscrito no tópico!\n")
         
		except:
			print("Não foi possível inscrever o cliente no tópico\n")
	else:
		print("Cliente não conectado ao Broker.\n")


def on_disconnect(client, userdata, rc):
	if rc != 0:
		print("Cliente desconectado do Broker inesperadamente.\n")	


def on_message(client, userdata, msg):
	msgPayload = str(msg.payload.decode('utf-8'))
	msgTopic = str(msg.topic)
	print(msgPayload + "\n")


broker_address='broker.hivemq.com'
broker_port=1883


client = mqtt.Client()
client.proxy_set(proxy_type=socks.HTTP, proxy_addr='https://disrct:saladigital0311@10.224.200.26:8080', proxy_port=proxy_port)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
print("Conectando ao Broker")
client.connect(broker_address, broker_port)
print("Broker!!")
time.sleep(4)
client.loop_forever()


