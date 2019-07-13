from .common import *

class Type3(Task1):
    """Количество чисел больших выражения"""
    def __init__(self):
        super().__init__()
        bases = list(range(2, 17, 2))
        self.base = bases[randint(0, len(bases)-1)]
        self.question = "Даны {col}, записанных в {notation}-й системе счисления:\t{numbers}.\nСколько из них {sign}, чем {vyr}?"
        self._col = randint(4, 6)
        self.col = f"{self._col} числа" if self._col == 4 else f"{self._col} чисел"
        num = randint(10**3, 2**15)
        self.nums = []
        signs = ["больше", "меньше"]
        self.answer = 0
        self.sign = signs[randint(0, 1)]
        for _ in range(self._col):
            a = randint(num-1000, num+1000)
            if self.sign == "больше":
                if a > num:
                    self.answer += 1
            else:
                if a < num:
                    self.answer += 1
            self.nums.append(str(transform(a, self.base)).upper())
        bases = list(range(2, 17, 2))*3+list(range(2, 32))
        signs = ["+", "-"]
        signs = signs[randint(0, 1)]
        if signs == "+":
            num1 = randint(100, num-10)
            num2 = num - num1
        else:
            num1 = randint(num, num*2)
            num2 = num1 - num
        self.vyr = transform(num1, bases[randint(0, len(bases)-1)], based=True) + signs + transform(num2, bases[randint(0, len(bases)-1)], based=True)
        self.vyr = self.vyr.upper()


    def category(self):
        return 'Количество чисел больших, меньших выражения'

    def question_text(self):
        return self.question.format(
            col=self.col,
            notation=self.base,
            numbers=", ".join(self.nums),
            sign=self.sign,
            vyr=self.vyr
        )

    def question_answer(self):
        return self.answer

class SubtypeA(Type3):
    def level(self):
        return "mid"
    
    @property
    def max_qty(self):
        return 0