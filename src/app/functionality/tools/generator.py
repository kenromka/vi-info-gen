from .tag import create_tag


class MainGenerator:
	def __init__(self, clses):
		self.clses = clses

	def generate(self):
		doc = create_tag()
		quiz = create_tag('quiz')
		doc.appendChild(quiz)

		for task_type in self.clses:
			task_generator = task_type()
			quiz.appendChild(task_generator.get_type_tag())
			for _ in range(100):
				task_generator = task_type()
				quiz.appendChild(task_generator.get_task_tag())
		return doc.toprettyxml()

