# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
import numpy as np
sys.path.append('/')

# End of fix
from NiaPy.algorithms.basic import ArtificialBeeColonyAlgorithm
from NiaPy.task import StoppingTask
from sphere import test123

# we will run Genetic Algorithm for 5 independent runs
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//abc//best_par.txt', 'w')
f.write('first_line')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//abc//best_val.txt', 'w')
f.write('100.0')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//abc//all_data.txt', 'w')
f.write('first_line')
f.close()
for i in range(50):
    f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//abc//data(%s).txt'% i, 'w')
    f.write('100.0')
    f.close()
    task = StoppingTask(D=6, nGEN=43, benchmark=test123(data_count = i),logger=True)
    algo = ArtificialBeeColonyAlgorithm(NP=5, Limit=2)
    algo.run(task=task)
    print("第 >%s< 次" % i)
    print("yes")
    print(task.return_conv())

