# Simulación de Caja Negra para Auto Escolar en Micro:bit

## Descripción
Este proyecto simula un sistema de "caja negra" para un autobús escolar utilizando una placa Micro:bit. Similar a las cajas negras en aviones, este sistema registra datos de operación del vehículo que pueden ser revisados posteriormente para análisis o en caso de incidentes.

## Características
- **Registro de datos simulados**:
  - Velocidad (0-80 km/h)
  - Aceleración (-2 a 2 m/s²)
  - Ubicación (coordenadas X,Y simplificadas)
  - Tiempo de registro

- **Controles intuitivos**:
  - Botón A: Inicia/detiene grabación
  - Botón B: Muestra los datos registrados
  - Botones A+B (simultáneos): Sale del modo visualización

- **Visualización de estados**:
  - Pantalla LED muestra "REC" cuando inicia grabación
  - Muestra "STOP" cuando se detiene
  - Un LED parpadea cada vez que se graba un nuevo registro

- **Gestión automática de memoria**:
  - Almacena hasta 20 registros
  - Elimina automáticamente registros antiguos para evitar saturar la memoria

## Requisitos
- Placa Micro:bit
- Editor Python Micro:bit v3 (https://python.microbit.org/v/3)

## Instalación
1. Visita https://python.microbit.org/v/3
2. Copia el código proporcionado en el editor
3. Conecta tu Micro:bit mediante USB
4. Haz clic en "Descargar" para transferir el programa a tu dispositivo

## Uso
1. **Iniciar grabación**:
   - Presiona el botón A
   - Verás el mensaje "REC" y la pantalla mostrará un corazón
   - Un LED en la esquina superior izquierda parpadeará cada vez que se registre un dato (cada 2 segundos)

2. **Detener grabación**:
   - Presiona el botón A nuevamente
   - Verás el mensaje "STOP" y la pantalla mostrará un cuadrado

3. **Ver datos registrados**:
   - Presiona el botón B
   - La pantalla mostrará primero la cantidad de registros almacenados
   - Luego mostrará cada registro con su número y velocidad
   - Para salir de la visualización antes de tiempo, presiona los botones A y B simultáneamente

## Personalización
Para adaptar este sistema a un uso real, considera estas modificaciones:
- Conectar sensores reales (acelerómetro, GPS, etc.)
- Añadir un módulo de almacenamiento externo (tarjeta microSD)
- Implementar comunicación inalámbrica para transmitir datos en tiempo real

## Limitaciones
- En esta versión de simulación, los datos son generados aleatoriamente
- La memoria del Micro:bit limita la cantidad de registros almacenables
- La visualización en pantalla LED es limitada debido al tamaño

## Solución de problemas
- **El programa no responde**: Reinicia el Micro:bit presionando el botón de reset
- **No se muestran datos**: Verifica que hayas iniciado la grabación (botón A) antes de intentar visualizar
- **Errores de memoria**: Reduce el valor de MAX_REGISTROS si experimentas problemas

## Aplicaciones educativas
Este proyecto puede utilizarse para enseñar conceptos de:
- Programación en Python
- Sistemas embebidos
- Recolección y análisis de datos
- Seguridad en transporte escolar

---

Desarrollado para educación y demostración. Este sistema simula el concepto de una caja negra pero no reemplaza sistemas comerciales de monitoreo vehicular.



https://gist.github.com/user-attachments/assets/cfe737df-6dd2-4356-ba91-7eccce8a7d71



