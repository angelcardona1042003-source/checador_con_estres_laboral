"""
OBJETIVO: Capa de Abstracción de Hardware (HAL) para aislamiento de sensores biométricos y actuadores.
INTEGRANTES: 
  - Angel Josue Lozano Cardona (Código: 22240229)
  - Cesar Armando Castro Luna
  - Luwing Espinoza Bravo
PROYECTO: Checador con Estrés Laboral
"""

def leer_sensor_biometrico():
    import random
    return random.randint(40, 100)

def escribir_actuador_led(estado):
    print(f"[HAL LOG] LED indicador cambiado a estado: {estado}")
