from controller import Robot

robot_belt = Robot()
timestep2 = int(robot_belt.getBasicTimeStep())
motor_belt = robot_belt.getDevice("belt_motor")
motor_belt.setVelocity(0.05)
motor_belt.setPosition(float('+inf'))
