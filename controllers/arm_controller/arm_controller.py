# 导入自己创建的六自由度机械臂库文件
from six_dof_arm import SixDofArm

# 创建六自由度机械臂类型的对象arm
arm = SixDofArm()

# 机械臂使能
arm.enable()

# 机械臂末端运动到(x=0m, y=0.25m, z=-0.2m)的目标位置
arm.inverse_kinemetics(0.2,0.25,0)
arm.delay(2)

arm.inverse_kinemetics(0,0.25,-0.25)
arm.delay(1)
# 机械手爪控制打开
arm.set_hand(1)
arm.delay(2)

# 机械臂末端缓慢运动到(x=0m, y=0.25m, z=-0.2m)的目标位置
for i in range(250, -5, -1):
    height = i / 1000.0
    arm.inverse_kinemetics(0,height,-0.25)
    arm.delay(0.032)
arm.delay(2)

arm.set_hand(0.5)
arm.delay(1)
# 机械臂末端缓慢运动到(x=0m, y=0.25m, z=-0.2m)的目标位置
for i in range(250, 160, -1):
    height = i / 1000.0
    arm.inverse_kinemetics(0,height,0.2)
    arm.delay(0.032)
arm.delay(1)

arm.set_hand(1)
arm.delay(1)

for i in range(160, 250, 1):
    height = i / 1000.0
    arm.inverse_kinemetics(0,height,0.2)
    arm.delay(0.032)
arm.delay(1)

arm.home()
#arm.delay(5)

# 机械臂失能
arm.disable()
