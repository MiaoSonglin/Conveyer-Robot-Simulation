from controller import Camera
from controller import Robot


robot=Robot()
timestep = int(robot.getBasicTimeStep())
camera = robot.getDevice('camera')
camera.enable(32)

print("width:", camera.getWidth(),"Height:", camera.getHeight() )
print("getNear:", camera.getNear() )
camera.hasRecognition()
camera.recognitionEnable(32)
while robot.step(timestep) != -1:
    pass




