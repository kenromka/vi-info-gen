from .common import *
from random import randint
from ...tools.choices import choices

class Type4(Task3):
    """Истинность высказывания - три высказывания"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Истинность высказывания - три высказывания"
    
    @property
    def get_type_num(self):
        return 4
	
    def level(self):
        return "hard"


class SubtypeA(Type4):
    """Истинность высказывания - три высказывания - Истинно"""
    question = """
    Напишите {minmax} {capacity} число <i>{var}</i>, для которого истинно высказывание: 
<br>
<code>
<b>{oper1}</b> ({costyl1}<i>{var}</i> {expr1}) <b> {oper} </b> <b>{oper2}</b> ({costyl2}<i>{var}</i> {expr2}) {operr2} </b> <b>{oper3}</b> ({costyl3}<i>{var}</i> {expr3}) 
</code>
    """
    _minmax, _costyl1, _costyl2, _costyl3, _capacity = [""]*5

    def __init__(self):
        # super().__init__()


#===========================================================================
        import numpy as np
        namevar = 'abcdnmtpxyz'
        domain = np.array(list(range(1, 10000)))
        # НЕ ОШИБКА!!! инвертировано специально для маски
        oper_i = {'{x}': 'НЕ', 'np.logical_not({x})': ''}
        oper = {'&': 'И', '|': 'ИЛИ'}
        expr = {
            'bin':
            {
                '< {n}': '< {n}', '<= {n}': '<= {n}', '> {n}': '> {n}', '>= {n}': '>= {n}'
            }
        }
        bounds = {
            '%': (2, 5),     #если деление
            '!': (1, 10000-1)
        }
#============================================================================
        finish_flg = False
        while not finish_flg:
            finish_flg = True

            self._var = choices(namevar)[0]
            expr1 = 'bin'
            expr2 = 'bin'
            expr3 = 'bin'

            expr1_oper = choices(list(expr[expr1].keys()))[0]
            oper_1 = choices(list(oper_i.keys()), weights=[.5, .5])[0]
            bound1 = choices(list(range(*bounds['!']))[1:-1])[0]
            mask = eval(oper_1.format(x=('(domain '+expr1_oper.format(n=bound1)+')'))),
            
            domain1 = np.array(domain)[~np.array(mask)[0]]

            bound2 = bound1 - 1 if domain[0] == domain1[0] else bound1 + 1
            expr2_oper = choices(list(expr[expr2].keys()))[0]
            oper_2 = choices(list(oper_i.keys()), weights=[.5, .5])[0]
            main_oper = '&'
            for bound2 in range(bound1 - 1, bound1 + 1):

                mask2 = eval(oper_2.format(x=('(domain '+expr2_oper.format(n=bound2)+')'))),

                domain2 = np.array(domain)[~np.array(mask2)[0]]
                
                domain3 = eval(f'set(domain1) {main_oper} set(domain2)')
                if len(domain3) == 1:
                    break
            
            self._oper1 = oper_i[oper_1]
            self._oper2 = oper_i[oper_2]
            self._oper = oper[main_oper]
            self._expr1 = expr[expr1][expr1_oper].format(n=str(bound1)) if expr1=='bin' else expr[expr1][expr1_oper]
            self._expr2 = expr[expr2][expr2_oper].format(n=str(bound2)) if expr2=='bin' else expr[expr2][expr2_oper]

            change = {
                    '<=': '>',
                    '>=': '<',
                    '<': '>=',
                    '>': '<='
            }
            if 'НЕ' not in [self._oper1, self._oper2]:
                all_exprs = self._expr1 + self._expr2
            elif 'НЕ' == self._oper1:
                all_exprs = self._expr2
                for c in change.keys():
                    if c in self._expr1:
                        all_exprs += self._expr1.replace(c, change[c])
                        break
            else:
                all_exprs = self._expr1
                for c in change.keys():
                    if c in self._expr2:
                        all_exprs += self._expr2.replace(c, change[c])
                        break

            less_cnt = all_exprs.count('<')
            more_cnt = all_exprs.count('>')

            if (
                (len(domain3) == 1)
                 and
                not (self._oper1 == self._oper2 and self._expr1 == self._expr2)
                 and
                (list(domain3)[0] not in bounds['!'])
            ):
                self._answer = domain3.pop()
            else:
                finish_flg = False
                continue

    def question_text(self):
        return self.question.format(
            var=self._var,
            capacity="",
            costyl1="",
            costyl2="",
            costyl3="",
            minmax="",
            oper=self._oper,
            operr2=self._operr2,
            oper1=self._oper1,
            oper2=self._oper2,
            oper3=self._oper3,
            expr1=self._expr1,
            expr2=self._expr2,
            expr3=self._expr3
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Три высказывания - истинно"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()


class SubtypeB(Type4):
    """Истинность высказывания - три высказывания - ложно"""
    question = """
    Напишите {minmax} {capacity} число <i>{var}</i>, для которого ложно высказывание: 
<br>
<code>
<b>{oper1}</b> ({costyl1}<i>{var}</i> {expr1}) <b> {oper} </b> <b>{oper2}</b> ({costyl2}<i>{var}</i> {expr2}) {operr2} </b> <b>{oper3}</b> ({costyl3}<i>{var}</i> {expr3}) 
</code>
    """
    _minmax, _costyl1, _costyl2, _costyl3, _capacity = [""]*5
    def __init__(self):
        # super().__init__()


#===========================================================================
        import numpy as np
        namevar = 'abcdnmtpxyz'
        domain = np.array(list(range(1, 10000)))
        # НЕ ОШИБКА!!! инвертировано специально для маски
        oper_i = {'{x}': 'НЕ', 'np.logical_not({x})': ''}
        oper = {'&': 'И', '|': 'ИЛИ'}
        expr = {
            'bin':
            {
                '< {n}': '< {n}', '<= {n}': '<= {n}', '> {n}': '> {n}', '>= {n}': '>= {n}'
            }
        }
        bounds = {
            '%': (2, 5),     #если деление
            '!': (1, 10000-1)
        }
#============================================================================
        finish_flg = False
        while not finish_flg:
            finish_flg = True

            self._var = choices(namevar)[0]
            expr1 = 'bin'
            expr2 = 'bin'

            expr1_oper = choices(list(expr[expr1].keys()))[0]
            oper_1 = choices(list(oper_i.keys()), weights=[.5, .5])[0]
            bound1 = choices(list(range(*bounds['!']))[1:-1])[0]
            mask = eval(oper_1.format(x=('(domain '+expr1_oper.format(n=bound1)+')'))),
            
            domain1 = np.array(domain)[~np.logical_not(np.array(mask)[0])]

            bound2 = bound1 - 1 if domain[0] == domain1[0] else bound1 + 1
            expr2_oper = choices(list(expr[expr2].keys()))[0]
            oper_2 = choices(list(oper_i.keys()), weights=[.5, .5])[0]
            main_oper = '|'
            for bound2 in range(bound1 - 1, bound1 + 1):

                mask2 = eval(oper_2.format(x=('(domain '+expr2_oper.format(n=bound2)+')'))),

                domain2 = np.array(domain)[~np.logical_not(np.array(mask2)[0])]
                
                domain3 = eval(f'set(domain1) {(set(oper.keys()) - set(main_oper)).pop()} set(domain2)')
                if len(domain3) == 1:
                    break
            
            self._oper1 = oper_i[oper_1]
            self._oper2 = oper_i[oper_2]
            self._oper = oper[main_oper]
            self._expr1 = expr[expr1][expr1_oper].format(n=str(bound1)) if expr1=='bin' else expr[expr1][expr1_oper]
            self._expr2 = expr[expr2][expr2_oper].format(n=str(bound2)) if expr2=='bin' else expr[expr2][expr2_oper]

            change = {
                    '<=': '>',
                    '>=': '<',
                    '<': '>=',
                    '>': '<='
            }
            if 'НЕ' not in [self._oper1, self._oper2]:
                all_exprs = self._expr1 + self._expr2
            elif 'НЕ' == self._oper1:
                all_exprs = self._expr2
                for c in change.keys():
                    if c in self._expr1:
                        all_exprs += self._expr1.replace(c, change[c])
                        break
            else:
                all_exprs = self._expr1
                for c in change.keys():
                    if c in self._expr2:
                        all_exprs += self._expr2.replace(c, change[c])
                        break

            less_cnt = all_exprs.count('<')
            more_cnt = all_exprs.count('>')

            if (
                (len(domain3) == 1)
                 and
                not (self._oper1 == self._oper2 and self._expr1 == self._expr2)
                 and
                (list(domain3)[0] not in bounds['!'])
            ):
                self._answer = domain3.pop()
            else:
                finish_flg = False
                continue

    def question_text(self):
        return self.question.format(
            var=self._var,
            capacity="",
            costyl1="",
            costyl2="",
            costyl3="",
            minmax="",
            oper=self._oper,
            operr2=self._operr2,
            oper1=self._oper1,
            oper2=self._oper2,
            oper3=self._oper3,
            expr1=self._expr1,
            expr2=self._expr2,
            expr3=self._expr3
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Три высказывания - ложно"
    
    @property
    def get_subtype_num(self):
        return 2

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
