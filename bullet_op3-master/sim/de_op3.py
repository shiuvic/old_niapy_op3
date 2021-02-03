# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

from NiaPy.algorithms.basic import DifferentialEvolution
from NiaPy.task import StoppingTask
from sphere import test123

# we will run Grey Wolf Optimizer for 5 independent runs

f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//de//best_par.txt', 'w')
f.write('first_line')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//de//best_val.txt', 'w')
f.write('100.0')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//de//all_data.txt', 'w')
f.write('first_line')
f.close()
for i in range(50):
    f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//de//data(%s).txt' % i, 'w')
    f.write('100.0')
    f.close()
    task = StoppingTask(D=6, nGEN=40, benchmark=test123(data_count=i))
    algo = DifferentialEvolution(NP=5, F=0.5, CR=0.9)
    algo.run(task=task)
    print("第 >%s< 次" % i)
    print("yes")
    # data.append(task.return_conv()[1])
    print(task.return_conv())