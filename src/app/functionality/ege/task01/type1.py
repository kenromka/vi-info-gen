from .common import *
from collections import Counter


class Type1(Task1):
	"""Определение показателей, связанных с цифрами чисел в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.base, self.degree = self.linked()

	def category(self):
		return "Определение показателей, связанных с цифрами чисел в разных сc"

	def question_text(self):
		return self.question.format(number=self.based(self.number, choice([self.base ** self.degree] * 9 + [10])), notation=self.notation(self.base))


class SubtypeA(Type1):
	"""Количество повторений некоторой цифры числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите сколько цифр {digit} содержит число {number} в {notation}."
		self.digit = choice(self.digits[:self.base])

	def category(self):
		return "Количество повторений некоторой цифры"

	def question_text(self):
		return self.question.format(digit=self.digit, number=self.based(self.number, choice([self.base ** self.degree] * 9 + [10])), notation=self.notation(self.base))

	def question_answer(self):
		return transform(self.number, self.base, self.digits).count(self.digit)

	@property
	def max_qty(self):
		return 0


class SubtypeB(Type1):
	"""Количество значащих цифр числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите сколько значащих цифр содержит число {number} в {notation}."

	def category(self):
		return "Количество значащих цифр"

	def question_answer(self):
		return len(transform(self.number, self.base, self.digits))
	
	@property
	def max_qty(self):
		return 0


class SubtypeC(Type1):
	"""Количество различных цифр числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите сколько различных цифр содержит число {number} в {notation}."

	def category(self):
		return "Количество различных цифр"

	def question_answer(self):
		return len(set(transform(self.number, self.base, self.digits)))
	
	@property
	def max_qty(self):
		return 0


class SubtypeD(Type1):
	"""Самая большая цифра числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите самую большую цифру числа {number} в {notation}."

	def category(self):
		return "Самая большая цифра"

	def question_answer(self):
		return max(transform(self.number, self.base, self.digits))
	
	@property
	def max_qty(self):
		return 0


class SubtypeE(Type1):
	"""Самая маленькая цифра числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите самую маленькую цифру числа {number} в {notation}."

	def category(self):
		return "Самая маленькая цифра"

	def question_answer(self):
		return min(transform(self.number, self.base, self.digits))
	
	@property
	def max_qty(self):
		return 0


class SubtypeF(Type1):
	"""Наибольшая из самых часто встречающихся цифр числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите самую часто встречающуюся цифру числа {number} в {notation}. Если чаще других встречаются несколько цифр, укажите наибольшую из них."

	def category(self):
		return "Самая часто встречающаяся (наибольшая)"

	def question_answer(self):
		return max([(element[1], element[0]) for element in Counter(transform(self.number, self.base, self.digits)).items()])[1]
	
	@property
	def max_qty(self):
		return 0


class SubtypeG(Type1):
	"""Наименьшая из самых часто встречающихся цифр числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите самую часто встречающуюся цифру числа {number} в {notation}. Если чаще других встречаются несколько цифр, укажите наименьшую из них."

	def category(self):
		return "Самая часто встречающаяся (наименьшая)"

	def question_answer(self):
		return min([(-element[1], element[0]) for element in Counter(transform(self.number, self.base, self.digits)).items()])[1]
	
	@property
	def max_qty(self):
		return 0


class SubtypeH(Type1):
	"""Наибольшая из самых редко встречающихся цифр числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите самую редко встречающуюся цифру числа {number} в {notation}. Если реже других встречаются несколько цифр, укажите наибольшую из них."

	def category(self):
		return "Самая редко встречающаяся (наибольшая)"

	def question_answer(self):
		return max([(-element[1], element[0]) for element in Counter(transform(self.number, self.base, self.digits)).items()])[1]
	
	@property
	def max_qty(self):
		return 0


class SubtypeI(Type1):
	"""Наименьшая из самых редко встречающихся цифр числа в разных системах счисления."""
	def __init__(self):
		super().__init__()
		self.question = "Определите самую редко встречающуюся цифру числа {number} в {notation}. Если реже других встречаются несколько цифр, укажите наименьшую из них."

	def category(self):
		return "Самая редко встречающаяся (наименьшая)"

	def question_answer(self):
		return min([(element[1], element[0]) for element in Counter(transform(self.number, self.base, self.digits)).items()])[1]
	
	@property
	def max_qty(self):
		return 0

