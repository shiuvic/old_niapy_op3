# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
import numpy as np
sys.path.append('/')
# End of fix
from NiaPy.algorithms.basic import ParticleSwarmAlgorithm
from NiaPy.task import StoppingTask
from sphere import test123

# we will run Genetic Algorithm for 5 independent runs
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//pso//best_par.txt', 'w')
f.write('first_line')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//pso//best_val.txt', 'w')
f.write('100.0')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//pso//all_data.txt', 'w')
f.write('first_line')
f.close()

for i in range(50):
    f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//pso//data(%d).txt'% i, 'w')
    f.write('100')
    f.close()
    task = StoppingTask(D=6, nGEN=40, benchmark=test123(data_count = i))
    algo = ParticleSwarmAlgorithm(NP=5, vMin=-5.0, vMax=5.0)
    algo.run(task=task)
    print("第 >%s< 次" % i)
    print(task.return_conv())
