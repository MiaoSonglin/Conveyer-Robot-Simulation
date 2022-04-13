# 导入自己创建的六自由度机械臂库文件
from six_dof_arm import SixDofArm

from multiprocessing.connection import Listener

arm = SixDofArm()

listener = Listener(('localhost', 6000))
conn = listener.accept()

arm.enable()

while arm.delay(0.032) != -1:
    if conn.poll():
        print("new solid")
        msg = conn.recv()
        x, y = msg.split(',')
        x = float(x)
        y = float(y)
        robot_x = (y + 69)/1555.5
        robot_z = (500 - x)/1760.0
        print(robot_x, robot_z)

        arm.inverse_kinemetics(robot_x, 0.25, robot_z - 0.009)
        arm.set_hand(1)
        arm.delay(1.6)

        for i in range(250, 160, -1):
            height = i / 1000.0
            arm.inverse_kinemetics(robot_x, height, robot_z - 0.009)
            arm.delay(0.032)
        arm.delay(0.96)

        arm.set_hand(0.5)
        arm.delay(0.96)

        for i in range(160, 250, 1):
            height = i / 1000.0
            arm.inverse_kinemetics(robot_x, height, robot_z - 0.009)
            arm.delay(0.032)
        arm.delay(0.96)

        arm.inverse_kinemetics(0.03, 0.2, 0.3)
        arm.delay(0.96)

        for i in range(200, 110, -1):
            height = i / 1000.0
            arm.inverse_kinemetics(0.03, height, 0.3)
            arm.delay(0.032)
        arm.delay(0.96)
        arm.set_hand(1)


conn.close()
conn2.close()
listener.close
