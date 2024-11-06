from machine import Pin
import time

# Configuración del LED
led = Pin(2, Pin.OUT)

# Lógica para encender el LED (puedes cambiarla para cualquier funcionalidad)
def encender_led():
    led.on()
    time.sleep(5)
    led.off()

# Llamar a la función para encender el LED
encender_led()
