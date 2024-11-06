import network
import socket
import machine
import os

# Configura el Wi-Fi
SSID = 'Tu_SSID'
PASSWORD = 'Tu_Contraseña'

def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Conectando a Wi-Fi...")
    while not wlan.isconnected():
        pass

    print("Conexión exitosa!")
    print("IP:", wlan.ifconfig()[0])

def iniciar_servidor_ota():
    # Servidor simple para recibir archivos OTA por socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8266))  # Puerto 8266
    s.listen(1)
    print("Esperando conexión OTA...")

    while True:
        conn, addr = s.accept()
        print(f"Conexión desde {addr}")

        # Recibir archivo OTA
        with open("main.py", "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        
        print("Archivo OTA recibido, reiniciando...")
        conn.close()
        machine.reset()

# Ejecuta el programa
conectar_wifi()
iniciar_servidor_ota()