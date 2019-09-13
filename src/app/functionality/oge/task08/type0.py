from .common import *
from random import randint, random, shuffle
from math import ceil


class Type0(Task8):
    """Принципы поиска информации в сети Интернет"""
    def __init__(self):
        super().__init__()

    def category(self):
        return "Принципы поиска информации в сети Интернет"
    
    @staticmethod
    def level():
        return 'mid'

class SubtypeA(Type0):
    """Базовые поисковые запросы"""
    def __init__(self):
        super().__init__()

        self.question = """
<p>В языке запросов поискового сервера для обозначения логической операции «ИЛИ» используется символ  «|», а для логической операции «И» – символ «&». 
<br>
В таблице приведены запросы и количество найденных по ним страниц некоторого сегмента сети Интернет. </p>

<table border="1">
	<thead>
		<tr>
			<th scope="col">Запрос</th>
			<th scope="col">Найдено страниц (в тыс.)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center;"><i>{requests[0]}</i></td>
			<td style="text-align: center;">{qty[0]}</td>
		</tr>
		<tr>
			<td style="text-align: center;"><i>{requests[1]}</i></td>
			<td style="text-align: center;">{qty[1]}</td>
		</tr>
		<tr>
			<td style="text-align: center;"><i>{requests[2]}</i></td>
			<td style="text-align: center;">{qty[2]}</td>
		</tr>
	</tbody>
</table>

<p>Какое количество страниц (в тысячах) будет найдено по запросу <i>{requests[3]}</i> ?   
<br>
Считается, что все запросы выполнялись практически одновременно, так что набор страниц, содержащих все искомые слова, не изменялся за время выполнения запросов.</p>
        """
#============================================================================
        import pandas as pd
        words = pd.read_csv('./app/functionality/xtra/russian_words.csv', header=None, usecols=[1])

        a_word, b_word = list(words.sample(n=2, replace=False).iloc[:, 0])

        a = set(map(lambda x: ceil(random()*100)/100, range(randint(9, 60))))
        b = set(map(lambda x: x + ceil(random()*100)/100, a))

#============================================================================
        disj = a | b
        conj = a & b

        requests = {
            a_word: len(a)*10,
            b_word: len(b)*10,
            f'{a_word} | {b_word}': len(disj)*10,
            f'{a_word} & {b_word}': len(conj)*10
        }

        self._requests = list(requests.keys())
        shuffle(self._requests)

        self._qty = list(map(lambda x: requests[x], self._requests))

        self._answer = self._qty[3]

    def question_text(self):
        return self.question.format(
            requests = self._requests,
            qty = self._qty
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Базовые поисковые запросы"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()