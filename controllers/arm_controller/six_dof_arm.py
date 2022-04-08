# 导入Robot及其他相关库文件
from protobot.webots import Robot
from protobot.webots.motor import MotorFactory
from protobot.webots.hand_module import HandModuleFactory
from kinematics import invKine
import numpy as np
from math import pi

# 创建六自由度机械臂类作为Robot的子类
class SixDofArm(Robot):
    # 构造方法，初始化机械臂所用的所有电机
    def __init__(self):
        super(SixDofArm, self).__init__()
        self.add_device('M1', MotorFactory(), reduction = 44)
        self.add_device('M2', MotorFactory(), reduction = 44)
        self.add_device('M3', MotorFactory(), reduction = 44)
        self.add_device('M4', MotorFactory(), reduction = 44)
        self.add_device('M5', MotorFactory(), reduction = 44)
        self.add_device('M6', MotorFactory(), reduction = 44)
        self.motors = [
            self.device('M1'),
            self.device('M2'),
            self.device('M3'),
            self.device('M4'),
            self.device('M5'),
            self.device('M6'),
        ]
        self.hand = self.add_device('hand', HandModuleFactory())
        for i in range(6):
            self.motors[i].position_traj_mode(1.57, 5)
        
    # 机械臂复位函数
    def home(self):
        for i in range(6):
            self.motors[i].set_pos(0)
        self.hand.set_pos(0)
    
    def set_hand(self, pos):
        self.hand.set_pos(pos)
            
    # 机械臂示例位置函数
    def demo_pose(self):
        self.motors[0].set_pos(-0.6)
        self.motors[1].set_pos(0.5)
        self.motors[2].set_pos(1)
        self.motors[3].set_pos(-0.9)
        self.motors[4].set_pos(1.57)
        self.motors[5].set_pos(3.14)
        self.hand.set_pos(0.5)
        
    
    # 逆运动学算法
    def inverse_kinemetics(self, x, y, z, ):
        np_pose = np.matrix(
          [[0, -1,  0,  -z],
          [ -1, 0, 0, -x],
          [ 0, 0,  -1,  y],
          [ 0,  0,  0,  1]]
        )
        pos_arr = invKine(np_pose)[:,2]
        pos_arr[0] = pos_arr[0,0]
        pos_arr[1] = pi/2.0 + pos_arr[1,0]
        pos_arr[2] = -pos_arr[2,0]
        pos_arr[3] = pi/2.0 + pos_arr[3,0]
        pos_arr[4] = pos_arr[4,0]
        pos_arr[5] = pi + pos_arr[5]
        for i in range(6):
            if pos_arr[i,0] > pi:
                pos_arr[i,0] -=2*pi
                self.motors[i].set_pos(pos_arr[i,0])
            else:
                self.motors[i].set_pos(pos_arr[i,0])