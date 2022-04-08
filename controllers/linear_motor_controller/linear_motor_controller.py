from protobot.webots import Robot
from protobot.webots.linear_module import LinearModuleFactory

robot = Robot()

motor = robot.add_device('motor', LinearModuleFactory())

motor.set_pos(-0.05)

robot.delay(5)

motor.set_pos(0.05)

robot.delay(10)

motor.set_pos(0)
