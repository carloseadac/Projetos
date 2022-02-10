
import requests
import json
import matplotlib.pyplot as plt

"""
temperatura=[]
umidade=[]

proxies = {'https': "http://disrct:saladigital0311@10.224.200.26:8080/"}

for i in range(5):
    temp = "https://projetinho-fellas-default-rtdb.firebaseio.com/Sensor/temperatura.json"
    umi = "https://projetinho-fellas-default-rtdb.firebaseio.com/Sensor/umidade.json"
    temperatura.append(float(requests.get(temp, proxies=proxies).content))
    umidade.append(float(requests.get(umi, proxies=proxies).content))
    print("temperatura: ", temperatura)
    print("Umidade: ", umidade)



plt.plot(temperatura, label='Temperatura')
plt.plot(umidade, label ='Umidade')
plt.legend()
plt.title("Dados DHT")
plt.show()
"""

def sinal():
 proxies = {'https': "http://disrct:saladigital0311@10.224.200.26:8080/"}
 lumi = "https://projettaprata-default-rtdb.firebaseio.com/Sensor/luminosidade.json"
 luminosidade = int(requests.get(lumi, proxies=proxies).content)
 return luminosidade

import pyodbc
def InserirBD(sinal):
 server = 'JVLPC0587\SQLSERVER'
 database = 'db_firebase_carlo'
 username = 'carlo'
 password = 'carlo'
 cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
 cursor = cnxn.cursor()
 cursor.execute(f"INSERT dbo.Sensor (luminosidade) VALUES ({sinal});")
 cursor.commit()
 print("Inserido com sucesso!")
 
 

import numpy as np

server = 'JVLPC0587\SQLSERVER'
database = 'db_firebase_carlo'
username = 'carlo'
password = 'carlo'
driver= '{ODBC Driver 17 for SQL Server}'

conn= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor=conn.cursor()

cursor.execute("SELECT Luminosidade, timestamp FROM dbo.Sensor")
row = cursor.fetchone()

lista=[]
listatempo=[]

while row:
    lista.append(row[0])
    listatempo.append(str(row[1])) 
    row = cursor.fetchone()
    
    
def apresentar(sinal):
 print(f"Luminosidade: {sinal[0]}")

import time
while True:
     valores=sinal()
     apresentar(valores)
     InserirBD(valores)
    
    
    