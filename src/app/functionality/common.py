import pydf
import time
from hashlib import md5

from .tools.choices import choices

import pickle
import re
#eee

def all_subclasses(cls):
	return cls.__subclasses__() + [g for s in cls.__subclasses__() for g in all_subclasses(s)]

def convertHtmlToPdf(sourceHtml, outputFilename):
	pdf = pydf.generate_pdf(sourceHtml)
	with open(outputFilename, "wb") as file:
		file.write(pdf)




def find_number(dic, item):
    for task, task_i in dic.items():
        for _, typo_i in task_i[0].items():
            for _, val in typo_i.items():
                if item == val[0]:
                    return task

import threading
from random import randint


class ExportingThread(threading.Thread):

	def __init__(self, outputFilename, choice_lst, dic, typo, headers, answer, proglangs):
		self.progress = 1
		self.outputFilename = outputFilename
		self.choice_lst = choice_lst
		self.dic = dic
		self.typo = typo
		self.headers = headers
		self.answer = answer
		self.proglangs = proglangs
		super().__init__()

	def run(self):
		if "pdf" in self.outputFilename:	
			create_pdf(self)
		elif "csv" in self.outputFilename:
			create_csv(self)
		elif "json" in self.outputFilename:
			create_step(self)

def create_step(thread):

	import json 
	
	tid_lst = []
	task_html_lst = []
	
	cnt = 0
	thread.progress = 0
	for subtype in thread.choice_lst:
		task = subtype[0]
		task_hashes = []
		for _ in range(subtype[1]):
			real_task = task()
			if real_task.max_qty <= 100:
				if real_task.max_qty <= len(task_hashes):
					break
			else:
				if real_task.max_qty*0.8 <= len(task_hashes):
					break
			while (md5(real_task.question_text().encode()).hexdigest() in task_hashes):
				real_task = task()
			task_hashes.append(md5(real_task.question_text().encode()).hexdigest())

			cnt += 1

			text = json.dumps(real_task.stepik_jsonify())
			#выбор языков программирования
			if thread.proglangs.get(task.__bases__[0].__bases__[0]().category(), None):
				for lang in set(["python", "qbasic", "cpplus", "pascal", "algori"])-set(thread.proglangs[task.__bases__[0].__bases__[0]().category()]):
					th_search = re.search(f"<th name='{lang}'[^~]*?</th>", text) or [""]
					td_search = re.search(f"<td name='{lang}'[^~]*?</td>", text) or [""]
					text = text.replace(th_search[0], "")
					text = text.replace(td_search[0], "")

			tid_lst.append(real_task.sha1(real_task.question_text()))
			task_html_lst.append(json.loads(text))

		result = dict(zip(tid_lst, task_html_lst))
		with open(thread.outputFilename, 'w', encoding='utf-8') as f:
			json.dump(result, f, ensure_ascii=False, indent=4)

		while thread.progress < 100:
				thread.progress += 1

def create_csv(thread):
	tid_lst = []
	task_num_lst = []
	type_num_lst = []
	subtype_num_lst = []
	task_html_lst = []
	answer_lst = []

	cnt = 0
	thread.progress = 0
	for subtype in thread.choice_lst:
		task = subtype[0]
		task_hashes = []
		for _ in range(subtype[1]):
			real_task = task()
			if real_task.max_qty <= 100:
				if real_task.max_qty <= len(task_hashes):
					break
			else:
				if real_task.max_qty*0.8 <= len(task_hashes):
					break
			while (md5(real_task.question_text().encode()).hexdigest() in task_hashes):
				real_task = task()
			task_hashes.append(md5(real_task.question_text().encode()).hexdigest())

			cnt += 1

			text = real_task.question_text()
			#выбор языков программирования
			if thread.proglangs.get(task.__bases__[0].__bases__[0]().category(), None):
				for lang in set(["python", "qbasic", "cpplus", "pascal", "algori"])-set(thread.proglangs[task.__bases__[0].__bases__[0]().category()]):
					th_search = re.search(f"<th name='{lang}'[^~]*?</th>", text) or [""]
					td_search = re.search(f"<td name='{lang}'[^~]*?</td>", text) or [""]
					text = text.replace(th_search[0], "")
					text = text.replace(td_search[0], "")

			tid_lst.append(real_task.sha1(real_task.question_text()))
			task_num_lst.append(real_task.get_task_num)
			type_num_lst.append(real_task.get_type_num)
			subtype_num_lst.append(real_task.get_subtype_num)
			task_html_lst.append(text)
			answer_lst.append(real_task.question_answer())
		
		from pandas import DataFrame

		DataFrame.from_dict(
			{
				'tid': tid_lst,
				'task': task_num_lst,
				'type': type_num_lst,
				'subtype': subtype_num_lst,
				'question': task_html_lst,
				'answer': answer_lst
			}
		).to_csv(thread.outputFilename, index=False)

		while thread.progress < 100:
				thread.progress += 1

def create_pdf(thread):
			html = """
				<!DOCTYPE html>
				<html>
				<head>
					<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
					<style type = "text/css">
						p { font-family: Calibri; font-size: 14pt }
						h1 { font-family: Calibri; font-style: bold }
						h2 { font-family: Calibri; font-style: bold }
						h3 { font-family: Calibri; font-style: bold }
						pre { font-family: Calibri; font-size: 14pt }
						table { font-family: Calibri; font-size: 14pt; table-layout: fixed; page-break-inside: avoid;}
						tr {vertical-align: top;}
						.texttask {page-break-inside: avoid;}
						.answers {page-break-before: always;}
					</style>
						<H1 align="center" style="font-size:6">""" + thread.typo + """ по информатике </H1>
				</head>

				<body>
				<hr>
						"""
			cnt = 0
			thread.progress = 0
			max_cnt = sum([i[1] for i in thread.choice_lst])
			ans_buffer = "<div class='answers'><h2>Ответы</h2><div>"
			for subtype in thread.choice_lst:
				task = subtype[0]
				task_hashes = []
				if thread.headers:
					if subtype == thread.choice_lst[0]:
						html += f"\n<h2 align='center' style='font-size:5'> {find_number(thread.dic, task().category())} {task().category()} </h2>"
					else:
						html += f"\n<h2 style='page-break-before: always;' align='center' style='font-size:5'> {find_number(thread.dic, task().category())} {task().category()} </h2>"
				for i in range(subtype[1]):
					real_task = task()
					if real_task.max_qty <= 100:
						if real_task.max_qty <= len(task_hashes):
							break
					else:
						if real_task.max_qty*0.8 <= len(task_hashes):
							break
					while (md5(real_task.question_text().encode()).hexdigest() in task_hashes):
						real_task = task()
					task_hashes.append(md5(real_task.question_text().encode()).hexdigest())
					cnt += 1
					html += f"<div class='texttask'>\n<h3>Задача № {cnt}</h3>\n"

					text = real_task.question_text()
					#выбор языков программирования
					if thread.proglangs.get(task.__bases__[0].__bases__[0]().category(), None):
						for lang in set(["python", "qbasic", "cpplus", "pascal", "algori"])-set(thread.proglangs[task.__bases__[0].__bases__[0]().category()]):
							th_search = re.search(f"<th name='{lang}'[^~]*?</th>", text) or [""]
							td_search = re.search(f"<td name='{lang}'[^~]*?</td>", text) or [""]
							text = text.replace(th_search[0], "")
							text = text.replace(td_search[0], "")

					html += f"\n<p>{text}</p>\n"
					if thread.answer == "ans_yes":
						html += f"\n<p style='font-style: italic'>Ответ:\t{str(real_task.question_answer())}</p>\n<hr size=1 color=gray>\n"
					elif thread.answer == "ans_end":
						ans_buffer += f"\n<p>{cnt}) \t{str(real_task.question_answer())}</p>\n"
					html += "</div>\n"
					
					#каждая задача на отдельной странице
					if "one-pager" in real_task.question_text():
						html += "<p style='page-break-after: always;'></p>"

				html += "<hr size=3>"
				thread.progress = int(cnt/max_cnt*50)+randint(1, 10) if max_cnt != 0 else 99
			if thread.answer == "ans_end":
				html += f"{ans_buffer}\n</div></div>"
			html += """	</body>
				</html>
				"""
			convertHtmlToPdf(html, thread.outputFilename)
			while thread.progress < 100:
				thread.progress += 1