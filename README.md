----
# RobotSubeEscaleras
----
En esta práctica hemos creado un robot que cumple con los siguientes requisitos:
- Esquiva obstáculos
- Es capaz de subir 1 peldaño
- Dimensiones: 25x25x25
- Inicio de movimiento mediante una interfaz inalámbrica


----
### Diseño del robot:

<img width="1024" height="833" alt="IMG-20261015-WA0017" src="https://github.com/user-attachments/assets/4b2af541-224e-4a6e-8117-024661b6656b" />

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

## PayLoad

| Componente | Cantidad | Peso unitario estimado | Peso total |
|---|---:|---:|---:|
| Servo Parallax Feedback 360 | 3 | 32 g | 96 g |
| ESP32 DevKit | 1 | 10 g | 10 g |
| Sensor ultrasónico HC-SR04 | 1 | 8 g | 8 g |
| Batería LiPo 2S, 2000 mAh | 1 | 110 g | 110 g |
| **Total de componentes** | | | **224 g** |

## Video Modelo 2

https://github.com/user-attachments/assets/8579e925-4092-4993-b2e3-47c2c2166304

