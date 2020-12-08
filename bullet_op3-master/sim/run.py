from walker import Walker
from core.op3 import OP3
from walking.wfunc import WFunc
import time
import numpy as np
walker = Walker(fallen_reset=True)
walker.reset_and_start()
# noinspection PyUnreachableCode
def run(x_vel, y_vel, ang_vel,parameters,walk_offset):
    walker.update_new_vel(x_vel, y_vel, ang_vel,parameters,walk_offset)
    time.sleep(1)

    while True:
        if walker.fall:
            return (walker.robot_postion())
        time.sleep(0.001)


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