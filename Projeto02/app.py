# Importar bibliotecas
from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
import serial

# Inicia comunicação serial arduino
comunicacaoSerial = serial.Serial('/dev/ttyUSB0', 9600)

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
rele = 16
GPIO.setup(rele, GPIO.OUT)
GPIO.output(rele, GPIO.HIGH)


# Cria Rota principal e chama arquivo html
@app.route("/")
def main():
    return render_template('index.html')


# Cria rota dos botões
@app.route("/<pin>/<action>")
def sensor(pin, action):
    temperature = ''
    humidity = ''

    # verifica se o botão da ventilção foi acionado para ligar ou desligar
    if pin == "rele" and action == "on":
        GPIO.output(rele, GPIO.LOW)
        print('on')
    if pin == "rele" and action == "off":
        GPIO.output(rele, GPIO.HIGH)
        print('off')

    # Limpa flush da comunicação serial
    comunicacaoSerial.flush()
    comunicacaoSerial.flushInput()
    comunicacaoSerial.flushOutput()
    time.sleep(2)  # aguarda 200 ms para receber a leitura atual

    # Lê a comunicação serial
    dados = comunicacaoSerial.readline()

    # trata a string para obter somente os valores desejados
    string_a_tratar = str(dados)
    temp_and_hum = string_a_tratar.split("e")
    umidade = temp_and_hum[0].split("b'")
    temperatura = temp_and_hum[1].split("\\r")

    umidade_float = float(umidade[1])
    temperatura_float = float(temperatura[0])

    # formata para 1 casa decimal
    humidity = '{0:0.1f}'.format(umidade_float)
    temperature = '{0:0.1f}'.format(temperatura_float)
    print(humidity)
    print(temperature)

    templateData = {
        'temperature': temperature,
        'humidity': humidity
    }
    # chama o html mandando os parâmetros do sensor
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
