"""Реализация логических констант, переменных, унарных и бинарных операций, скобок в логических выражениях."""


class Term:
	"""Базовый класс для всех термов логического выражения."""
	pass


class Variable(Term):
	"""Логическая переменная."""
	def __init__(self, name):
		assert(type(name) == str)
		self.family = name[0]
		self.order = int(name[1:])

	def __repr__(self):
		return self.family + '_{' + str(self.order) + '}'

	def __str__(self):
		return self.family + str(self.order)

	def __call__(self, **kwargs):
		return kwargs[str(self)]

	def __hash__(self):
		return hash(str(self))

	def __eq__(self, other):
		return self.family == other.family and self.order == other.order


class Constant(Term):
	"""Логическая константа."""
	pass


class TrueConst(Constant):
	"""Логическая истина."""
	@staticmethod
	def __repr__():
		return '1'

	@staticmethod
	def __call__(**kwargs):
		return True


class FalseConst(Constant):
	"""Логическая ложь."""
	@staticmethod
	def __repr__():
		return '0'

	@staticmethod
	def __call__(**kwargs):
		return False


class LogicOperation(Term):
	"""Базовый класс для логических операций."""
	pass


class UnaryLogicOperation(LogicOperation):
	"""Базовый класс для унарных логических операций и скобок."""
	def __init__(self, *args):
		assert(len(args) == 1)
		self.args = args

	def __repr__(self):
		return self.repr + ' ' + repr(self.args[0])

	def __str__(self):
		return self.symbol + ' ' + str(self.args[0])

	def __call__(self, **kwargs):
		return self.operation(self.args[0](**kwargs))


class Positive(UnaryLogicOperation):
	"""Тривиальная обёртка над логическим термом."""
	repr = ''
	symbol = ''

	@staticmethod
	def operation(a):
		return a


class Negation(UnaryLogicOperation):
	"""Отрицание."""
	repr = '\\overline'
	symbol = '!'

	@staticmethod
	def operation(a):
		return not a


class Brackets(UnaryLogicOperation):
	"""Скобки, используются для повышения приоритета логической операции."""
	@staticmethod
	def operation(a):
		return a

	def __repr__(self):
		return '\\left(' + ' ' + repr(self.args[0]) + ' ' + '\\right)'

	def __str__(self):
		return '(' + str(self.args[0]) + ')'


class BinaryLogicOperation(LogicOperation):
	"""Базовый класс для бинарных логических операций."""
	def __init__(self, *args):
		assert(len(args) == 2)
		self.args = args

	def __repr__(self):
		return repr(self.args[0]) + ' ' + self.repr + ' ' + repr(self.args[1])

	def __str__(self):
		return str(self.args[0]) + ' ' + self.symbol + ' ' + str(self.args[1])

	def __call__(self, **kwargs):
		return self.operation(self.args[0](**kwargs), self.args[1](**kwargs))


class Conjunction(BinaryLogicOperation):
	"""Коньюнкция."""
	repr = '\\wedge'
	symbol = '&'

	@staticmethod
	def operation(a, b):
		return a and b


class Disjunction(BinaryLogicOperation):
	"""Дизьюнкция."""
	repr = '\\vee'
	symbol = '|'

	@staticmethod
	def operation(a, b):
		return a or b


class Implication(BinaryLogicOperation):
	"""Импликация."""
	repr = '\\implies'
	symbol = '->'

	@staticmethod
	def operation(a, b):
		return not a or b


class Equal(BinaryLogicOperation):
	"""Равенство."""
	repr = '\\equiv'
	symbol = '=='

	@staticmethod
	def operation(a, b):
		return a == b


class Notequal(BinaryLogicOperation):
	"""Неравенство."""
	repr = '\\neq'
	symbol = '!='

	@staticmethod
	def operation(a, b):
		return a != b


def analyze(t):
	r = {}
	ranalyze(t, r)
	return r


def ranalyze(t, r):
	if type(t) in [FalseConst, TrueConst]:
		pass
	elif type(t) == Variable:
		if t.family not in r:
			r[t.family] = [t.order]
		elif t.order not in r[t.family]:
			r[t.family] += [t.order]
	elif type(t) in UnaryLogicOperation.__subclasses__() + BinaryLogicOperation.__subclasses__():
		for arg in t.args:
			ranalyze(arg, r)


def shift(t, k):
	import copy
	c = copy.deepcopy(t)
	rshift(c, k)
	return c


def rshift(t, k):
	if type(t) in [FalseConst, TrueConst]:
		pass
	elif type(t) == Variable:
		t.order += k if type(k) == int else k[t.family]
	elif type(t) in UnaryLogicOperation.__subclasses__() + BinaryLogicOperation.__subclasses__():
		for arg in t.args:
			rshift(arg, k)


def terms(t):
	r = []
	rterms(t, r)
	return r


def rterms(t, r):
	if type(t) in [FalseConst, TrueConst]:
		pass
	elif type(t) == Variable and t not in r:
		r.append(t)
	elif type(t) in UnaryLogicOperation.__subclasses__() + BinaryLogicOperation.__subclasses__():
		for arg in t.args:
			rterms(arg, r)


def varlist(t):
	z = analyze(t)
	return [key + str(order) for key in z for order in z[key]]

