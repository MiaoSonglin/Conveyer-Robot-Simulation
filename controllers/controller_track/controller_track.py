from controller import Robot

from multiprocessing.connection import Listener

robot = Robot()
timestep = int(robot.getBasicTimeStep())
listener = Listener(('localhost', 6001))
conn = listener.accept()


motor_belt = robot.getDevice("belt_motor")
motor_belt.setVelocity(0.08)
motor_belt.setPosition(float('+inf'))

while robot.step(timestep) != -1:
    if conn.poll():
        msg = conn.recv()
        if msg == 'stop':
            motor_belt.setVelocity(0)
            robot.step(300*timestep)
        if msg == 'start':
            motor_belt.setVelocity(0.08)

conn.close()
listener.close()
