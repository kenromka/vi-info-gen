from .common import *
from random import randint, randrange, shuffle
from ...tools.choices import choices
from collections import OrderedDict

class Type0(Task2):
    """Декодирование кодовой последовательности"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Декодирование кодовой последовательности"
    
    @property
    def get_type_num(self):
        return 1
	
    def level(self):
        return "ez"


class SubtypeA(Type0):
    """Декодирование кодовой последовательности - Неравномерное двоичное кодирование (Фано)"""
    def __init__(self):
        super().__init__()

        self.question = """
        От разведчика было получено сообщение: <br><br>{msg}<br><br> В этом сообщении зашифрован пароль – последовательность русских букв. В пароле использовались только буквы {letters}; каждая буква кодировалась двоичным словом по такой таблице: 

<table align="center" border="1">
	<thead>
		<tr>
			{letters_table}
		</tr>
	</thead>
	<tbody>
		<tr>
            {code_table}
		</tr>
	</tbody>
</table>


Расшифруйте сообщение. <br>Запишите в ответе пароль.
        """


#===========================================================================
        import pandas as pd
        words = pd.read_csv('./app/functionality/xtra/russian_words.csv', header=None, usecols=[1])
#============================================================================
        self._answer = words.sample(1).iloc[0, 0].upper()

        self._letters = sorted(set(self._answer))
        self._letters_table = (
                '<th scope="col">'
                +
                self._letters[0]
                +
                '</th>\n<th scope="col">'
                +
                '</th>\n<th scope="col">'.join(self._letters[1:])
                +
                '</th>'
        )

        f = ['0', '1']
        shuffle(f)

        codes = dict(zip(self._letters, [""]*len(self._letters)))
        probs = OrderedDict(zip(self._letters, list(map(lambda x: self._letters.count(x), self._letters))))
        keys = list(probs.keys())
        shuffle(keys)
        probs = OrderedDict(sorted(zip(keys, probs.values()), key=lambda kv: kv[1], reverse=True))
        while len(probs) >= 2:
            key1, val1 = probs.popitem()
            key2, val2 = probs.popitem()
            for l in key1:
                codes[l] += f[0]
            for l in key2:
                codes[l] += f[1]
            probs[key1+key2] = val1 + val2
            keys = list(probs.keys())
            shuffle(keys)
            probs = OrderedDict(sorted(zip(keys, probs.values()), key=lambda kv: kv[1], reverse=True))
        
        for k, v in codes.items():
            codes[k] = "".join(reversed(v))


        self._code_table = (
                '<td>'
                +
                codes[self._letters[0]]
                +
                '</td>\n<td>'
                +
                '</td>\n<td>'.join([codes[x] for x in self._letters[1:]])
                +
                '</td>'
        )

        self._msg = "".join([codes[a] for a in self._answer])


    def question_text(self):
        return self.question.format(
            msg=self._msg,
            letters=', '.join(self._letters),
            letters_table=self._letters_table,
            code_table=self._code_table
        )

    def question_answer(self):
        return self._answer

    def category(self):
        return "Неравномерное двоичное кодирование"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
