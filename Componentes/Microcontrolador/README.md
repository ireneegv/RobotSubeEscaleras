# ¿Por qué un ESP32 y no un Arduino UNO?

> **Nota:** los valores son aproximados y corresponden a las placas de desarrollo más habituales (ESP32 DevKit con ESP32-WROOM-32 y Arduino UNO R3). Los precios son orientativos. Hay que comprobar la hoja de características de la placa concreta que se compre.

## 1. Resumen

El robot necesita controlar varios servos Parallax Feedback 360° y leer la señal de realimentación de cada uno para medir lo que avanza. Eso exige varios pines con interrupciones, buena velocidad de cálculo y, preferiblemente, comunicación inalámbrica. El ESP32 cumple todo eso con una sola placa pequeña y barata. El Arduino UNO se queda corto en varios puntos.

## 2. Comparativa

| Característica | ESP32 (DevKit) | Arduino UNO R3 |
|---|---:|---:|
| Microcontrolador | Xtensa LX6, 32 bits | ATmega328P, 8 bits |
| Núcleos | 2 | 1 |
| Frecuencia | Hasta 240 MHz | 16 MHz |
| Memoria RAM | ≈ 520 KB | 2 KB |
| Memoria flash (programa) | ≈ 4 MB (habitual en la placa) | 32 KB |
| Pines de entrada/salida | ≈ 25 utilizables | 14 digitales + 6 analógicas |
| Interrupciones externas | En cualquier pin GPIO | Solo en 2 pines (2 y 3), el resto con interrupciones por cambio de pin |
| PWM | 16 canales, en cualquier pin | 6 pines (con limitaciones si se usa la librería de servos) |
| Conversor analógico | 12 bits | 10 bits |
| Comunicaciones | 3 UART, 2 I²C, 3 SPI | 1 UART, 1 I²C, 1 SPI |
| Wi-Fi | Sí (802.11 b/g/n) | No |
| Bluetooth | Sí (clásico y BLE) | No |
| Tensión lógica | 3,3 V | 5 V |
| Consumo aproximado | ≈ 80 - 240 mA según el uso de Wi-Fi | ≈ 45 - 50 mA |
| Tamaño aproximado | ≈ 51 × 28 mm | 68,6 × 53,4 mm |
| Peso aproximado | ≈ 10 g | ≈ 25 g |
| Precio aproximado | 5 - 10 € | 8 - 10 € (clon), ≈ 25 € (original) |
| Programación | Arduino IDE, PlatformIO, ESP-IDF, MicroPython | Arduino IDE |

## 3. Motivos de la elección

### 3.1 Realimentación de varios servos a la vez

Cada servo Parallax Feedback 360° devuelve una señal PWM de 3,3 V a unos 910 Hz, cuyo ciclo de trabajo indica la posición. Con tres servos hay que medir tres señales a la vez sin perder flancos.

- En el ESP32 se puede usar una interrupción en cualquier pin y hay dos núcleos para repartir el trabajo.
- En el UNO solo hay dos pines de interrupción externa. Hay que recurrir a interrupciones por cambio de pin, que son más incómodas, o a lecturas bloqueantes como `pulseIn`, que dejan el procesador parado mientras esperan.

### 3.2 Potencia de cálculo y memoria

Contar vueltas, calcular la distancia y el control de velocidad de los tres servos a la vez es poca carga para un ESP32, pero ajustado para un UNO con 2 KB de RAM, sobre todo si se añade comunicación o más sensores.

### 3.3 Compatibilidad con la señal de 3,3 V

La señal de realimentación de los servos es de 3,3 V, igual que la lógica del ESP32, así que se conecta directamente. Con un UNO (5 V) esa señal queda cerca del umbral de lectura y es más delicada.

### 3.4 Wi-Fi y Bluetooth integrados

Permite monitorizar el robot, enviarle órdenes o recibir datos sin añadir módulos externos (por ejemplo, con MQTT o una interfaz web). En el UNO habría que añadir un módulo aparte, con más peso, más cableado y más consumo.

### 3.5 Tamaño y peso

El objetivo del proyecto es reducir el tamaño y el peso del robot. La placa ESP32 es más pequeña y ligera que el UNO y además incluye más funciones.

### 3.6 Precio

Una placa ESP32 cuesta lo mismo o menos que un UNO, y da mucho más por ese precio.

### 3.7 Mismo entorno de programación

El ESP32 se puede programar con el Arduino IDE y con la misma sintaxis, así que no hay que aprender un entorno nuevo.

## 4. Inconvenientes del ESP32 a tener en cuenta

- **Lógica de 3,3 V:** los pines no toleran 5 V. Hay que usar adaptadores de nivel con sensores o módulos de 5 V.
- **Más consumo:** sobre todo con el Wi-Fi activo. Hay que dimensionar bien la batería.
- **Restricciones de pines:** algunos pines solo son de entrada y otros condicionan el arranque. Además, los conversores analógicos del segundo grupo (ADC2) no se pueden usar con el Wi-Fi activo.
- **Conversor analógico poco lineal:** hay que calibrarlo si se necesita precisión.
- **Alimentación de los servos:** los servos no se pueden alimentar desde la placa. Necesitan una fuente propia con masa común, igual que con el UNO.

## 5. ¿Cuándo sería mejor un Arduino UNO?

- Proyectos sencillos con pocos sensores y sin comunicación inalámbrica.
- Cuando se necesite lógica de 5 V sin adaptadores.
- Para aprender, por la cantidad de tutoriales y shields compatibles.

## 6. Conclusión

Para este robot, el ESP32 es mejor opción: permite medir la realimentación de varios servos con interrupciones en cualquier pin, tiene potencia y memoria de sobra, es compatible con la señal de 3,3 V de los servos, incluye Wi-Fi y Bluetooth, y es más pequeño y barato que un Arduino UNO.
