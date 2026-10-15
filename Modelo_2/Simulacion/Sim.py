import pybullet as p
import pybullet_data
import time
import os

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.81)
p.setTimeStep(1.0 / 240.0)

p.loadURDF("plane.urdf")

robot_path = os.path.abspath("Modelo1/urdf/unnamed.urdf")

robotId = p.loadURDF(
    robot_path,
    basePosition=[0, 0, 1.0],
    useFixedBase=False,
    flags=p.URDF_USE_SELF_COLLISION
)

# Buscar las articulaciones
transversal = None
nexos = []

for i in range(p.getNumJoints(robotId)):
    info = p.getJointInfo(robotId, i)
    nombre = info[1].decode()

    print(f"Articulación {i}: {nombre} | Tipo: {info[2]}")

    if nombre == "Transversal_link_joint":
        transversal = i

    elif nombre in [
        "Nexo_Pata_D_link_joint",
        "Nexo_Pata_I_link_joint"
    ]:
        nexos.append(i)

# Slider de la transversal
slider_transversal = p.addUserDebugParameter(
    "Transversal",
    -3.14,
    3.14,
    0.0
)

# Slider compartido para los dos nexos
slider_nexos = p.addUserDebugParameter(
    "Nexos (ambos)",
    -3.14,
    3.14,
    0.0
)

p.resetDebugVisualizerCamera(
    cameraDistance=2.5,
    cameraYaw=45,
    cameraPitch=-25,
    cameraTargetPosition=[0, 0, 0.5]
)

print("\nMueve los sliders para controlar el robot.")
print("Nexos encontrados:", nexos)

try:
    while p.isConnected():

        # Control de la transversal
        posicion_transversal = p.readUserDebugParameter(
            slider_transversal
        )

        if transversal is not None:
            p.setJointMotorControl2(
                robotId,
                transversal,
                p.POSITION_CONTROL,
                targetPosition=posicion_transversal,
                force=100
            )

        # Control simultáneo de ambos nexos
        posicion_nexos = p.readUserDebugParameter(slider_nexos)

        for articulacion in nexos:
            p.setJointMotorControl2(
                robotId,
                articulacion,
                p.POSITION_CONTROL,
                targetPosition=posicion_nexos,
                force=100
            )

        p.stepSimulation()
        time.sleep(1.0 / 240.0)

except KeyboardInterrupt:
    pass

finally:
    if p.isConnected():
        p.disconnect()