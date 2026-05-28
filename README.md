# checador_con_estres_laboral

La arquitectura de comunicación sigue estrictamente el formato jerárquico de 4 niveles:  
`proyecto / tipo_nodo / nombre_modulo / id_dispositivo`

| Componente Físico | Naturaleza / Propósito | Nivel 1 (Proyecto) | Nivel 2 (Tipo) | Nivel 3 (Módulo) | Nivel 4 (ID) | Tópico Completo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Sensor de Pulso / GSR** | Telemetría (Datos de salida) | `checador_estres` | `sensor` | `biometrico` | `01` | `checador_estres/sensor/biometrico/01` |
| **Lector RFID / Huella** | Telemetría (Datos de salida) | `checador_estres` | `sensor` | `lector_id` | `01` | `checador_estres/sensor/lector_id/01` |
| **Pantalla LCD / OLED** | Comando (Instrucción entrante) | `checador_estres` | `cmd` | `pantalla` | `01` | `checador_estres/cmd/pantalla/01` |
| **Buzzer (Alertas)** | Comando (Instrucción entrante) | `checador_estres` | `cmd` | `buzzer` | `01` | `checador_estres/cmd/buzzer/01` |
| **LED de Estado** | Estado Operativo Actual | `checador_estres` | `actuador` | `led_indicador` | `01` | `checador_estres/actuador/led_indicador/01` |

## Evidencias de Funcionamiento

### 1. Transmisión desde el Hardware (ESP32)
El microcontrolador ESP32 establece la conexión exitosa a la red inalámbrica local, se enlaza al broker MQTT centralizado (broker.hivemq.com) e inicia la publicación cíclica automatizada de las lecturas biométricas procesadas a través de la HAL sin bloqueos del sistema.

* **Estado en Consola:** Conexión validada con IP local asignada y envío activo de cargas útiles en formato string cada 5 segundos.
https://docs.google.com/document/d/1YlXQDLVg-5mv169c-keydqpB9pB6QCRwPEIW2BdowfU/edit?usp=sharing

### 2. Processing y Timestamps en Servidor (Python)
El backend centralizado desarrollado en Python detecta las ráfagas entrantes de telemetría en el broker y les inyecta de forma síncrona una marca de tiempo con resolución de milisegundos para garantizar el ordenamiento cronológico riguroso del historial de estrés.

https://docs.google.com/document/d/1YlXQDLVg-5mv169c-keydqpB9pB6QCRwPEIW2BdowfU/edit?usp=sharing

## Validación de la HAL y Estructura del Proyecto

El repositorio sigue un modelo arquitectónico desacoplado, separando la lógica de comunicación de red de la interacción física con los periféricos mediante una Capa de Abstracción de Hardware:

* `/server_python/app_mqtt.py`: Script central del servidor en Python.
* `/firmware_esp32/mainn.py`: Código de gestión de red, Wi-Fi y cliente MQTT para la ESP32.
* `/firmware_esp32/hal.py`: Funciones aisladas de lectura de sensores y escritura de actuadores.

## Sección de Conclusion Individual 

### Integrante 1: Angel Josue Lozano Cardona 
* **Problema Encontrado:** Al intentar acoplar la librería paho-mqtt en el entorno global del servidor e interactuar mediante el gestor visual de paquetes de Thonny con la ESP32, el sistema arrojó errores de colisión de entornos (ModuleNotFoundError) y bloqueos persistentes en el puerto serie (Device is busy or does not respond) causados por subprocesos activos en segundo plano.
* **Solución Aplicada:** Se forzó la instalación de dependencias en el servidor mediante el uso de ensurepip directo en consola nativa. En la ESP32, se rompió el ciclo mediante interrupción por hardware combinando Ctrl + C y el botón físico RST, implementando posteriormente un script de instalación remota mediante el módulo mip para descargar la librería umqtt.simple de forma automatizada evadiendo las interfaces colgadas de Windows.
* **Conclusión Personal:** El aislamiento de las capas físicas mediante la HAL y la implementación del broker MQTT demuestran que es posible diseñar un sistema robusto capaz de centralizar datos heterogéneos, donde el backend asume la responsabilidad de la sincronización temporal mediante Timestamps de alta precisión sin sobrecargar el procesamiento del nodo emisor.

### Integrante 2: Cesar Armando Castro Luna
* **Problema Encontrado:** Desfase en la consistencia de los tópicos de comunicación al estructurar los payloads de prueba y sincronizar los canales de escucha del servidor de forma asíncrona con el broker público de HiveMQ.
* **Solución Aplicada:** Se estandarizó la matriz de comunicación bajo el esquema jerárquico rígido de 4 niveles, permitiendo que el callback on_message del servidor Python discrimine con precisión el origen de la telemetría mediante comodines estructurados (#).
* **Conclusión Personal:** El uso de un estándar estricto en la nomenclatura de tópicos es indispensable para la escalabilidad del proyecto. Permite agregar múltiples nodos biométricos en el futuro sin necesidad de reescribir la lógica de procesamiento central en el servidor.

### Integrante 3: Luwing Espinoza Bravo
* **Problema Encontrado:** Pérdida aleatoria de paquetes y colgado del socket de red al intentar mantener la transmisión síncrona del bucle principal de la ESP32 sin un control de demoras controlado.
* **Solución Aplicada:** Se integró un retardo no bloqueante en el ciclo infinito mediante time.sleep(5) y se validó que la inicialización del cliente MQTT mantuviera los parámetros de enlace estables frente al broker central.
* **Conclusión Personal:** La modularidad del firmware en MicroPython facilita enormemente el diagnóstico de fallas de red, permitiendo probar la conectividad y la publicación en el broker de internet de forma aislada a las señales eléctricas analógicas de los sensores biométricos.
