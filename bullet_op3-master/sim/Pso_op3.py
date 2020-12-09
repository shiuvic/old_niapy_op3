# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
import numpy as np
sys.path.append('/')

# End of fix

from NiaPy.algorithms.basic import ParticleSwarmAlgorithm
from NiaPy.algorithms.basic.ga import UniformCrossover, UniformMutation
from NiaPy.task import StoppingTask
from sphere import test123

# we will run Genetic Algorithm for 5 independent runs
data = []
for i in range(20):
    task = StoppingTask(D=6, nGEN=1, benchmark=test123())
    algo = ParticleSwarmAlgorithm(NP=1, vMin=-5.0, vMax=5.0)
    for j in range(1):
        algo.run(task=task)
        print("第 >%s< 次" % i)
        print("yes")
    data.append(task.return_conv()[1])
    print(data)
    np.savetxt('data.txt',data)
    # task.plot()

    # for i in range(50):
    #     task = StoppingTask(D=3, nGEN=20, benchmark=test(data_i=i), logger=True)
    #     algo = ParticleSwarmAlgorithm(NP=5, vMin=-5.0, vMax=5.0)
    #     print("step------------------------------------------------------------")
    #     for _ in range(20):
    #         algo.run(task)
    #     print(task.return_conv())
    #     np.save('C:/Users/willy/Desktop/mantis_python/test_mantis/controllers/python_mantis/PSO/1118/%d.npy' % i,
    #             task.return_conv())
    #     # task.plot()