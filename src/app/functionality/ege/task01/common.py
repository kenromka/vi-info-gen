from ...tools.task import *
from ...tools.notation import transform
from random import randint, choice
from math import log


class Task1(BaseTask):
    """ЕГЭ по информатике - Задача номер 1"""
    def __init__(self):
        self.number = randint(10**3, 2**15)
        self.digits = '0123456789abcdefghijklmnopqrstuvwxyz'
        self.order = ['ноль', 'одно', 'двух', 'трёх', 'чытырёх', 'пяти', 'шести', 'семи', 'восьми', 'девяти', 'десяти', 'одиннадцати', 'двенадцати', 'тринадцати', 'четырнадцати', 'пятнадцати', 'шестнадцати', 'семнадцати', 'восемнадцати', 'девятнадцати', 'двадцати']
        self.notations = {2: 'двоичной', 3: 'троичной', 4: 'четверичной', 5: 'пятеричной', 6: 'шестеричной', 7: 'семеричной', 8: 'восьмеричной', 9: 'девятеричной', 10: 'десятичной', 11: 'одиннадцатеричной', 12: 'двенадцатеричной', 13: 'тринадцатеричной', 14: 'четырнадцатеричной', 15: 'пятнадцатеричной', 16: 'шестнадцатеричной', 17: 'семнадцатеричной', 18: 'восемнадцатеричной', 19: 'девятнадцатеричной', 20: 'двадцатеричной'}
        self.sign_suffix = 'значное'
        self.base = choice(list(range(2, 10)) + list(range(11, 37)))

    def category(self):
        return "Задача 1"

    def notation(self, base):
        assert(1 < base < 37)
        return self.notations[base] + ' системе счисления' if base in self.notations else 'системе счисления с основанием ' + self.latex(base)

    def linked(self):
        base = randint(2, 6)
        degree = randint(2, int(log(36, base)))
        return base, degree

    def based(self, number, base):
        return self.latex(number if base == 10 else transform(number, base, self.digits, True))

