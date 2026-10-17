# Elección de los motores

> **Nota:** los valores de esta tabla son aproximados (datos de fabricante y tiendas habituales, precios orientativos en euros). Antes de comprar hay que comprobar la hoja de características de la versión concreta.

## 1. Punto de partida

Al principio, el robot utilizaba tres servos **Parallax Feedback 360°**. Queremos reducir el tamaño y el peso del robot, así que hemos buscado alternativas más pequeñas que sigan permitiendo medir cuánto avanza el robot.

| Característica | Parallax Feedback 360° |
|---|---:|
| Tipo | Servo de rotación continua con realimentación |
| Dimensiones | 40,7 × 19,8 × 38,8 mm |
| Peso aproximado | 41 g |
| Par máximo a 6 V | ≈ 2,2 kg·cm |
| Alimentación | 4 - 6 V |
| Consumo (sin carga / aprox.) | ≈ 140 mA |
| Precio aproximado | 25 - 35 € |
| Permite medir lo que avanza | Sí |
| Giro continuo | Sí |

## 2. Requisito nuevo: levantar las piernas

Cada pierna es una pieza articulada con una bisagra y el motor debe actuar directamente sobre ella.

| Dato | Valor |
|---|---:|
| Masa de la parte a levantar | 700 g |
| Longitud | 20 cm |
| Reparto del peso | Casi todo en el extremo libre |
| Par estático (pierna horizontal) | 0,7 kg × 9,81 × 0,2 m ≈ **1,4 N·m** (≈ 14 kg·cm) |
| Par dinámico (aceleración suave, ≈ 10 rad/s²) | ≈ 0,3 N·m |
| Par de arranque total | ≈ **1,7 N·m** (≈ 17 kg·cm) |
| **Par objetivo con margen** | **2,5 - 3 N·m (25 - 30 kg·cm)** |

Importante: hay que mirar el par **nominal o continuo**. El par de bloqueo (stall) que anuncian los catálogos solo se puede dar durante instantes sin calentar el motor.

Un **muelle de torsión** en la bisagra que compense parte del peso puede reducir el par necesario casi a la mitad.

## 3. Servos pequeños (no giran de forma continua)

Son muy ligeros, pero **no llegan al par necesario para las piernas** y no giran de forma continua, así que **no sirven para medir el avance del robot**. Solo valen para articulaciones ligeras.

| Característica | FEETECH FS0403-FB | FEETECH FS90-FB |
|---|---:|---:|
| Dimensiones | 20 × 8,3 × 19,3 mm | 23,2 × 12,5 × 22 mm |
| Peso aproximado | 6 g | 13 g |
| Par máximo a 6 V | 0,7 kg·cm | 1,5 kg·cm |
| Alimentación | 4,8 - 6 V | 4,8 - 6 V |
| Consumo aproximado | Bajo (cientos de mA con carga) | Bajo (cientos de mA con carga) |
| Precio aproximado | 8 - 12 € | 6 - 10 € |
| Salida de realimentación | Sí (analógica) | Sí (analógica) |
| Giro continuo | No | No |

## 4. Servos inteligentes con encoder (candidatos para las piernas y las ruedas)

| Característica | FEETECH STS3215 (12 V) | FEETECH STS3250 (12 V) | Dynamixel XL430-W250 | Dynamixel XL330-M288 |
|---|---:|---:|---:|---:|
| Dimensiones | 45,2 × 24,7 × 35 mm | ≈ 45 × 25 × 35 mm | 28,5 × 46,5 × 34 mm | 20 × 34 × 26 mm |
| Peso aproximado | ≈ 55 g | ≈ 65 g | 57 g | 18 g |
| Par de bloqueo | ≈ 30 kg·cm (≈ 3 N·m) a 12 V | ≈ 50 kg·cm (≈ 5 N·m) a 12 V | ≈ 1,5 N·m (≈ 15 kg·cm) a 12 V | ≈ 0,5 N·m (≈ 5 kg·cm) a 5 V |
| Alimentación | 6 - 12 V (7,4 V → ≈ 19,5 kg·cm) | 6 - 12 V | 6,5 - 12 V | 3,7 - 6 V |
| Corriente de bloqueo | ≈ 2,7 A | ≈ 3 A o más | ≈ 1,3 A | ≈ 1 A |
| Consumo en reposo | ≈ 100 - 200 mA | ≈ 100 - 200 mA | ≈ 50 - 100 mA | ≈ 50 mA |
| Encoder | Magnético 12 bits (4096 cuentas/vuelta) | Magnético 12 bits | Magnético 12 bits | Magnético 12 bits |
| Giro continuo | Sí (modo rueda) | Sí (modo rueda) | Sí (modo rueda) | Sí (modo rueda) |
| Comunicación | Bus serie TTL | Bus serie TTL | Bus TTL (half-duplex) | Bus TTL (half-duplex) |
| Precio aproximado | 15 - 25 € | 30 - 40 € | 50 - 60 € | 25 - 35 € |
| ¿Llega a 2,5 - 3 N·m? | **Justo** | **Sí, con margen** | No | No |

## 5. Motorreductores DC con encoder (opción más barata, más trabajo de control)

| Característica | N20 con encoder | JGB37-520 con encoder Hall | Pololu 37D con encoder |
|---|---:|---:|---:|
| Dimensiones | 12 × 10 × 25 - 30 mm | Ø 37 mm × 60 - 80 mm | Ø 37 mm × 60 - 70 mm |
| Peso aproximado | 10 - 12 g | ≈ 100 - 150 g | ≈ 125 - 200 g |
| Tensión | 3 - 12 V (versión de 6 V habitual) | 12 V | 6 - 12 V |
| Par aproximado | 1 - 3 kg·cm según reducción | Hasta decenas de kg·cm según reducción | Hasta decenas de kg·cm según reducción |
| Consumo | 100 mA sin carga, ≈ 1 A bloqueado | ≈ 200 mA sin carga, ≈ 3 - 5 A bloqueado | ≈ 200 mA sin carga, ≈ 5 A bloqueado |
| Precio aproximado | 8 - 12 € | 12 - 25 € | 35 - 45 € |
| Encoder | Sí (magnético, pocos pulsos por vuelta) | Sí (Hall) | Sí (Hall, 64 CPR) |
| Giro continuo | Sí | Sí | Sí |
| Necesita driver aparte | Sí (puente en H) | Sí | Sí |
| Idoneidad | Ruedas ligeras | Ruedas y piernas | Ruedas y piernas |

## 6. ¿Cómo sabemos cuánto avanza el robot?

No necesitamos conocer el ángulo del eje, solo **la distancia que ha recorrido el robot**. Para ello hay tres posibilidades:

- Utilizar un **servo con encoder en modo rueda** (STS3215, STS3250, Dynamixel).
- Utilizar un **motorreductor con encoder integrado** (N20, JGB37, Pololu 37D). El ESP32 cuenta los pulsos del encoder con interrupciones o con su contador de pulsos por hardware.
- Añadir un **sensor externo** que mida el giro del eje, por ejemplo un encoder magnético **AS5600** (12 bits, I²C, 3,3 V, ≈ 2 - 4 €).

### Con el FEETECH STS3215 en modo rueda

El STS3215 no da una cuenta de vueltas acumulada. Da la posición dentro de cada vuelta y las vueltas las cuenta el ESP32.

- El servo sigue leyendo su encoder magnético de 12 bits en modo rueda. Por el bus serie se puede pedir:
  - La **posición del eje**, de 0 a 4095 por vuelta, que vuelve a 0 al completar cada revolución.
  - La **velocidad actual**, con signo según el sentido de giro.
- El ESP32 lee la posición cada pocos milisegundos y detecta cuándo salta de 4095 a 0 (o al revés) para sumar o restar una vuelta.
- La distancia recorrida se calcula así:

`distancia = (vueltas + posición / 4096) × perímetro de la rueda`

Cosas a tener en cuenta:

- Hay que leer lo bastante rápido para que el eje nunca avance más de media vuelta entre dos lecturas. Con ruedas pequeñas y lecturas cada 10 - 20 ms no hay problema.
- Si la rueda patina, el encoder cuenta giro y no avance real, así que la medida pierde precisión en suelos resbaladizos.
- El encoder está en el eje de salida, después del reductor, así que cada vuelta de rueda son exactamente 4096 cuentas.
- Algunas versiones de la serie STS tienen un modo de posición multivuelta, pero no está confirmado que el STS3215 lo ofrezca. Hay que comprobarlo en la hoja de características o en la librería de Feetech antes de depender de ello.
- Los servos FS0403-FB y FS90-FB no sirven para esto, porque no giran de forma continua.

## 7. Criterios de elección

| Característica | Objetivo |
|---|---|
| Tamaño | Que ocupen poco espacio |
| Peso | Reducir el peso del robot |
| Fuerza | 2,5 - 3 N·m en las piernas, par menor en las ruedas |
| Avance | Poder medir cuánto avanza el robot |
| Alimentación | Compatible con la batería (7,4 V o 12 V) y con el ESP32 (lógica de 3,3 V) |
| Consumo | Que la batería aguante, sobre todo con las piernas levantadas |
| Precio | Coste razonable |

Aspectos prácticos con el ESP32:

- Los servos de 12 V no se pueden alimentar desde el ESP32. Necesitan batería propia (por ejemplo una LiPo 3S) con masa común.
- Los servos de bus serie (Feetech, Dynamixel) necesitan una pequeña placa o circuito adaptador para el bus half-duplex.
- Los motorreductores DC necesitan un driver de motor y un control PID en el ESP32.

## 8. Resumen comparativo

| Opción | Par | Peso | Precio | Complejidad | Veredicto |
|---|---|---|---|---|---|
| FS0403-FB / FS90-FB | Muy bajo | 6 - 13 g | 6 - 12 € | Baja | No giran de forma continua, no sirven |
| STS3215 | ≈ 3 N·m (bloqueo) | ≈ 55 g | 15 - 25 € | Media | **Mejor relación calidad/precio** |
| STS3250 | ≈ 5 N·m (bloqueo) | ≈ 65 g | 30 - 40 € | Media | Si el STS3215 se queda corto |
| Dynamixel XL430 | ≈ 1,5 N·m | 57 g | 50 - 60 € | Media | Fiable pero corto de par |
| Dynamixel XL330 | ≈ 0,5 N·m | 18 g | 25 - 35 € | Media | Demasiado débil para las piernas |
| JGB37 / Pololu 37D | Alto | 100 - 200 g | 12 - 45 € | Alta | Barato pero pesado y más grande |
| N20 con encoder | Bajo | 10 g | 8 - 12 € | Alta | Solo para ruedas ligeras |

## 9. Conclusión

Los servos FEETECH FS0403-FB y FS90-FB son más pequeños y ligeros que los Parallax Feedback 360°, pero no tienen par suficiente para las piernas ni giran de forma continua, así que no permiten medir cuánto avanza el robot.

Para **levantar las piernas** (≈ 1,7 N·m de arranque, objetivo 2,5 - 3 N·m) la opción recomendada es el **FEETECH STS3215 de 12 V**, con un muelle de torsión que reduzca la carga. Si el par continuo no basta, el siguiente escalón es el **STS3250**.

Para **mover las ruedas y medir cuánto avanza el robot**, el STS3215 en modo rueda sirve: el ESP32 lee la posición del encoder, cuenta las vueltas y calcula la distancia. Si se prefiere algo más barato o ligero, se puede usar un motorreductor con encoder (N20 si es ligero, JGB37 o Pololu 37D si necesita más par).

La elección definitiva dependerá del espacio disponible, el tiempo que deba aguantar la pierna levantada y la batería disponible.
