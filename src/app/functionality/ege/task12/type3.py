from .common import *


class Type3(Task12):
    """Маска"""
    def __init__(self):
        super().__init__()
        self._question = choices([
            ("Узлы с IP-адресами {host1} и {host2} находятся в одной сети.", False),
            ("Для узла с IP-адресом {host1} адрес сети равен {host2}.", True)
        ])[0]
        self._question2 = ["Чему равно {mostleast} количество возможных {zerosones} в маске этой сети?", "Для скольких различных значений маски это возможно?"]
        self.question = "В терминологии сетей TCP/IP маской сети называется двоичное число, определяющее, "\
        "какая часть IP-адреса узла сети относится к адресу сети, а какая — к адресу самого узла"\
        " в этой сети. При этом в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого"\
        " места — нули. Обычно маска записывается по тем же правилам, что и IP-адрес, — в виде"\
        " четырёх байтов, причём каждый байт записывается в виде десятичного числа. Адрес сети "\
        "получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла и "\
        "маске. Например, если IP-адрес узла равен 192.62.255.182, а маска равна 255.255.240.0, то адрес сети"\
        " равен 192.62.240.0.<br>"\
        "{question} {question2}"

    def category(self):
        return "Маска"
    
    def level(self):
        return "hard"
    
    @property
    def max_qty(self):
        return 5000


class SubtypeA(Type3):
    """Наибольшее количество единиц в маске"""
    def __init__(self):
        super().__init__()
        n_ones = randint(8, 31)
        self.task = LimitMaskedHostAddress(n_ones)
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0] or self.task.host() == self.task.network():
            self.task = LimitMaskedHostAddress(n_ones)
    
    def category(self):
        return "Наибольшее количество единиц в маске"

    def question_text(self):
        if self._question[1] or len(transform(int(self.task.network()), 2).split("1")[-1]) <= len(self.task.suitable()):
            self._host2 = self.task.network()
        else:
            self._host2 = MaskedHostAddress(address=randint(int(self.task.network()), int(self.task.network()) + 2 ** (len(transform(int(self.task.network()), 2).split("1")[-1]) - len(self.task.suitable())))).host()
        return self.question.format(
            question=self._question[0].format(
                host1=self.task.host(),
                host2=self._host2
            ),
            question2=self._question2[0].format(
                mostleast="наибольшее",
                zerosones="единиц"
            )
        )

    def question_answer(self):
        return max(self.task.suitable()).ones()
    

class SubtypeB(Type3):
    """Наименьшее количество единиц в маске"""
    def __init__(self):
        super().__init__()
        n_ones = randint(8, 31)
        self.task = LimitMaskedHostAddress(n_ones)
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0] or self.task.host() == self.task.network():
            self.task = LimitMaskedHostAddress(n_ones)
    
    def category(self):
        return "Наименьшее количество единиц в маске"

    def question_text(self):
        if self._question[1] or len(transform(int(self.task.network()), 2).split("1")[-1]) <= len(self.task.suitable()):
            self._host2 = self.task.network()
        else:
            self._host2 = MaskedHostAddress(address=randint(int(self.task.network()), int(self.task.network()) + 2 ** (len(transform(int(self.task.network()), 2).split("1")[-1]) - len(self.task.suitable())))).host()
        return self.question.format(
            question=self._question[0].format(
                host1=self.task.host(),
                host2=self._host2
            ),
            question2=self._question2[0].format(
                mostleast="наименьшее",
                zerosones="единиц"
            )
        )

    def question_answer(self):
        return min(self.task.suitable()).ones()
    

class SubtypeC(Type3):
    """Наибольшее количество нулей в маске"""
    def __init__(self):
        super().__init__()
        n_ones = randint(8, 31)
        self.task = LimitMaskedHostAddress(n_ones)
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0] or self.task.host() == self.task.network():
            self.task = LimitMaskedHostAddress(n_ones)
    
    def category(self):
        return "Наибольшее количество нулей в маске"

    def question_text(self):
        if self._question[1] or len(transform(int(self.task.network()), 2).split("1")[-1]) <= len(self.task.suitable()):
            self._host2 = self.task.network()
        else:
            self._host2 = MaskedHostAddress(address=randint(int(self.task.network()), int(self.task.network()) + 2 ** (len(transform(int(self.task.network()), 2).split("1")[-1]) - len(self.task.suitable())))).host()
        return self.question.format(
            question=self._question[0].format(
                host1=self.task.host(),
                host2=self._host2
            ),
            question2=self._question2[0].format(
                mostleast="наибольшее",
                zerosones="нулей"
            )
        )

    def question_answer(self):
        return min(self.task.suitable()).zeros()
    

class SubtypeD(Type3):
    """Наименьшее количество нулей в маске"""
    def __init__(self):
        super().__init__()
        n_ones = randint(8, 31)
        self.task = LimitMaskedHostAddress(n_ones)
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0] or self.task.host() == self.task.network():
            self.task = LimitMaskedHostAddress(n_ones)
    
    def category(self):
        return "Наименьшее количество нулей в маске"

    def question_text(self):
        if self._question[1] or len(transform(int(self.task.network()), 2).split("1")[-1]) <= len(self.task.suitable()):
            self._host2 = self.task.network()
        else:
            self._host2 = MaskedHostAddress(address=randint(int(self.task.network()), int(self.task.network()) + 2 ** (len(transform(int(self.task.network()), 2).split("1")[-1]) - len(self.task.suitable())))).host()
        return self.question.format(
            question=self._question[0].format(
                host1=self.task.host(),
                host2=self._host2
            ),
            question2=self._question2[0].format(
                mostleast="наименьшее",
                zerosones="нулей"
            )
        )

    def question_answer(self):
        return max(self.task.suitable()).zeros()
    

class SubtypeE(Type3):
    """Количество масок"""
    def __init__(self):
        super().__init__()
        n_ones = randint(8, 31)
        self.task = LimitMaskedHostAddress(n_ones)
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0] or self.task.host() == self.task.network():
            self.task = LimitMaskedHostAddress(n_ones)
    
    def category(self):
        return "Количество масок"

    def question_text(self):
        if self._question[1] or len(transform(int(self.task.network()), 2).split("1")[-1]) <= len(self.task.suitable()):
            self._host2 = self.task.network()
        else:
            self._host2 = MaskedHostAddress(address=randint(int(self.task.network()), int(self.task.network()) + 2 ** (len(transform(int(self.task.network()), 2).split("1")[-1]) - len(self.task.suitable())))).host()
        return self.question.format(
            question=self._question[0].format(
                host1=self.task.host(),
                host2=self._host2
            ),
            question2=self._question2[1]
        )

    def question_answer(self):
        return len(self.task.suitable())