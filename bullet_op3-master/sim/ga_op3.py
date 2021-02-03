# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('/')

# End of fix
from NiaPy.algorithms.basic import GeneticAlgorithm
from NiaPy.algorithms.basic.ga import UniformCrossover, UniformMutation
from NiaPy.task import StoppingTask
from sphere import test123

# we will run Genetic Algorithm for 5 independent runs
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//ga//best_par.txt', 'w')
f.write('first_line')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//ga//best_val.txt', 'w')
f.write('100.0')
f.close()
f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//ga//all_data.txt', 'w')
f.write('first_line')
f.close()
for i in range(50):
    f = open('C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//ga//data(%s).txt'% i, 'w')
    f.write('100.0')
    f.close()
    task = StoppingTask(D=6, nGEN=40, benchmark=test123(data_count = i))
    algo = GeneticAlgorithm(NP=5, Crossover=UniformCrossover, Mutation=UniformMutation, Cr=0.45, Mr=0.9)
    for j in range(20):
        algo.run(task=task)
        print(task.return_conv())
