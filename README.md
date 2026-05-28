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
