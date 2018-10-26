#!/usr/bin/env python 

#modulos de comunicacao serial e de tempo
import serial
import time

# classe de comunicacao com o Arduino
class Arduino(object):
    def conecta_sensor(self, porta, sensor_velocidade):
        self.arduino = serial.Serial(porta, sensor_velocidade)
        time.sleep(2)

    def insere_dado_musculo(self, dado_musculo):   
        self.arduino.write(dado_musculo)

    def le_dado_musculo(self):
        return self.arduino.readline()

# programa principal
if __name__ == '__main__':
    
    # modulos de integracao com DJANGO
    import os
    import sys
    import json

    #se identificar configuracao DJANGO importa a classe model
    if os.environ.setdefault('DJANGO_SETTINGS_MODULE','kaorawebprojeto.settings'):
        from kaorawebpages.models import Dados_Musculos
        from django.utils import timezone

    else:
        sys.exit(2)

    #definir porta e velocidade arduino
    PORTA_SERIAL = '/dev/ttyACM0'
    SERIAL_BEGIN = 115200

    # objeto do tipo arduino
    arduino = Arduino()
    arduino.conecta_sensor(PORTA_SERIAL, SERIAL_BEGIN)

    # indicar leitura do arduino
    arduino.insere_dado_musculo(1)

    # receber dados da leitura do musculo
    recebe_dados_musculos = json.loads(arduino.le_dado_musculo())

    # objeto para leitura
    ler_dados_musculos = Dados_Musculos()
    ler_dados_musculos.dados_musculos = recebe_dados_musculos['dados_musculos']
    ler_dados_musculos.data = timezone.now()

    # salvar leitura no banco
    ler_dados_musculos.save()
