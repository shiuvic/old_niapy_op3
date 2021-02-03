# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

from NiaPy.algorithms.basic import FireflyAlgorithm
from NiaPy.task import StoppingTask
from sphere import test123

# we will run Grey Wolf Optimizer for 5 independent runs
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//fa//best_par.txt', 'w')
f.write('first_line')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//fa//best_val.txt', 'w')
f.write('100.0')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//fa//all_data.txt', 'w')
f.write('first_line')
f.close()
for i in range(50):
    f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//fa//data(%s).txt' % i, 'w')
    f.write('100.0')
    f.close()
    task = StoppingTask(D=6, nGEN=50, benchmark=test123(data_count=i))
    algo = FireflyAlgorithm(NP=5, alpha=0.5, betamin=0.2, gamma=1.0)
    algo.run(task=task)
    print("第 >%s< 次" % i)
    print("yes")
    # data.append(task.return_conv()[1])
    print(task.return_conv())