from functools import reduce
from itertools import product
from .boolean import *


class SystemEquation:
	def __init__(self, equations):
		self.equations = equations
		self.system = reduce(Conjunction, self.equations)
		self.names = [str(t) for t in terms(self.system)]
		self.terms = terms(self.system)

	def count(self):
		s = 0
		for row in product([False, True], repeat=len(self.terms)):
			if self.system(**dict(zip(self.names, row))):
				s += 1
		return s

	def __str__(self):
		return '\\[ \\begin{cases}' + ' \\\\ '.join(map(str, self.equations)) + '\\end{cases} \\]'
