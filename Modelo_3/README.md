----
# RobotSubeEscaleras - Modelo 3
----
En esta práctica hemos creado un robot que cumple con los siguientes requisitos:
- Esquiva obstáculos
- Es capaz de subir 1 peldaño
- Dimensiones: 25x25x25
- Inicio de movimiento mediante una interfaz inalámbrica


----
### Diseño del robot:

<img width="4967" height="3509" alt="print-2_page-0001" src="https://github.com/user-attachments/assets/8529d561-820d-4efb-9626-bb7f93b2dfaf" />

----
### Materiales

| Componente | Cantidad | Corriente de funcionamiento | Corriente de arranque |
|---|:---:|:---:|:---:|
| [Servo Parallax Feedback 360](https://eu.robotshop.com/es/products/servo-de-alta-velocidad-con-retroalimentacion-de-360%C2%BA-parallax) | 3 | $I_m = 0{,}15\ \text{A}$ | $I_a = 1{,}2\ \text{A}$ |
| [ESP32 DevKit](https://www.electrohobby.es/esp32/448-esp32-devkit.html) | 1 | $I_b = 0{,}5\ \text{A}$ | - |
| [Sensor ultrasónico HC-SR04](https://electronicaymas.com/movimiento/modulo-ultrasonido-para-arduino-700) | 1 | $I_d = 0{,}015\ \text{A}$ | - |
| Batería LiPo 2S | 1 | - | - |

**Batería:** el cálculo de la tensión, la capacidad y la tasa de descarga, junto con la selección final, está en la carpeta [`Bateria`](./Bateria/).

Para elegir la batería hemos usado este cálculo para sacar la tasa de descarga, teniendo en cuenta los componentes que hemos nombrado anteriormente.

```
Idis = Ia*3 + Ib + Id
It = Im*3 + Ib + Id 

C = Idis/It = 3,815/0,665 = 5,736842105
```


# PESOS APROXIMADOS: 

##  Base del robot

| Componente | Cantidad | Peso unitario estimado | Peso total |
|---|---:|---:|---:|
| Servo Parallax Feedback 360 | 3 | 32 g | 96 g |
| ESP32 DevKit | 1 | 10 g | 10 g |
| Batería LiPo 2S, 2000 mAh | 1 | 110 g | 110 g |
| Peso de la carcasa de PLA | 1 | 400 g | 400 g |
| **Total de componentes** | | | **616 g** |


## Soporte del robot (segunda base)

| Componente | Cantidad | Peso unitario estimado | Peso total |
|---|---:|---:|---:|
| Servo Parallax Feedback 360 | 2 | 32 g | 64 g |
| ESP32 DevKit | 1 | 10 g | 10 g |
| Sensor ultrasónico HC-SR04 | 1 | 8 g | 8 g |
| Batería LiPo 2S, 2000 mAh | 1 | 110 g | 110 g |
| Peso de la carcasa de PLA rellena (0.1 X 0.15 X 0.01) | 1 | 180 g | 180 g |
| **Total de componentes** | | | **372 g** |


# MEDIDAS:

| Componente | Cantidad | Dimensiones aproximadas |
|---|---:|---|
| Servo Parallax Feedback 360 | 3 | 40,7 × 19,8 × 38,8 mm |
| ESP32 DevKit | 1 | 55 × 28 mm |
| Sensor ultrasónico HC-SR04 | 1 | 45 × 20 × 15 mm |
| Batería LiPo 2S, 2000 mAh | 1 | Consultar ficha técnica del fabricante |
| brazos PLA (65 g) | 2 | (0.25 x 0.02 x 0.03) |

# VIDEO SIMULACIÓN: 
https://github.com/user-attachments/assets/e7b172c3-d4eb-400a-bb99-c79db4da110a
