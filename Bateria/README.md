## Selección de la batería

La elección de la batería es un aspecto fundamental en el diseño del robot, ya que determina su autonomía, condiciona su peso y debe garantizar el suministro de corriente necesario para alimentar todos los componentes.

Para seleccionar la batería se seguirá el procedimiento propuesto en la guía de diseño detallado, teniendo en cuenta los requerimientos eléctricos, el peso, la tasa de descarga, la vida útil y los aspectos de seguridad.

### 1. Determinación de la tensión y la corriente requerida

El robot tiene una masa aproximada de 1 kg y está compuesto por los siguientes elementos:

| Componente | Cantidad | Corriente de funcionamiento | Corriente de arranque |
|---|---:|---:|---:|
| Servo Parallax Feedback 360 | 3 | 0,15 A por unidad | 1,2 A por unidad |
| ESP32 DevKit | 1 | 0,5 A | No especificada |
| Sensor ultrasónico HC-SR04 | 1 | 0,015 A | No especificada |

Los valores de corriente se toman como datos de diseño iniciales y deberán contrastarse con las condiciones reales de funcionamiento de los componentes.

#### 1.1. Corriente total en funcionamiento

La corriente total del sistema se calcula sumando el consumo de todos los componentes:

$$
I_T = 3I_m + I_b + I_d
$$

Donde:
- $I_m$ es la corriente de funcionamiento de cada motor.
- $I_b$ es la corriente consumida por la placa de control.
- $I_d$ es la corriente consumida por los dispositivos auxiliares.

Sustituyendo los valores:

$$
I_T = 3(0{,}15) + 0{,}5 + 0{,}015
$$

$$
I_T = 0{,}45 + 0{,}5 + 0{,}015
$$

$$
\boxed{I_T = 0{,}965\ \text{A}}
$$

Por tanto, el consumo nominal estimado del robot es de 0,965 A cuando los tres servos están funcionando simultáneamente.

#### 1.2. Corriente máxima durante el arranque

Para dimensionar la batería también es necesario considerar los picos de corriente que se producen cuando los motores arrancan simultáneamente.

La corriente máxima estimada se calcula mediante:

$$
I_{dis} = 3I_a + I_b + I_d
$$

Donde $I_a$ representa la corriente de arranque de cada servo.

Sustituyendo:

$$
I_{dis} = 3(1{,}2) + 0{,}5 + 0{,}015
$$

$$
I_{dis} = 3{,}6 + 0{,}5 + 0{,}015
$$

$$
\boxed{I_{dis} = 4{,}115\ \text{A}}
$$

Este resultado representa una estimación del consumo máximo instantáneo del sistema. La corriente real dependerá de la carga mecánica y de las condiciones de arranque de los servos.

### 2. Influencia del peso de la batería

El robot tiene una masa inicial aproximada de 1 kg. La incorporación de la batería incrementará esta masa y puede aumentar la corriente necesaria para desplazarlo.

Como ejemplo, si se selecciona una batería de 2000 mAh con una masa aproximada de 110 g, la masa total será:

$$
m_{total} = m_{robot} + m_{bateria}
$$

$$
m_{total} = 1000 + 110
$$

$$
\boxed{m_{total} = 1110\ \text{g} = 1{,}11\ \text{kg}}
$$

El incremento porcentual de masa será:

$$
\text{incremento} = \frac{m_{bateria}}{m_{robot}} \cdot 100
$$

$$
\text{incremento} = \frac{110}{1000} \cdot 100
$$

$$
\boxed{\text{incremento} = 11\ \text{por ciento}}
$$

Por tanto, la batería incrementaría aproximadamente un 11 % la masa inicial del robot.

Este aumento puede modificar el esfuerzo requerido por los motores y, en consecuencia, el consumo energético. No obstante, para cuantificar dicho efecto sería necesario conocer las características mecánicas del robot, como el diámetro de las ruedas, la transmisión, la velocidad y las condiciones de desplazamiento.

### 3. Estimación de la capacidad y de la tasa de descarga

Para realizar los cálculos se establece inicialmente una autonomía objetivo de 30 minutos, equivalente a 0,5 horas.

#### 3.1. Capacidad mínima necesaria

La capacidad eléctrica necesaria se obtiene multiplicando la corriente consumida por el tiempo de funcionamiento:

$$
Q = I_T \cdot t
$$

Donde:
- $Q$ es la capacidad necesaria, expresada en Ah.
- $I_T$ es la corriente total, expresada en A.
- $t$ es el tiempo de funcionamiento, expresado en horas.

Para una autonomía de 30 minutos:

$$
t = \frac{30}{60} = 0{,}5\ \text{h}
$$

Sustituyendo los valores:

$$
Q = 0{,}965 \cdot 0{,}5
$$

$$
\boxed{Q = 0{,}4825\ \text{Ah}}
$$

Expresando el resultado en miliamperios-hora:

$$
Q = 0{,}4825 \cdot 1000
$$

$$
\boxed{Q = 482{,}5\ \text{mAh}}
$$

Por tanto, la capacidad teórica mínima para alcanzar 30 minutos de funcionamiento es de 482,5 mAh, suponiendo que el consumo se mantiene constante.

Este resultado no incluye las pérdidas de los reguladores, las variaciones de carga de los motores ni la capacidad que debe reservarse para evitar una descarga excesiva. Por ello, se seleccionará una batería de mayor capacidad.

#### 3.2. Cálculo de la tasa de descarga necesaria

La tasa de descarga, expresada en C, relaciona la corriente suministrada por la batería con su capacidad nominal.

Se calcula mediante:

$$
C = \frac{I}{Q}
$$

Donde:
- $C$ es la tasa de descarga.
- $I$ es la corriente suministrada por la batería, en A.
- $Q$ es la capacidad nominal de la batería, en Ah.

Si se utilizase una batería con la capacidad mínima teórica calculada:

$$
C_{necesaria} = \frac{I_{dis}}{Q}
$$

$$
C_{necesaria} = \frac{4{,}115}{0{,}4825}
$$

$$
\boxed{C_{necesaria} \approx 8{,}53\,C}
$$

Por tanto, una batería de 482,5 mAh necesitaría admitir una tasa de descarga de al menos 8,53C para suministrar la corriente máxima estimada.

#### 3.3. Comprobación de una batería de 2000 mAh y 20C

Como opción preliminar se considera una batería LiPo de 7,4 V, 2000 mAh y una tasa de descarga de 20C.

Su capacidad expresada en amperios-hora es:

$$
Q = \frac{2000}{1000} = 2\ \text{Ah}
$$

La corriente máxima teórica de descarga se calcula mediante:

$$
I_{max} = C \cdot Q
$$

Sustituyendo:

$$
I_{max} = 20 \cdot 2
$$

$$
\boxed{I_{max} = 40\ \text{A}}
$$

Para comprobar que cumple los requisitos eléctricos, se compara esta corriente con el consumo máximo estimado del robot:

$$
40\ \text{A} > 4{,}115\ \text{A}
$$

Por tanto, la batería cumple teóricamente el requisito de corriente de descarga.

La tasa de descarga mínima necesaria para esta batería sería:

$$
C_{necesaria} = \frac{I_{dis}}{Q}
$$

$$
C_{necesaria} = \frac{4{,}115}{2}
$$

$$
\boxed{C_{necesaria} \approx 2{,}06\,C}
$$

Dado que la batería seleccionada tiene una tasa de descarga nominal de 20C, dispone de un margen considerable respecto a la corriente máxima estimada.

La corriente máxima indicada por la tasa C es un valor teórico que debe contrastarse con las condiciones de uso y las especificaciones del fabricante.

#### 3.4. Estimación de la autonomía

La autonomía teórica de una batería puede calcularse dividiendo su capacidad entre la corriente consumida:

$$
t = \frac{Q}{I_T}
$$

Para una batería de 2000 mAh:

$$
t = \frac{2}{0{,}965}
$$

$$
\boxed{t \approx 2{,}07\ \text{h}}
$$

Convirtiendo el resultado a minutos:

$$
t = 2{,}07 \cdot 60
$$

$$
\boxed{t \approx 124\ \text{minutos}}
$$

Este resultado es una estimación ideal. No constituye una autonomía garantizada, ya que el cálculo debe considerar las distintas tensiones de alimentación, las pérdidas de conversión, la carga mecánica y la variación del consumo durante el funcionamiento.

### 4. Vida útil de la batería

La vida útil de una batería recargable suele expresarse mediante el número de ciclos de carga y descarga que puede completar antes de que su capacidad disminuya significativamente.

Para la selección definitiva se deberán consultar las especificaciones del fabricante, prestando especial atención a:

- Número de ciclos de carga y descarga.
- Capacidad residual después de los ciclos especificados.
- Temperatura de funcionamiento y almacenamiento.
- Condiciones de carga y descarga recomendadas.
- Procedimientos de almacenamiento cuando la batería no se utilice.

No se asignará un número concreto de ciclos sin disponer de información verificable del fabricante de la batería seleccionada.

### 5. Consideraciones ambientales y de seguridad

La batería deberá cumplir los requisitos eléctricos de los componentes y garantizar un funcionamiento seguro.

#### 5.1. Compatibilidad de tensiones

Los servos Parallax Feedback 360 admiten una alimentación de 5 a 8,4 V, con un intervalo recomendado de 5,8 a 8 V para su funcionamiento en rotación continua.

Una batería LiPo 2S presenta una tensión nominal de 7,4 V y una tensión máxima de 8,4 V cuando está completamente cargada.

Por tanto, su tensión se encuentra dentro del intervalo admitido por el fabricante de los servos. No obstante, se deberá comprobar que la alimentación permanece dentro de los límites especificados durante el funcionamiento.

El ESP32 DevKit requiere una alimentación adecuada a la placa, normalmente 5 V a través de USB o VIN, mientras que el módulo ESP32 funciona internamente a 3,3 V.

El sensor ultrasónico HC-SR04 requiere una alimentación de 5 V. Además, su señal ECHO deberá adaptarse a un nivel compatible con las entradas de 3,3 V del ESP32.

Por estos motivos, será necesario diseñar una distribución de alimentación adecuada para cada componente, incluyendo los reguladores de tensión que correspondan.

#### 5.2. Medidas de seguridad

Durante el diseño y la utilización de la batería se deberán considerar las siguientes medidas:

- Utilizar un cargador compatible con baterías LiPo 2S y con equilibrado de celdas.
- Evitar cortocircuitos y conexiones con polaridad invertida.
- Respetar los límites de tensión de los componentes.
- Evitar golpes, perforaciones y temperaturas excesivas.
- Dimensionar adecuadamente los cables, conectores y reguladores.
- Evitar que los motores permanezcan bloqueados durante periodos prolongados.
- Proteger la batería frente a una descarga excesiva.
- Respetar las condiciones de carga, almacenamiento y transporte indicadas por el fabricante.

### 6. Selección preliminar de la batería

A partir de los cálculos realizados, se propone evaluar una batería LiPo 2S de 7,4 V, 2000 mAh y 20C.

Las características consideradas son:

| Parámetro | Batería inicial | Nueva batería |
|---|---:|---:|
| Tecnología | LiPo | LiPo |
| Número de celdas | 2S | 2S |
| Tensión nominal | 7,4 V | 7,4 V |
| Tensión máxima cargada | 8,4 V | 8,4 V |
| Capacidad nominal | 2000 mAh | 1500 mAh |
| Tasa de descarga indicada | 20C | 25C |
| Corriente máxima teórica | 40 A | 37,5 A |
| Corriente normal estimada del robot | 0,965 A | 0,965 A |
| Corriente máxima estimada del robot | 4,115 A | 4,115 A |
| Autonomía objetivo inicial | 30 minutos | 30 minutos |
| Autonomía teórica estimada | 124 minutos | 93 minutos |
| Masa inicial del robot | Aproximadamente 1 kg | Aproximadamente 1 kg |
| Peso de la batería | 110 g (aprox.) | 75 g (aprox) |
| Dimensiones | Según modelo | 65 × 34 × 14 mm |

Una posible batería es la [batería Dualsky LiPo 2S de 7,4 V y 2000 mAh](https://www.flashrc.com/es/baterias-del-receptor/22780-bateria-2s-7-4v-2000mah-lipo-20c-rx-toma-dualsky-xt60-6941047114593.html) ya que cumple con todas las especificaciones necesarias.

La segunda columna corresponde a esta batería [Batería LiPo TERFPV 7.4V 2S 1500mAh](https://es.aliexpress.com/item/1005013087173451.html?src=google&src=google&albch=shopping&acnt=439-079-4345&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=es1005013087173451&ds_e_product_merchant_id=768446337&ds_e_product_country=ES&ds_e_product_language=es&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=21116729971&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=21106574823&gclid=CjwKCAjwuczWBhA9EiwAYGgEoSPQ7IYbAdVRAv9Uoe6RVCk6ZZY3ja0-4MXH9LLl2mKp4Hx8iOP8rRoCRg8QAvD_BwE)
