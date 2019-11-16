from .common import *
from random import randint
from ...tools.choices import choices

class Infix:
    "Own operators hack:)"
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

class Type2(Task3):
    """Истинность высказывания"""
    def __init__(self):
        super().__init__()

        
    def category(self):
        return "Истинность высказывания - число с конкретным количеством разрядов"
    
    @property
    def get_type_num(self):
        return 3
	
    def level(self):
        return "mid"
    


class SubtypeA(Type2):
    """Число с конкретным количеством разрядов - истинно"""
    question = """
    Напишите {minmax} {capacity} число <i>{var}</i>, для которого истинно высказывание: 
<br>
<code>
<b>{oper1}</b> ({costyl1}<i>{var}</i> {expr1}) <b> {oper} </b> <b>{oper2}</b> ({costyl2}<i>{var}</i> {expr2}) 
</code>
    """
    def __init__(self):
        # super().__init__()
        ends_with = Infix(lambda s, n: (n < 10) and str(s)[-1] == str(n))
        contains = Infix(lambda s, n: (n < 10) and str(n) in str(s))
        no_contains = Infix(lambda s, n: not ((n < 10) and str(n) in str(s)))
        no_similar = Infix(lambda s, dummy: len(str(s)) == len(set(str(s))))
        num_sum_less = Infix(lambda s, n: sum(list(map(int, str(s)))) < n)
        num_sum_more = Infix(lambda s, n: sum(list(map(int, str(s)))) > n)
        n_cifer_1 = Infix(lambda s, n: int(str(s)[n-1]) % 2 == 1)
        n_cifer_0 = Infix(lambda s, n: int(str(s)[n-1]) % 2 == 0)


#===========================================================================
        import numpy as np
        minmax = {'min': 'наименьшее', 'max': 'наибольшее'}
        capacity = {2: 'двухзначное', 3: 'трехзначное', 4: ' четырехзначное', 5: 'пятизачное'}
        slice_by_cap = {
            2: list(range(10, 100)),
            3: list(range(100, 1000)),
            4: list(range(1000, 10000)),
            5: list(range(10000, 100000))
        }
        namevar = 'abcdnmtpxyz'
        # НЕ ОШИБКА!!! инвертировано специально для маски
        oper_i = {'{x}': 'НЕ', 'np.logical_not({x})': ''}
        oper = {'&': 'И', '|': 'ИЛИ'}
        expr = {
            'unary':
            {
                '%2 == 0': 'четное', '%2 != 0': 'нечетное',
                '|no_similar| 0': 'не содержит одинаковых цифр'
            },
            'bin':
            {
                '%{n} == 0': 'кратно {n}', '%{n} != 0': 'не делится на {n} нацело',
                '|ends_with| {n}': 'оканчивается на {n}', '|contains| {n}': 'содержит {n}', '|no_contains| {n}': 'не содержит {n}',
                '|num_sum_less| {n}': 'меньше {n}', '|num_sum_more| {n}': 'больше {n}', 
                '|n_cifer_1| {n}': '{n}-я цифра нечетная', '|n_cifer_0| {n}': '{n}-я цифра четная'
            }
        }
        costyl = {
            'num_sum': 'сумма цифр числа ',
            'n_cifer': 'у числа '
        }
#============================================================================
        finish_flg = False
        while not finish_flg:
            # костыль на текст перед переменной
            self._costyl1 = ''
            self._costyl2 = ''

            cap = choices(list(capacity.keys()))[0]
            domain = np.array(slice_by_cap[cap])
            self._capacity = capacity[cap]
            bounds = {
                '%': (2, 9),     #если деление
                '|': (0, 9),
                '!': (1, 10000-1),
                'num_sum': (6, 15),
                'n_cifer': (1, cap)
            }
            
            finish_flg = True
            self._var = choices(namevar)[0]
            expr1 = choices(list(expr.keys()), weights=[.2, .8])[0]
            expr2 = choices(list(expr.keys()), weights=[.3, .7])[0] if expr1 == 'bin' else 'bin'

            expr1_oper = choices(list(expr[expr1].keys()))[0]
            if expr1 == 'bin':
                if expr1_oper[0] in ('%', '|'):
                    if 'num_sum' in expr1_oper:
                        bound1 = randint(*bounds['num_sum'])
                        self._costyl1 = costyl['num_sum']
                    elif 'n_cifer' in expr1_oper:
                        bound1 = randint(*bounds['n_cifer'])
                        self._costyl1 = costyl['n_cifer']
                    else:
                        bound1 = randint(*bounds[expr1_oper[0]])
                else:
                    bound1 = randint(*bounds['!'])
                oper_1 = choices(list(oper_i.keys()), weights=[.3, .7])[0]
                mask = eval(oper_1.format(x=('(domain '+expr1_oper.format(n=bound1)+')'))).astype(bool),
                
            else:
                bound1 = None
                oper_1 = choices(list(oper_i.keys()), weights=[.3, .7])[0]
                mask = eval(oper_1.format(x=('(domain '+expr1_oper+')'))).astype(bool),
            # print(expr1_oper, mask)
            domain1 = np.array(domain)[~np.array(mask)[0]]
            if len(domain1) < 7:
                domain1 = np.array(domain)[~np.logical_not(mask[0])]
                oper_1 = (set(oper_i.keys()) - set([oper_1])).pop()

            expr2_oper = choices(list(expr[expr2].keys()))[0]
            if expr2 == 'bin':
                if expr2_oper[0] in ('%', '|'):
                    if 'num_sum' in expr2_oper:
                        bound2 = randint(*bounds['num_sum'])
                        self._costyl2 = costyl['num_sum']
                    elif 'n_cifer' in expr2_oper:
                        bound2 = randint(*bounds['n_cifer'])
                        self._costyl2 = costyl['n_cifer']
                    else:
                        bound2 = randint(*bounds[expr2_oper[0]])
                else:
                    bound2 = randint(*bounds['!'])
                oper_2 = choices(list(oper_i.keys()), weights=[.3, .7])[0]
                mask2 = eval(oper_2.format(x=('(domain '+expr2_oper.format(n=bound2)+')'))).astype(bool),
                
            else:
                bound2 = None
                oper_2 = choices(list(oper_i.keys()), weights=[.3, .7])[0]
                mask2 = eval(oper_2.format(x=('(domain '+expr2_oper+')'))).astype(bool),
            # print(expr2_oper, mask2)
            domain2 = np.array(domain)[~np.array(mask2)[0]]
            if len(domain2) < 7:
                domain2 = np.array(domain)[~np.logical_not(mask2[0])]
                oper_2 = (set(oper_i.keys()) - set([oper_2])).pop()
            
            main_oper = '&'
            domain3 = eval(f'(set(domain1) {main_oper} set(domain2)) & set(slice_by_cap[{cap}])')
            if len(domain3) < 3:
                main_oper = (set(oper.keys()) - set([main_oper])).pop()
                domain3 = eval(f'(set(domain1) {main_oper} set(domain2)) & set(slice_by_cap[{cap}])')
            
            self._oper1 = oper_i[oper_1]
            self._oper2 = oper_i[oper_2]
            self._oper = oper[main_oper]
            self._expr1 = expr[expr1][expr1_oper].format(n=str(bound1)) if expr1=='bin' else expr[expr1][expr1_oper]
            self._expr2 = expr[expr2][expr2_oper].format(n=str(bound2)) if expr2=='bin' else expr[expr2][expr2_oper]

            change = {
                    'четная': 'нечетная',
                    'нечетная': 'четная'
            }
            # if 'НЕ' not in [self._oper1, self._oper2]:
            all_exprs = self._expr1 + self._expr2
            # elif 'НЕ' == self._oper1:
            #     all_exprs = self._expr2
            #     for c in change.keys():
            #         if c in self._expr1:
            #             all_exprs += self._expr1.replace(c, change[c])
            #             break
            # else:
            #     all_exprs = self._expr1
            #     for c in change.keys():
            #         if c in self._expr2:
            #             all_exprs += self._expr2.replace(c, change[c])
            #             break

            less_cnt = all_exprs.count('-я') + all_exprs.count('меньше') + all_exprs.count('больше')
            # print(all_exprs)
            # print(len(domain1), len(domain2), len(domain3))
            # print("_"*10)
            if (len(domain3) < 15):
                finish_flg = False
                continue
            if less_cnt >= 1:
                chosen = choices(list(minmax.keys()))[0]
                self._minmax = minmax[chosen]
                self._answer = eval(chosen+f'({domain3})')
            else:
                finish_flg = False
                continue

    def question_text(self):
        return self.question.format(
            minmax=self._minmax,
            costyl1=self._costyl1,
            costyl2=self._costyl2,
            capacity=self._capacity,
            var=self._var,
            oper=self._oper,
            oper1=self._oper1,
            oper2=self._oper2,
            expr1=self._expr1,
            expr2=self._expr2
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Число с конкретным количеством разрядов - истинно"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()


#class SubtypeB
@property
def get_subtype_num_B(self):
    return 2

def category_B(self):
    return 'Число с конкретным количеством разрядов - ложно'

change_dict = {
    # '>НЕ<': '><',
    'И': ' ИЛИ ',
    'ИЛИ': ' И ',
    '<=': ' > ',
    '>=': ' < ',
    '<': ' >= ',
    '>': ' <= ',
    'кратно': ' не делится на ',
    'не': ' ',
    'оканчивается на': ' не оканчивается на ',
    'одинаковых цифр)': ' одинаковые цифры) ',
    'содержит': ' не содержит ',
    'меньше': ' не больше ',
    'больше': ' не меньше ',
    'четное)': ' нечетное) ',
    'нечетное)': ' четное) '
}

import re 

def multiple_replace(dict, text): 
    regex = re.compile(" (%s) " % "|".join(map(re.escape, dict.keys())))
    return regex.sub(lambda mo: dict[mo.string[mo.start()+1:mo.end()-1]], text) 

def question_text_B(self):
    text = self.question.format(
            minmax=self._minmax,
            costyl1=self._costyl1,
            costyl2=self._costyl2,
            var=self._var,
            capacity=self._capacity,
            oper=self._oper,
            oper1=self._oper1,
            oper2=self._oper2,
            expr1=self._expr1,
            expr2=self._expr2
    )

    result = multiple_replace(change_dict, text)
    return result

B_dict = dict(SubtypeA.__dict__)
B_dict['get_subtype_num'] = get_subtype_num_B
B_dict['category'] = category_B
B_dict['question_text'] = question_text_B
SubtypeB = type('SubtypeB', (Type2,), B_dict)
SubtypeB.question = SubtypeB.question.replace('истинно', 'ложно')