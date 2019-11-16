from .common import *
from random import randint
from ...tools.choices import choices

class Type3(Task3):
    """Истинность высказывания"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Закон де Моргана"
    
    @property
    def get_type_num(self):
        return 4
	
    def level(self):
        return "hard"

from . import type0
from . import type1
from . import type2


#class SubtypeA
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

def question_text_A(self):
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
    result = result.replace('<code>', '<code><b>НЕ</b>(')
    result = result.replace('</code>', ')</code>')
    return result


chosen_subtype = choices(
    [
        type0.SubtypeA,
        type0.SubtypeB,
        type1.SubtypeA,
        type1.SubtypeB,
        type2.SubtypeA,
        type2.SubtypeB
    ]
)[0]

A_dict = dict(type0.SubtypeA.__dict__)
A_dict['__module__'] = 'app.functionality.oge.task03.type3'
@property
def get_subtype_num_A(self):
    return 1

def category_A(self):
    return 'Закон де Моргана - просто число - истинно' 
A_dict['get_subtype_num'] = get_subtype_num_A
A_dict['category'] = category_A
A_dict['question_text'] = question_text_A
SubtypeA = type('SubtypeA', (Type3,), A_dict)

A_dict = dict(type0.SubtypeB.__dict__)
A_dict['__module__'] = 'app.functionality.oge.task03.type3'
@property
def get_subtype_num_B(self):
    return 2

def category_B(self):
    return 'Закон де Моргана - просто число - ложно'
A_dict['get_subtype_num'] = get_subtype_num_B
A_dict['category'] = category_B
A_dict['question_text'] = question_text_A
SubtypeB = type('SubtypeB', (Type3,), A_dict)

A_dict = dict(type1.SubtypeA.__dict__)
A_dict['__module__'] = 'app.functionality.oge.task03.type3'
@property
def get_subtype_num_C(self):
    return 3

def category_C(self):
    return 'Закон де Моргана - minmax число - истинно'
A_dict['get_subtype_num'] = get_subtype_num_C
A_dict['category'] = category_C
A_dict['question_text'] = question_text_A
SubtypeC = type('SubtypeC', (Type3,), A_dict)

A_dict = dict(type1.SubtypeB.__dict__)
A_dict['__module__'] = 'app.functionality.oge.task03.type3'
@property
def get_subtype_num_D(self):
    return 4

def category_D(self):
    return 'Закон де Моргана - minmax число - истинно'
A_dict['get_subtype_num'] = get_subtype_num_D
A_dict['category'] = category_D
A_dict['question_text'] = question_text_A
SubtypeD = type('SubtypeD', (Type3,), A_dict)

A_dict = dict(type2.SubtypeA.__dict__)
A_dict['__module__'] = 'app.functionality.oge.task03.type3'
@property
def get_subtype_num_E(self):
    return 5

def category_E(self):
    return 'Закон де Моргана - число с конкретным количеством разрядов - истинно'
A_dict['get_subtype_num'] = get_subtype_num_E
A_dict['category'] = category_E
A_dict['question_text'] = question_text_A
SubtypeE = type('SubtypeE', (Type3,), A_dict)

A_dict = dict(type2.SubtypeB.__dict__)
A_dict['__module__'] = 'app.functionality.oge.task03.type3'
@property
def get_subtype_num_F(self):
    return 6

def category_F(self):
    return 'Закон де Моргана - число с конкретным количеством разрядов - ложно'
A_dict['get_subtype_num'] = get_subtype_num_F
A_dict['category'] = category_F
A_dict['question_text'] = question_text_A
SubtypeF = type('SubtypeF', (Type3,), A_dict)

