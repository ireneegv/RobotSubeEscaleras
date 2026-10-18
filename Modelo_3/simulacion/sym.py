import pybullet as p
import pybullet_data
import time
import math

MIN_LINK1 = -math.pi
MAX_LINK1 = 10*math.pi
MIN_LINK3 = -math.pi
MAX_LINK3 = math.pi

INIT_LINK1 = 0
INIT_LINK2 = 0
INIT_LINK3 = 0



LATERAL_FRICTION_ = 1
ROLLING_FRICTION_ = 0.2
SPINNING_FRICTION_ = 0.1

INIT_FORCE = 0

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

startPosR = [0,0,0.15]
startPosE1 = [0.5,-0.2,0.0825]
startPosE2 = [0.8,-0.2,0.2575]
startPosE3 = [1.1,-0.2,0.4225]

startOrientation = p.getQuaternionFromEuler([0,0,0])

robot = p.loadURDF("./robot/urdf/robot.urdf", startPosR, startOrientation)
escalon1 = p.loadURDF("./escalon/urdf/escalon.urdf", startPosE1, startOrientation, useFixedBase=True)
escalon2 = p.loadURDF("./escalon/urdf/escalon.urdf", startPosE2, startOrientation, useFixedBase=True)
escalon3 = p.loadURDF("./escalon/urdf/escalon.urdf", startPosE3, startOrientation, useFixedBase=True)
planeId = p.loadURDF("plane_transparent.urdf")

numJoints = p.getNumJoints(robot)

print("NumJoints: {}".format(numJoints))
for j in range(numJoints):
     print("{} - {}".format(p.getJointInfo(robot,j)[0], p.getJointInfo(robot,j)[1].decode("utf-8")))


giro1 = p.addUserDebugParameter("mover_base", MIN_LINK1, MAX_LINK1, INIT_LINK1)
giro3 = p.addUserDebugParameter("girar_base", MIN_LINK3, MAX_LINK3, INIT_LINK3)

p.changeDynamics(robot, 5, lateralFriction=LATERAL_FRICTION_)
p.changeDynamics(robot,  5, spinningFriction=SPINNING_FRICTION_)
p.changeDynamics(robot, 5, rollingFriction=ROLLING_FRICTION_)


p.changeDynamics(robot, 0, lateralFriction=LATERAL_FRICTION_)
p.changeDynamics(robot,  0, spinningFriction=SPINNING_FRICTION_)
p.changeDynamics(robot, 0, rollingFriction=ROLLING_FRICTION_)



try:
    while True:
        p.stepSimulation()
        time.sleep(1./240.)

        link_1 = p.readUserDebugParameter(giro1)
        link_3 = p.readUserDebugParameter(giro3)

        
        p.setJointMotorControlArray(robot, [1, 3], p.POSITION_CONTROL, targetPositions=[link_1, link_1], 
                            forces = [3, 3])
        p.setJointMotorControlArray(robot, [2, 4], p.POSITION_CONTROL, targetPositions=[-link_1, -link_1], 
                        forces = [3, 3])

    

        p.setJointMotorControl2(bodyIndex=robot,
                                    jointIndex=0,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=link_3,
                                    targetVelocity=0,
                                    force=2)


except KeyboardInterrupt:
      pass

p.disconnect()    