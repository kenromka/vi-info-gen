from .tag import create_tag
from abc import abstractmethod
from hashlib import sha1
import hmac


class BaseTask:
	"""Базовый класс для задач"""
	@abstractmethod
	def question_text(self):
		"""Возвращает текст вопроса."""

	@abstractmethod
	def question_answer(self):
		"""Возвращает ответ на вопрос."""

	def get_type_tag(self):
		"""Возвращает категорию вопроса."""
		question = create_tag('question', None, {"type": "category"})
		category = create_tag('category')
		text = create_tag('text', self.category())
		category.appendChild(text)
		question.appendChild(category)
		return question

	def get_task_tag(self):
		"""Возвращает вопрос."""
		task = self.question_text()
		question = create_tag('question', None, {"type": self.question_type()})
		name = create_tag('name')
		text = create_tag('text', 'Задача №' + self.sha1(str(task)))
		name.appendChild(text)
		question.appendChild(name)
		question_text = create_tag('questiontext', None, {"format": "html"})
		text = create_tag('text', self.question_text(), cdata = self.cdata())
		question_text.appendChild(text)
		question.appendChild(question_text)
		answer = create_tag('answer', None, {"fraction": "100", "format": "moodle_auto_format"})
		text = create_tag('text', str(self.question_answer()))
		answer.appendChild(text)
		question.appendChild(answer)
		return question

	@staticmethod
	def question_type():
		"""Тип вопроса.

		Возможные значения: «numerical», «shortanswer» и другие. По умолчанию «shortanswer»."""
		return 'shortanswer'

	@staticmethod
	def cdata():
		return False

	@staticmethod
	def sha1(text):
		assert(type(text) == str)
		return hmac.new(bytearray(text, 'utf-8'), bytearray('text', 'utf-8'), sha1).hexdigest()

	@staticmethod
	def latex(element):
		return str(element).upper()

	@staticmethod
	def category():
		return 'ЕГЭ/'
	
	@staticmethod
	def level():
		return "ez"


class BaseTaskOge:
	"""Базовый класс для задач ОГЭ"""
	@abstractmethod
	def question_text(self):
		"""Возвращает текст вопроса."""

	@abstractmethod
	def question_answer(self):
		"""Возвращает ответ на вопрос."""

	def get_type_tag(self):
		"""Возвращает категорию вопроса."""
		question = create_tag('question', None, {"type": "category"})
		category = create_tag('category')
		text = create_tag('text', self.category())
		category.appendChild(text)
		question.appendChild(category)
		return question

	def get_task_tag(self):
		"""Возвращает вопрос."""
		task = self.question_text()
		question = create_tag('question', None, {"type": self.question_type()})
		name = create_tag('name')
		text = create_tag('text', 'Задача №' + self.sha1(str(task)))
		name.appendChild(text)
		question.appendChild(name)
		question_text = create_tag('questiontext', None, {"format": "html"})
		text = create_tag('text', self.question_text(), cdata = self.cdata())
		question_text.appendChild(text)
		question.appendChild(question_text)
		answer = create_tag('answer', None, {"fraction": "100", "format": "moodle_auto_format"})
		text = create_tag('text', str(self.question_answer()))
		answer.appendChild(text)
		question.appendChild(answer)
		return question

	@staticmethod
	def question_type():
		"""Тип вопроса.

		Возможные значения: «numerical», «shortanswer» и другие. По умолчанию «shortanswer»."""
		return 'shortanswer'

	@staticmethod
	def cdata():
		return False

	@staticmethod
	def sha1(text):
		assert(type(text) == str)
		return hmac.new(bytearray(text, 'utf-8'), bytearray('text', 'utf-8'), sha1).hexdigest()

	@staticmethod
	def latex(element):
		return str(element).upper()

	@staticmethod
	def category():
		return '$course$/OГЭ/'
	
	@staticmethod
	def level():
		return "ez"


