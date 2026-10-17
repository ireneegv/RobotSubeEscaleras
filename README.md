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
### Materiales:

- <a href="https://eu.robotshop.com/es/products/servo-de-alta-velocidad-con-retroalimentacion-de-360%C2%BA-parallax?gad_source=1&gad_campaignid=20151977646&gclid=CjwKCAjw88HWBhA3EiwAo2Zd6Jef_sOjay0D-MVZ2EdZULnVFxpq6SfI-ABb1wPAqvAF3BfwqhCEpxoCuRAQAvD_BwE&_su_rec=rLdseOBKBaEEp6T-TpOoVvnIQOqD0Sc1rRXsHfTcqa7XqecSJ2XMHrR5i1DIwBJ2qEo1VbKuYzDw4eobAEKpMy6NFoBo08E9SmB-tD8Z9MT3m0b1MeNX0PIox8Yp5_POjJIzJXUr68cGyd2yn89NNwMinb_2bcF7bPQcsO8AvA2aMg9PhvmjAKHx7dAvyG0UU9XhUa_1Z9cmJUhf-N2VPIOKcWtwSaqRy7tBVLXKeLHtn2_4EXHrI9mHb3w&_su_rec_id=751f40d6-1e14-4ada-8d24-98c52aae8cec-1792080001" target="_blank">
  servo Parallax Feedback 360 (x3)
</a>

Corriente de los motores (Im) = 0,15 A

Corriente de arranque (Ia) = 1,2 A

- <a href="https://www.electrohobby.es/esp32/448-esp32-devkit.html" target="_blank">
  ESP32
</a>

Corriente de la tarjeta (Ib) = 0,5 A


- <a href="https://electronicaymas.com/movimiento/modulo-ultrasonido-para-arduino-700?gad_source=1&gad_campaignid=17297688630&gclid=CjwKCAjw88HWBhA3EiwAo2Zd6M3Y-1ZefiVBVX1ADatzS5J_iHjAX1mjm9LTxAz0ObsYp-F9YTpF7RoCrl0QAvD_BwE" target="_blank">
Ultrasonido
</a>
corriente de dispositivo (Id) = 0,015 A

- <a href="https://electronicaymas.com/movimiento/modulo-ultrasonido-para-arduino-700?gad_source=1&gad_campaignid=17297688630&gclid=CjwKCAjw88HWBhA3EiwAo2Zd6M3Y-1ZefiVBVX1ADatzS5J_iHjAX1mjm9LTxAz0ObsYp-F9YTpF7RoCrl0QAvD_BwE" target="_blank">
  </a>
  
Batería -> Especificada en la Carpeta "Bateria"
  
 
Para elegir la batería hemos usado este cálculo para sacar la tasa de descarga, teniendo en cuenta los componentes que hemos nombrado anteriormente.

```
Idis = Ia*3 + Ib + Id
It = Im*3 + Ib + Id 

C = Idis/It = 3,815/0,665 = 5,736842105
```

## Video Modelo 1

https://github.com/user-attachments/assets/8579e925-4092-4993-b2e3-47c2c2166304

