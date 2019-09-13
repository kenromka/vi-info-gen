from .common import *
import numpy as np
from random import randint
from ...tools.choices import choices

class Type0(Task5):
    """Формальное исполнение алгоритмов"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Формальное исполнение алгоритмов"
    
    @property
    def get_type_num(self):
        return 1
	
    def level(self):
        return "ez"


class SubtypeA(Type0):
    """Исполнитель с фиксированными командами"""
    def __init__(self):
        super().__init__()

        self.question = """
<p>У исполнителя Альфа две команды, которым присвоены номера: </p>
<ol>
<b>
<li>{cmd1}</li> 
<li>{cmd2}</li>
</b>
</ol> 
(<i>{b_letter}</i> – неизвестное натуральное число; <i>{b_letter}</i> ≥ {bound}).
<br>
<p>Выполняя первую из них, Альфа {cmd_verb[0]} число на экране на {cmd1_a}, а выполняя вторую, {cmd_verb[1]} это число на {cmd2_b}. 
Программа для исполнителя Альфа  –  это последовательность номеров команд. Известно, что программа {prog} переводит число {num1} в число {num2}. 
Определите значение <i>{b_letter}</i>.</p>
        """


#============================================================================
        b_letter = choices('abcdkmnptxyz')[0]
        cmd_verbs = {
            'увеличивает': '+',
            'уменьшает': '-',
            'умножает': '*'
        }
        cmd_verbs_other_form = {
            'увеличивает': 'прибавь ',
            'уменьшает': 'отними ',
            'умножает': 'умножь на '
        }
#============================================================================
        cmd_verb = []
        cmd_verb.append(choices(list(cmd_verbs.keys()))[0])
        cmd_verb.append(choices(list(set(cmd_verbs.keys())-set([cmd_verb[0]])))[0])

        num2 = -100

        while num2 < -30 or num2 > 150:
            num1 = randint(1, 15)

            prog = choices([0, 1], k=5)        

#============================================================================
        
            numbers = choices(list(range(1, 10)), k=2)
            
            if randint(0, 1):
                cmd1_a = numbers[0]
                cmd2_b = f'<i>{b_letter}</i>'
                self._answer = numbers[1]
            else:
                cmd1_a = f'<i>{b_letter}</i>'
                cmd2_b = numbers[1]
                self._answer = numbers[0]
                

            f = lambda prog: eval(f'{f(prog[:-1])} {cmd_verbs[cmd_verb[prog[-1]]]} {numbers[prog[-1]]}') if prog else num1

            num2 = f(prog)
            
            self._cmd_verb = cmd_verb
            self._b_letter = b_letter
            self._prog = ''.join(list(map(lambda x: str(x+1), prog)))
            self._cmd1_a = cmd1_a
            self._cmd2_b = cmd2_b
            self._cmd1, self._cmd2 = (cmd_verbs_other_form[cmd_verb[0]] + str(cmd1_a), cmd_verbs_other_form[cmd_verb[1]] + str(cmd2_b))
            self._num1, self._num2 = num1, num2



    def question_text(self):
        return self.question.format(
            cmd1 = self._cmd1,
            cmd2 = self._cmd2,
            b_letter = self._b_letter,
            cmd_verb = self._cmd_verb,
            cmd1_a = self._cmd1_a,
            cmd2_b = self._cmd2_b,
            prog = self._prog,
            num1 = self._num1,
            num2 = self._num2,
            bound = choices(
                list(range(1, min(4, self._answer)+1))+[1]
            )[0]
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Исполнитель с фиксированными командами"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
