# 导入Robot及其他相关库文件
from protobot.webots import Robot
from protobot.webots.motor import MotorFactory
from protobot.webots.linear_module import LinearModuleFactory
from math import pi

# 创建机械臂类作为Robot的子类
class ScaraDofArm(Robot):
    # 构造方法，初始化机械臂所用的所有电机
    def __init__(self):
        super(ScaraDofArm, self).__init__()
        self.add_device('M1', LinearModuleFactory())
        self.add_device('M2', MotorFactory(), reduction = 44)
        self.add_device('M3', MotorFactory(), reduction = 44)
        self.add_device('M4', MotorFactory(), reduction = 44)
        self.motors = [
            self.device('M1'),
            self.device('M2'),
            self.device('M3'),
            self.device('M4'),
        ]
        for i in range(1,4):
            self.motors[i].position_traj_mode(1.57, 5)
        
    # 机械臂复位函数
    def home(self):
        for i in range(4):
            self.motors[i].set_pos(0)
            self.motors[0].set_pos(0.04)
            self.motors[1].set_pos(0.6)
            self.motors[2].set_pos(0.6)
    
    def test1(self):
        self.motors[0].set_pos(0.04)
        self.motors[1].set_pos(-1.4)
        self.motors[2].set_pos(-1.57)
        self.motors[3].set_pos(-1.57)

    def test2(self):
        self.motors[0].set_pos(-0.05)
        self.motors[1].set_pos(-1)
        self.motors[2].set_pos(1.2)
        self.motors[3].set_pos(1.57)
        
arm = ScaraDofArm()
arm.enable()
arm.home()
arm.delay(15)
arm.test1()
arm.delay(6)
arm.test2()
arm.delay(3)
arm.home()