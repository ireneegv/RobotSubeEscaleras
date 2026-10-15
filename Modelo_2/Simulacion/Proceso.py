import pybullet as p
import time
import math
import pybullet_data
import time
import os

# ==========================================
# CONFIGURACIÓN DE PYBULLET
# ==========================================

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.setTimeStep(1.0 / 240.0)

p.loadURDF("plane.urdf")

# ==========================================
# CARGAR ROBOT Y ESCALERA
# ==========================================

escalera_path = os.path.abspath("Modelo1/urdf/Escalera.urdf")
robot_path = os.path.abspath("Modelo1/urdf/Modelo1.urdf")

robotId = p.loadURDF(
    robot_path,
    basePosition=[0, 0, 0.1],
    useFixedBase=False,
    flags=p.URDF_USE_SELF_COLLISION
)

escaleraId = p.loadURDF(
    escalera_path,
    basePosition=[0, -0.09, 0],
    baseOrientation=p.getQuaternionFromEuler(
        [0, 0, -math.pi / 2]
    ),
    useFixedBase=True
)

# ==========================================
# CONFIGURAR FRICCIÓN DE LA ESCALERA
# ==========================================

for i in range(-1, p.getNumJoints(escaleraId)):
    p.changeDynamics(
        escaleraId,
        i,
        lateralFriction=1.5,
        spinningFriction=0.1,
        rollingFriction=0.1
    )



# ==========================================
# BUSCAR ARTICULACIONES
# ==========================================

transversal = None
nexos = []

for i in range(p.getNumJoints(robotId)):
    info = p.getJointInfo(robotId, i)
    nombre = info[1].decode()

    print(
        f"Articulación {i}: {nombre} | Tipo: {info[2]}"
    )

    if nombre == "Transversal_link_joint":
        transversal = i

    elif nombre in [
        "Nexo_Pata_D_link_joint",
        "Nexo_Pata_I_link_joint"
    ]:
        nexos.append(i)

# Comprobar que se han encontrado las articulaciones
if transversal is None:
    raise RuntimeError(
        "No se ha encontrado Transversal_link_joint"
    )

if len(nexos) != 2:
    raise RuntimeError(
        f"Se esperaban 2 nexos, pero se encontraron {len(nexos)}"
    )

print("\nTransversal encontrada:", transversal)
print("Nexos encontrados:", nexos)

# ==========================================
# PARÁMETROS DEL CONTROLADOR
# ==========================================

FUERZA = 100
VELOCIDAD = 1.0

# Tolerancia de 2 grados
TOLERANCIA = math.radians(2)

# Ángulos objetivo en radianes
ANGULO_0 = math.radians(0)
ANGULO_45 = math.radians(45)
ANGULO_N45 = math.radians(-45)
ANGULO_90 = math.radians(90)
ANGULO_N90 = math.radians(-90)
ANGULO_180 = math.radians(180)
ANGULO_270 = math.radians(270)
ANGULO_360 = math.radians(360)



# ==========================================
# DEFINIR SECUENCIA DE MOVIMIENTOS
# ==========================================

time.sleep(10)

secuencia = [
    {
        "nombre": "Nexos de las patas bajas a 45 grados",
        "articulaciones": nexos,
        "objetivo": ANGULO_N45
    },
    {
        "nombre": "Transversal a 90 grados",
        "articulaciones": [transversal],
        "objetivo": ANGULO_90
    },
    {
        "nombre": "Nexos de las patas bajas a 90 grados",
        "articulaciones": nexos,
        "objetivo": ANGULO_N90
    },
    {
            "nombre": "Nexos de las patas bajas a 90 grados",
            "articulaciones": nexos,
            "objetivo": ANGULO_0
    },
    {
            "nombre": "Nexos de las patas bajas a 90 grados",
            "articulaciones": [transversal],
            "objetivo": ANGULO_180
    },
    {
            "nombre": "Nexos de las patas bajas a 90 grados",
            "articulaciones": [transversal],
            "objetivo": ANGULO_270
    },
    {
            "nombre": "Nexos de las patas bajas a 90 grados",
            "articulaciones": [transversal],
            "objetivo": ANGULO_360
    }
]

# ==========================================
# CONFIGURAR CÁMARA
# ==========================================


# ==========================================
# CONTROLADOR AUTOMÁTICO
# ==========================================

etapa = 0

print("\n========================================")
print("INICIANDO CONTROLADOR AUTOMÁTICO")
print("========================================")

try:
    while p.isConnected() and etapa < len(secuencia):

        movimiento = secuencia[etapa]

        articulaciones_objetivo = movimiento["articulaciones"]
        objetivo = movimiento["objetivo"]

        # Enviar la posición objetivo a los motores
        for articulacion in articulaciones_objetivo:
            p.setJointMotorControl2(
                bodyUniqueId=robotId,
                jointIndex=articulacion,
                controlMode=p.POSITION_CONTROL,
                targetPosition=objetivo,
                force=FUERZA,
                maxVelocity=VELOCIDAD
            )

        # Comprobar si todas las articulaciones de la etapa
        # han alcanzado la posición objetivo
        alcanzado = True

        for articulacion in articulaciones_objetivo:
            estado = p.getJointState(
                robotId,
                articulacion
            )

            posicion_actual = estado[0]

            if abs(posicion_actual - objetivo) > TOLERANCIA:
                alcanzado = False
                break

        # Actualizar la simulación
        p.stepSimulation()
        time.sleep(1.0 / 240.0)

        # Pasar a la siguiente etapa
        if alcanzado:
            print(
                f"\nMovimiento completado: {movimiento['nombre']}"
            )

            etapa += 1

            if etapa < len(secuencia):
                print(
                    f"Siguiente movimiento: "
                    f"{secuencia[etapa]['nombre']}"
                )

    # ======================================
    # MANTENER EL ROBOT EN LA POSICIÓN FINAL
    # ======================================

    if p.isConnected() and etapa == len(secuencia):

        print("\nSecuencia completada.")
        print("Manteniendo la posición final del robot.")

        while p.isConnected():
            p.stepSimulation()
            time.sleep(1.0 / 240.0)

except KeyboardInterrupt:
    print("\nSimulación interrumpida por el usuario.")

finally:
    if p.isConnected():
        p.disconnect()