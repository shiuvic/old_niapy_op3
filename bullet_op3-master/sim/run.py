from walker import Walker
from core.op3 import OP3
from walking.wfunc import WFunc
import time
import math
import numpy as np
walker = Walker(fallen_reset=True)
walker.reset_and_start()
# noinspection PyUnreachableCode
def run(x_vel, y_vel, ang_vel,parameters,walk_offset):
    walker.update_new_vel(x_vel, y_vel, ang_vel,parameters,walk_offset)
    time.sleep(1)

    while True:
        if walker.fall:
            print(_angle_(0,0,walker.robot_postion()[1],walker.robot_postion()[2]))
            return (walker.robot_postion())
        time.sleep(0.001)

def _angle_(x1,  y1,  x2,  y2):
    angle = 0.0;
    dx = x2 - x1
    dy = y2 - y1
    if  x2 == x1:
        angle = math.pi / 2.0
        if  y2 == y1 :
            angle = 0.0
        elif y2 < y1 :
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif  x2 > x1 and  y2 < y1 :
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif  x2 < x1 and y2 < y1 :
        angle = math.pi + math.atan(dx / dy)
    elif  x2 < x1 and y2 > y1 :
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    ans = float(angle * 180 / math.pi)
    return(ans)

# x_vel=1
# y_vel=0
# ang_vel=0
# parameters,walk_offset


# for i in range (100):
#     walk_offset = {'hip_pitch': i/-0.063,
#                    'hip_roll': 0.0,
#                    'hip_yaw': 0.0,
#                    'ank_pitch': 0.0,
#                    'ank_roll': 0.0,
#                    'knee': 0.0}
#
#     parameters = {"swing_scale": 0.0,
#                   "step_scale": i/0.3,
#                   "step_offset": i/0.55,
#                   "ankle_offset": 0.0,
#                   "vx_scale": i/0.5,
#                   "vy_scale": i/0.5,
#                   "vt_scale": i/0.4}
#     print(parameters, walk_offset)
#     x = run(1, 0, 0, parameters, walk_offset)
#     val = np.linalg.norm(x-[0.0,0.0,0.0])
#     print(val)
# parameters
# walk_offset

# swing_scale:0.0
# step_scale:0.3
# step_offset:0.55
# ankle_offset:0.0
# vx_scale:0.5
# vy_scale:0.5
# vt_scale:0.4
# hip_pitch:-1.1517569271716863
# hip_roll:-0.8454785372846194
# hip_yaw:-1.0792401690158298
# ank_pitch:0.25254711154731346
# ank_roll:-1.2883878593363458
# knee:1.2376552675268

walk_offset = {'hip_pitch': -0.063,
               'hip_roll': 0.0,
               'hip_yaw': 0.0,
               'ank_pitch': 0.0,
               'ank_roll': 0.0,
               'knee': 0.0}

parameters = {'swing_scale': 0.0, 'step_scale': 0.6, 'step_offset': 0.6, 'ankle_offset': 0.0, 'vx_scale': 0.22864225192302623, 'vy_scale': -0.5829433017784157, 'vt_scale': 0.2969009519162831}



# swing_scale:0.0
# step_scale:-0.10506553676292368
# step_offset:-0.36615762158925014
# ankle_offset:0.0
# vx_scale:-0.6
# vy_scale:-0.4848915309603625
# vt_scale:0.05057566580486009
# hip_pitch:-0.063
# hip_roll:0.0
# hip_yaw:0.0
# ank_pitch:0.0
# ank_roll:0.0
# knee:0.0



print(run(1,0,0,parameters,walk_offset))