import subprocess as sp
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def ejecutar_programa():
    sp.call("chmod +x botones.sh", shell=True)
    sp.call("./botones.sh", shell=True)
	


while True:
    input_state=GPIO.input(18)
    if input_state==False:
        print('Boton presionado')
	ejecutar_programa()
        time.sleep(0.2)
