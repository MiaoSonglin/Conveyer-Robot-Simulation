# 导入Robot库文件
from protobot.webots import Robot
from protobot.webots.motor import MotorFactory

# 创建机器人类型的对象robot
robot = Robot()

# 获取并打印当前时间
print('current time:')
print(robot.time())

# 机器人添加电机，名字'motor'（对应模型中的底座电机），减速比12.45
robot.add_device('motor', MotorFactory(), reduction = 12.45)

# 从机器人中获取刚刚添加的名字为'motor'的电机对象motor
motor = robot.device('motor')

# 位置模式
motor.position_mode()
# 机器人使能
robot.enable()

motor.set_pos(3.14) # 电机发送运动到π(180°)的位置指令
robot.delay(2.5) #延时2.5s
motor.set_pos(0) # 电机发送运动到0(0°)的位置指令
robot.delay(2.5) #延时2.5s
 
# 机器人失能
robot.disable()

# 轨迹位置模式，设置速度，加速度
motor.position_traj_mode(max_vel=2.5,max_acc=10)
robot.enable()

motor.set_pos(6.28) # 电机发送运动到2π(360°)的位置指令
robot.delay(5)
motor.set_pos(0) # 电机发送运动到0(0°)的位置指令
robot.delay(5)
 
robot.disable()

 
# 速度模式
motor.velocity_mode()
robot.enable()
 
motor.set_vel(3.14) #电机发送以π/s(180°/s)速度转动的速度指令
robot.delay(3)
motor.set_vel(-3.14) #电机发送以-π/s(-180°/s)速度转动的速度指令
robot.delay(3)
motor.set_vel(0)
robot.delay(1)

robot.disable()

# 匀加速速度模式，设置加速度
motor.velocity_ramp_mode(ramp = 1.57)
robot.enable()

motor.set_vel(3.14) #电机发送以π/s(180°/s)速度转动的速度指令
robot.delay(5)
motor.set_vel(-3.14) #电机发送以-π/s(-180°/s)速度转动的速度指令
robot.delay(7)
motor.set_vel(0)
robot.delay(1)

robot.disable()
