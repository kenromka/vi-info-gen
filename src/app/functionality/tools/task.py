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

	@property
	def get_task_num(self):
		return 0
	
	@property
	def get_type_num(self):
		return 0
	
	@property
	def get_subtype_num(self):
		return 0
	
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

	def jsonify_basic_text(self):
		return {
				"text": self.question_text(),
				"name":"string",
				"video": None,
				"animation": None,
				"options": None,
				"source": {
					"pattern": self.question_answer(),
					"use_re": False,
					"match_substring": False,
					"case_sensitive": False,
					"code": "# def check(reply):\n#     \"\"\"Evaluate the learner's reply.\n#\n#     It should return 1 or True for the correct reply and 0 or False\n#     for the incorrect one.\n#\n#     A partial solution may be scored using a float number from the\n#     interval (0, 1). In such a case the learner total score for the\n#     problem will be 'step cost' * 'score'.\n#\n#     :param reply: a string that is the learner's reply to the problem\n#     :return: a score number (int or float) in range [0, 1]\n#\n#     \"\"\"\n#     return reply == \"Hello\"\n\n# def solve():\n#     \"\"\"Return a correct reply. This function is *optional*.\n#\n#     It is used to test the correctness of the 'check' function.\n#\n#     :return: a string that is a correct reply to the problem\n#\n#     \"\"\"\n#     return \"Hello\"",
					"is_text_disabled": False,
					"is_file_disabled": True
				}
			}

	@abstractmethod
	def stepik_jsonify(self):
		pass


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
	
	@property
	def get_task_num(self):
		return 0
	
	@property
	def get_type_num(self):
		return 0
	
	@property
	def get_subtype_num(self):
		return 0

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

	def jsonify_basic_text(self):
		return {
				"text": self.question_text(),
				"name":"string",
				"video": None,
				"animation": None,
				"options": None,
				"source": {
					"pattern": self.question_answer(),
					"use_re": False,
					"match_substring": False,
					"case_sensitive": False,
					"code": "# def check(reply):\n#     \"\"\"Evaluate the learner's reply.\n#\n#     It should return 1 or True for the correct reply and 0 or False\n#     for the incorrect one.\n#\n#     A partial solution may be scored using a float number from the\n#     interval (0, 1). In such a case the learner total score for the\n#     problem will be 'step cost' * 'score'.\n#\n#     :param reply: a string that is the learner's reply to the problem\n#     :return: a score number (int or float) in range [0, 1]\n#\n#     \"\"\"\n#     return reply == \"Hello\"\n\n# def solve():\n#     \"\"\"Return a correct reply. This function is *optional*.\n#\n#     It is used to test the correctness of the 'check' function.\n#\n#     :return: a string that is a correct reply to the problem\n#\n#     \"\"\"\n#     return \"Hello\"",
					"is_text_disabled": False,
					"is_file_disabled": True
				}
			}

	@abstractmethod
	def stepik_jsonify(self):
		pass
