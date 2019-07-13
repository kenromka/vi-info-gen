from .common import *


class Type2(Task1):
	"""Решение неравенств в различных системах счисления."""
	def __init__(self):
		super().__init__()
		self.base, self.degree = self.linked()
		self.question = 'Определите количество целых решений неравенства {inequality}.'
		self.distance = randint(1, 1000)
		left = transform(self.number, self.base, based=True)
		right = transform(self.number + self.distance + 1, self.base ** self.degree, based=True)
		self.left_sign = randint(0, 1)
		self.right_sign = randint(0, 1)
		letter = 'xyz'
		signs = [' < ', ' <= ']
		self.inequality = self.latex(left + signs[self.left_sign] + choice(letter) + signs[self.right_sign] + right)

	def category(self):
		return "Решение неравенств в различных системах счисления"

class SubtypeA(Type2):
	"""Превод чисел из десятичной в произвольные системы счисления."""
	def __init__(self):
		super().__init__()

	def question_text(self):
		return self.question.format(inequality=self.inequality)

	def question_answer(self):
		return self.distance + self.left_sign + self.right_sign
	
	def level(self):
		return "hard"
	
	@property
	def max_qty(self):
		return 0
