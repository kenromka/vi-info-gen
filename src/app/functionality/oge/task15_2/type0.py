from .common import *
from random import randint, choices

class Type0(Task15_2):
    """Создание простых программ (ЯП)"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Создание простых программ ЯП"
    
    @property
    def get_type_num(self):
        return 1
	
    def level(self):
        return "hard"


class SubtypeA(Type0):
    """Количество чисел, удовлетворяющих условию"""
    def __init__(self):
        super().__init__()

        self.question = 'Напишите программу, которая в последовательности натуральных чисел '\
        'определяет количество чисел, {condition_1} {oper} {condition_2}. Программа получает '\
        'на вход количество чисел в последовательности, а затем сами числа.<br>'\
        'Количество чисел не превышает 1000. Введённые числа не превышают 30000.<br>'\
        'Программа должна вывести одно число: количество чисел, {condition_1} {oper} {condition_2}.'


#===========================================================================
        conditions = {
            'кратных {n}': 'x % {n} == 0',
            'не кратных {n}': 'x % {n} != 0',
            'начинающихся с {n}': 'str(x)[0] == "{n}"',
            'заканчивающихся на {n}': 'str(x)[-1] == "{n}"'
        }

        opers = {
            'и': 'and',
            'или': 'or'
        }

        del_ns = {
            'кратных {n}': list(range(2, 11))+[11, 15, 16, 18, 20, 25, 36, 50],
            'не кратных {n}': list(range(2, 11))+[11, 15, 16, 18, 20, 25, 36, 50],
            'начинающихся с {n}': list(range(1, 10)),
            'заканчивающихся на {n}': list(range(10))
        }

        check_lst = list(range(1, 30001))
#============================================================================
        condition_1, condition_2, n1, n2 = [None]*4
        while condition_1 == condition_2 and n1 == n2:
            condition_1, condition_2 = choices(list(conditions.keys()), k=2)
            n1 = choices(del_ns[condition_1])[0]
            oper = choices(list(opers.keys()))[0]

            n2 = choices(del_ns[condition_2])[0]
            if oper != 'или':
                f1 = lambda x: eval(conditions[condition_1].format(n=n1))
                f2 = lambda x: eval(conditions[condition_2].format(n=n2))
                if not any([f1(i) and f2(i) for i in check_lst]):
                    condition_1, condition_2, n1, n2 = [None]*4
                
            
        self._condition_1 = condition_1.format(n=n1)
        self._condition_2 = condition_2.format(n=n2)
        self._oper = oper

        self._generate = f"""
def generate():
    from random import shuffle, sample, randint
    
    n = sample(list(range(10, 1000)), k=95) + [0, 1000]
    shuffle(n)
    n = sample(list(range(1, 10)), k=3) + n
    
    a = [
            f'{{i}}\\n'+
            '\\n'.join([str(randint(1, 30000)) for _ in range(i)]) +
            '\\n'
        for i in n
    ]
    
    return a
        """
        self._solve = f"""
def solve(dataset):
    from functools import reduce
    
    dataset = list(map(int, dataset.split()))
    
    condition = lambda x: ({conditions[condition_1].format(n=n1)} {opers[oper]} {conditions[condition_2].format(n=n2)})
    
    if len(dataset) == 1:
        return '0'
    else:
        return str(reduce(
            lambda cnt, x: cnt+1 if condition(x) else cnt,
            dataset[1:]
        ) - (dataset[1])+(1 if condition(dataset[1]) else 0))
        """
        self._check = f"""
def check(reply, clue):
    if reply.strip() != clue.strip():
        if clue.strip() == '0':
            return reply.strip() == clue.strip(), 'А что если на вход программа примет о-о-очень мало чисел?'
    return reply.strip() == clue.strip()
        """
        

    def question_text(self):
        return self.question.format(
            condition_1=self._condition_1,
            condition_2=self._condition_2,
            oper=self._oper
        )

    def question_answer(self):
        answer = self._solve.replace('\n', '<br>')
        return f"<code>{answer}</code>"

    def category(self):
        return "Количество чисел, удовлетворяющих условию"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_code()
