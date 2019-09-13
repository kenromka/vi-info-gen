from .common import *
from random import randint
from numpy.random import choice

def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


class Type0(Task10):
    """Системы счисления"""
    def __init__(self):
        super().__init__()

    def category(self):
        return "Системы счисления"

class SubtypeA(Type0):
    """Сравнение чисел"""
    def __init__(self):
        super().__init__()

        self.question = """
<p>
Среди приведенных ниже {n} чисел, записанных в различных системах счисления, найдите {minmax} и запишите его в ответе в десятичной системе счисления. В ответе запишите только число, основание системы счисления указывать не нужно.
</p>
<p>
<code>{numbers}</code>
</p>
        """
#============================================================================
        minmax_dict = {'max': 'максимальное','min': 'минимальное'}
        n_dict = {3: 'трех', 4: 'четырех', 5: 'пяти'}

        bases_lst = list(range(2, 10)) + list(range(11, 33))
        bases_weights = [4, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 4]+[1]*7+[2]+[1]*7+[2]
        bases_weights = list(map(lambda x: x/sum(bases_weights), bases_weights))

        n = randint(3, 5)
        minmax = choice(list(minmax_dict.keys()))
        
        tmp = randint(11, 99)
        bases = choice(bases_lst, size=n, replace=False, p=bases_weights)
        numbers = choice(list(range(tmp-randint(5, 10), tmp+randint(10, 15))), size=n, replace=False)

#============================================================================
        self._answer = eval(f"{minmax}({list(numbers)})")

        self._n = n_dict[n]
        self._minmax = minmax_dict[minmax]
        self._numbers = list(map(lambda x, y: (convert_base(x, to_base=y), y), numbers, bases))


    def question_text(self):
        return self.question.format(
            n = self._n,
            minmax = self._minmax,
            numbers = ", ".join(list(map(lambda x: f"{x[0]}<sub>{x[1]}</sub>", self._numbers)))
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Сравнение чисел"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()