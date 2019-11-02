from .common import *
from random import randint
from ...tools.choices import choices

class Type0(Task3):
    """Истинность высказывания"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Истинность высказывания"
    
    @property
    def get_type_num(self):
        return 1
	
    def level(self):
        return "ez"


class SubtypeA(Type0):
    """Истинность высказывания - Граница области определения"""
    def __init__(self):
        super().__init__()

        self.question = """
        Напишите {minmax} число <i>{var}</i>, для которого истинно высказывание: 
<br>
<code>
<b>{oper1}</b> (<i>{var}</i> {expr1}) <b>{oper}</b> <b>{oper2}</b> (<i>{var}</i> {expr2})
</code>
        """


#===========================================================================
        import numpy as np
        minmax = {'min': 'наименьшее', 'max': 'наибольшее'}
        namevar = 'abcdnmtpxyz'
        domain = np.array(list(range(102)))
        # НЕ ОШИБКА!!! инвертировано специально для маски
        oper_i = {'{x}': 'НЕ', 'np.logical_not({x})': ''}
        oper = {'&': 'И', '|': 'ИЛИ'}
        expr = {
            'unary':
            {
                '%2 == 0': 'четное', '%2 != 0': 'нечетное'
            },
            'bin':
            {
                '< {n}': '< {n}', '<= {n}': '<= {n}', '> {n}': '> {n}', '>= {n}': '>= {n}', 
                '%{n} == 0': 'делится на {n} нацело', '%{n} != 0': 'не делится на {n} нацело'
            }
        }
        bounds = {
            '%': (2, 5),     #если деление
            '!': (9, 90)
        }
#============================================================================
        finish_flg = False
        while not finish_flg:
            finish_flg = True
            self._var = choices(namevar)[0]
            expr1 = choices(list(expr.keys()), weights=[.2, .8])[0]
            expr2 = choices(list(expr.keys()), weights=[.3, .7])[0] if expr1 == 'bin' else 'bin'

            expr1_oper = choices(list(expr[expr1].keys()))[0]
            if expr1 == 'bin':
                if '%' in expr1_oper:
                    bound1 = randint(*bounds['%'])
                else:
                    bound1 = randint(*bounds['!'])
                oper_1 = choices(list(oper_i.keys()), weights=[.3, .7])[0]
                mask = eval(oper_1.format(x=('(domain '+expr1_oper.format(n=bound1)+')'))),
                
            else:
                bound1 = None
                oper_1 = choices(list(oper_i.keys()), weights=[.3, .7])[0]
                mask = eval(oper_1.format(x=('(domain '+expr1_oper+')'))),
            
            domain1 = np.array(domain)[~np.array(mask)[0]]
            if len(domain1) < 7:
                domain1 = np.array(domain)[~np.logical_not(mask)]
                oper_1 = (set(oper_i.keys()) - set([oper_1])).pop()

            expr2_oper = choices(list(expr[expr2].keys()))[0]
            if expr2 == 'bin':
                if '%' in expr2_oper:
                    bound2 = randint(*bounds['%'])
                else:
                    bound2 = randint(*bounds['!'])
                oper_2 = choices(list(oper_i.keys()), weights=[.3, .7])[0]
                mask2 = eval(oper_2.format(x=('(domain '+expr2_oper.format(n=bound2)+')'))),
                
            else:
                bound2 = None
                oper_2 = choices(list(oper_i.keys()), weights=[.3, .7])[0]
                mask2 = eval(oper_2.format(x=('(domain '+expr2_oper+')'))),
            
            domain2 = np.array(domain)[~np.array(mask2)[0]]
            if len(domain2) < 7:
                domain2 = np.array(domain)[~np.logical_not(mask2)]
                oper_2 = (set(oper_i.keys()) - set([oper_2])).pop()
            
            main_oper = choices(list(oper.keys()), weights=[.3, .7])[0]
            domain3 = eval(f'set(domain1) {main_oper} set(domain2)')
            if len(domain3) < 3:
                main_oper = (set(oper.keys()) - set([main_oper])).pop()
                domain3 = eval(f'set(domain1) {main_oper} set(domain2)')
            
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
            if 'НЕ' in self._oper1 and 'НЕ' in self._oper2:
                finish_flg = False
                continue
            elif 'НЕ' not in [self._oper1, self._oper2]:
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

            if less_cnt * more_cnt == 1 and oper['|'] != self._oper:
                chosen = choices(list(minmax.keys()))[0]
                self._minmax = minmax[chosen]
                self._answer = eval(chosen+f'({domain3})')
            elif less_cnt == 2 or (less_cnt == 1 and oper['|'] != self._oper):
                self._minmax = minmax['max']
                self._answer = max(domain3)
            elif more_cnt == 2 or (more_cnt == 1 and oper['|'] != self._oper):
                self._minmax = minmax['min']
                self._answer = min(domain3)
            else:
                finish_flg = False
                continue

    def question_text(self):
        return self.question.format(
            minmax=self._minmax,
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
        return "Граница области определения"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
