import serial
import time
import datetime
import djongo
import pymongo
import random
from pymongo import MongoClient

#configuracao do arduino porta e mongo
serial_port = '/dev/ttyACM0'
mongodb_host = 'mongodb://127.0.0.1'
mongodb_db = 'kaora_DB'

#conectando a porta serial
porta = serial.Serial(serial_port, 115200, timeout=0)

#conectando no mongo
client = MongoClient(mongodb_host, 27017)
db = client[mongodb_db]
collection = db['kaorawebpages_dados_musculos']

#configurar para mandar os dados de leitura
intervalo_fixo = 5
while 1:
    try:
        sensor_string = porta.readline().rstrip()
        if sensor_string:
            sensor_C = int(sensor_string)
            collection.insert({'id': 1, 'dadosMusculos': sensor_C, 'dia': datetime.datetime.now()})
            print(str(sensor_C))
    except serial.SerialTimeoutException:
        print('Erro na leitura dos sensores')
    except ValueError:
        print('Erro na conversao da leitura')
    finally:
        time.sleep(intervalo_fixo)

