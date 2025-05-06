# Simulación de Caja Negra para Auto Escolar
# Para MicroBit usando Python en https://python.microbit.org/v/3

from microbit import *
import random

# Constantes
MAX_REGISTROS = 20  # Reducido para ahorrar memoria en MicroBit

# Variables globales
registros = []  # Lista para almacenar los datos registrados
grabando = False  # Estado de grabación
intervalo_ms = 2000  # Intervalo de registro en milisegundos (2 segundos)
ultima_grabacion = 0  # Tiempo de la última grabación

# Función para simular la lectura de sensores
def leer_sensores():
    # En un sistema real, estos valores vendrían de sensores físicos
    velocidad = random.randint(0, 80)  # Velocidad simulada (0-80 km/h)
    aceleracion = random.randint(-20, 20) / 10  # Aceleración simulada (-2 a 2 m/s²)
    ubicacion_x = random.randint(0, 100)  # Posición X simplificada
    ubicacion_y = random.randint(0, 100)  # Posición Y simplificada
    
    # Crear registro como tupla (más eficiente en memoria que objetos)
    return (running_time(), velocidad, aceleracion, (ubicacion_x, ubicacion_y))

# Función para iniciar la grabación
def iniciar_grabacion():
    global grabando, registros, ultima_grabacion
    registros = []  # Limpiar registros anteriores
    grabando = True
    ultima_grabacion = running_time()
    display.scroll("REC", delay=80)
    display.show(Image.HEART)

# Función para detener la grabación
def detener_grabacion():
    global grabando
    grabando = False
    display.scroll("STOP", delay=80)
    display.show(Image.SQUARE)

# Función para mostrar los datos registrados
def mostrar_registros():
    if not registros:
        display.scroll("No hay datos", delay=80)
        return
    
    display.scroll(str(len(registros)) + " reg", delay=80)
    
    for i, reg in enumerate(registros):
        if button_a.is_pressed() and button_b.is_pressed():
            # Permitir salir de la visualización presionando ambos botones
            break
            
        # Mostrar número de registro y velocidad
        display.scroll("#" + str(i+1), delay=80)
        display.scroll("V:" + str(reg[1]), delay=80)  # Índice 1 es velocidad
        
        # Pausa para permitir leer los datos
        sleep(300)

# Configuración inicial
display.scroll("Caja Negra", delay=80)
display.show(Image.SQUARE)

# Bucle principal
while True:
    # Control con botones
    if button_a.was_pressed():
        # Botón A inicia/detiene la grabación
        if not grabando:
            iniciar_grabacion()
        else:
            detener_grabacion()
    
    if button_b.was_pressed():
        # Botón B muestra los datos registrados
        detener_grabacion()
        mostrar_registros()
    
    # Registro de datos si está grabando
    if grabando:
        tiempo_actual = running_time()
        if tiempo_actual - ultima_grabacion >= intervalo_ms:
            # Es hora de grabar un nuevo registro
            ultima_grabacion = tiempo_actual
            
            # Leer datos de sensores y guardar
            nuevo_registro = leer_sensores()
            registros.append(nuevo_registro)
            
            # Mostrar parpadeo para indicar grabación
            display.set_pixel(0, 0, 9)
            sleep(100)
            display.set_pixel(0, 0, 0)
            
            # Limitar cantidad de registros para no saturar la memoria
            if len(registros) > MAX_REGISTROS:
                registros.pop(0)  # Eliminar el registro más antiguo
    
    sleep(100)  # Pequeña pausa para no sobrecargar el procesador