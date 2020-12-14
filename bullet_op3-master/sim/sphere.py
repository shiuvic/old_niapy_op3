# encoding=utf8

"""Sphere benchmarks."""

from numpy import abs
from NiaPy.benchmarks.benchmark import Benchmark
from walking.wfunc import WFunc
from walker import Walker
import numpy as np
from savetxt import savefit
# __all__ = ['Sphere', 'Sphere2', 'Sphere3']
from run import run
class test123(Benchmark):
	r"""Implementation of Sphere functions.

	Date: 2018

	Authors: Iztok Fister Jr.

	License: MIT

	Function: **Sphere function**

		:math:`f(\mathbf{x}) = \sum_{i=1}^D x_i^2`

		**Input domain:**
		The function can be defined on any input domain but it is usually
		evaluated on the hypercube :math:`x_i ∈ [0, 10]`, for all :math:`i = 1, 2,..., D`.

		**Global minimum:** :math:`f(x^*) = 0`, at :math:`x^* = (0,...,0)`

	LaTeX formats:
		Inline:
				$f(\mathbf{x}) = \sum_{i=1}^D x_i^2$

		Equation:
				\begin{equation}f(\mathbf{x}) = \sum_{i=1}^D x_i^2 \end{equation}

		Domain:
				$0 \leq x_i \leq 10$

	Reference paper:
		Jamil, M., and Yang, X. S. (2013).
		A literature survey of benchmark functions for global optimisation problems.
		International Journal of Mathematical Modelling and Numerical Optimisation,
		4(2), 150-194.
	"""
	Name = ['Sphere']

	def __init__(self, Lower=-0.6, Upper=0.6, count = 0 , data_count = 0):
		r"""Initialize of Sphere benchmark.

		Args:
			Lower (Optional[float]): Lower bound of problem.
			Upper (Optional[float]): Upper bound of problem.

		See Also:
			:func:`NiaPy.benchmarks.Benchmark.__init__`
		"""
		Benchmark.__init__(self, Lower, Upper)
		self.count = count
		self.data_count = data_count
	@staticmethod
	def latex_code():
		r"""Return the latex code of the problem.

		Returns:
			str: Latex code
		"""
		return r'''$f(\mathbf{x}) = \sum_{i=1}^D x_i^2$'''

	def function(self):
		r"""Return benchmark evaluation function.

		Returns:
			Callable[[int, Union[int, float, List[int, float], numpy.ndarray]], float]: Fitness function
		"""
		def evaluate(D, sol):
			r"""Fitness function.

			Args:
				D (int): Dimensionality of the problem
				sol (Union[int, float, List[int, float], numpy.ndarray]): Solution to check.

			Returns:
				float: Fitness value for the solution.
			"""
			# parameters = {"swing_scale": sol[0],
			# 				   "step_scale": sol[1],
			# 				   "step_offset": sol[2],
			# 				   "ankle_offset": sol[3],
			# 				   "vx_scale": sol[4],
			# 				   "vy_scale": sol[5],
			# 				   "vt_scale": sol[6]}
			# walk_offset = {'hip_pitch': sol[7],
			# 			   'hip_roll': sol[8],
			# 			   'hip_yaw': sol[9],
			# 			   'ank_pitch': sol[10],
			# 			   'ank_roll': sol[11],
			# 			   'knee': sol[12]}
			# run.update_param_ga(parameters,walk_offset)



			val = 0.0
			for i in range(D):
				val = sol[i]

			parameters = {"swing_scale": 0.0,
							   "step_scale": sol[1],
							   "step_offset": sol[2],
							   "ankle_offset": 0.0,
							   "vx_scale": sol[3],
							   "vy_scale": sol[4],
							   "vt_scale": sol[5]}
			walk_offset = {'hip_pitch': -0.063,
						   'hip_roll': 0.0,
						   'hip_yaw': 0.0,
						   'ank_pitch': 0.0,
						   'ank_roll': 0.0,
						   'knee': 0.0}

			for key, value in parameters.items():
				print('{key}:{value}'.format(key=key, value=value))
			for key, value in walk_offset.items():
				print('{key}:{value}'.format(key=key, value=value))
			x = run(1,0,0,parameters,walk_offset)
			val = (0 - np.linalg.norm(x - [0.0, 0.0, 0.0]))
			self.count += 1
			print("count=========================>",self.count)
			savefit(self.data_count,val)
			# for i in range(D):val += sol[i] ** 2
			print("----val------->",val)
			return val
		return evaluate
