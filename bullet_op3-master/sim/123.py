# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

sys.path.append('/')

# End of fix

from NiaPy.algorithms.basic import GeneticAlgorithm ,ParticleSwarmAlgorithm
from NiaPy.algorithms.basic.ga import UniformCrossover, UniformMutation
from NiaPy.task import StoppingTask
import sphere

# we will run Genetic Algorithm for 5 independent runs
for i in range(50):
    task = StoppingTask(D=6, nGEN=1, benchmark=sphere.test123())
    algo = ParticleSwarmAlgorithm(NP=1, vMin=-4.0, vMax=4.0)
    for j in range(1):
        algo.run(task=task)
        print("第--%d--次" % i+1)
        print("yes")
    # print('%s -> %s' % (best[0], best[1]))
    print(task.return_conv())
