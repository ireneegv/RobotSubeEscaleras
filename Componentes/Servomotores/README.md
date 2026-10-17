# Motores del robot: Parallax Feedback 360°

Por ahora el robot sigue usando los servos **Parallax Feedback 360° High-Speed (ref. 900-00360)**. Este documento recoge sus especificaciones. Si más adelante hace falta cambiarlos, se añadirán aquí las alternativas.

## 1. Especificaciones

| Característica | Valor |
|---|---:|
| Tipo | Servo de rotación continua con realimentación de posición |
| Referencia del fabricante | 900-00360 |
| Dimensiones del cuerpo | 40,7 × 19,8 × 38,8 mm |
| Dimensiones con orejetas de fijación | ≈ 50,3 × 37,1 × 20,1 mm |
| Peso | ≈ 40 g |
| Par máximo a 6 V | ≈ 2,2 kg·cm (≈ 0,22 N·m, 30,6 oz·in) |
| Velocidad máxima a 6 V, sin carga | 140 rpm (± 10) |
| Velocidad con control por realimentación | ± 120 rpm |
| Tensión de alimentación | 5,8 - 8 V recomendada para el control de velocidad (según un distribuidor) |
| Engranajes | Plástico |
| Giro continuo | Sí, en ambos sentidos |
| Precio aproximado | ≈ 28 USD / 28 £ |
| Consumo | Pendiente de comprobar en el datasheet oficial |

## 2. Señal de control

| Característica | Valor |
|---|---:|
| Tipo de señal | PWM de 50 Hz (como un servo de rotación continua) |
| Rango de pulso de control | 1280 - 1720 µs |
| Zona muerta (velocidad cero) | 1480 - 1520 µs (± 10) |
| Respuesta de velocidad | Lineal en todo el rango de control |
| Centrado manual | No hace falta |

El ancho del pulso determina la velocidad y el sentido de giro.

## 3. Señal de realimentación

| Característica | Valor |
|---|---:|
| Sensor | Efecto Hall (sin desgaste ni zona muerta, a diferencia de un potenciómetro) |
| Tipo de señal | PWM digital de 3,3 V |
| Frecuencia | ≈ 910 Hz (periodo ≈ 1,1 ms) |
| Ciclo de trabajo | 2,7 - 97,1 % |
| Conexión | Cable independiente con conector hembra, a un pin de entrada del microcontrolador |

El ciclo de trabajo de la señal corresponde a la posición del eje dentro de una vuelta. Es compatible con la lógica de 3,3 V del ESP32.

## 4. Cómo medir lo que avanza el robot

No hace falta conocer el ángulo del eje, solo la distancia recorrida. Con este servo:

1. El ESP32 mide el ciclo de trabajo de la señal de realimentación (por ejemplo con una interrupción o con el periférico de captura de pulsos).
2. Lo convierte en posición dentro de la vuelta: entre 0 y 360°, según el ciclo de trabajo entre su mínimo y su máximo.
3. Detecta cuándo la posición salta de casi 360° a casi 0° (o al revés) para sumar o restar una vuelta.
4. Calcula la distancia:

`distancia = (vueltas + posición / 360°) × perímetro de la rueda`

Cosas a tener en cuenta:

- Hay que leer lo bastante rápido para que el eje nunca avance más de media vuelta entre dos lecturas. A 120 rpm (2 vueltas por segundo) es muy fácil de cumplir.
- Si la rueda patina, el sensor cuenta giro y no avance real.
- Los extremos del ciclo de trabajo (2,7 % y 97,1 %) hay que calibrarlos para que el salto entre vueltas no cuente de más ni de menos.
- Parallax tiene una librería (servo360) para su placa Propeller y ejemplos de código C en el datasheet, que sirven como referencia para portarlo al ESP32.

## 5. Notas prácticas con el ESP32

- La señal de control es PWM de 50 Hz y se puede generar con el ESP32.
- El servo no debe alimentarse desde el pin del ESP32. Necesita una alimentación propia (batería o regulador) con masa común.
- La realimentación es de 3,3 V, así que no hace falta adaptador de nivel.

## Fuentes

- [Parallax Feedback 360° High-Speed Servo (RobotShop)](https://robotshop.com/en/parallax-feedback-360-high-speed-servo.html)
- [Parallax 900-00360 (Jameco)](https://www.jameco.com/z/900-00360-Parallax-Feedback-360-deg-High-Speed-Continuous-Rotation-Servo_2239541.html)
- [Parallax 900-00360 (Servo Database)](https://servodatabase.com/servo/parallax/900-00360)
- [Datasheet Parallax Feedback 360° High-Speed Servo (Pololu)](https://pololu.com/file/0J1395/900-00360-Feedback-360-HS-Servo-v1.2.pdf)
