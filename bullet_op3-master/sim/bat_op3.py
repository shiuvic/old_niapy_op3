# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
import numpy as np
sys.path.append('/')

# End of fix
from NiaPy.algorithms.basic import BatAlgorithm
from NiaPy.task import StoppingTask
from sphere import test123

# we will run Genetic Algorithm for 5 independent runs
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//bat//best_val.txt', 'w')
f.write('1.0')
f.close()
for i in range(50):
    f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//bat//data(%s).txt'% i, 'w')
    f.write('-0.000001')
    f.close()
    task = StoppingTask(D=6, nGEN=20, benchmark=test123(data_count = i))
    algo = BatAlgorithm(NP=5)
    for _ in range(20):
        algo.run(task=task)
        print("第 >%s< 次" % i)
        print("yes")
    # data.append(task.return_conv()[1])
        print(task.return_conv())
