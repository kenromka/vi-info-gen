from .common import *


class Type5(Task12):
    """Последний байт маски"""
    def __init__(self):
        super().__init__()
        self.question = "В терминологии сетей TCP/IP маской сети называется двоичное число, определяющее, какая"\
        " часть IP-адреса узла сети относится к адресу сети, а какая – к адресу"\
        " самого узла в этой сети. При этом в маске сначала (в старших разрядах) стоят единицы,"\
        " а затем с некоторого места – нули. Обычно маска записывается по тем же правилам, что и IP-адрес – "\
        "в виде четырёх байтов, причём каждый байт записывается в виде десятичного числа."\
        " Адрес сети получается в результате применения поразрядной конъюнкции к заданному"\
        " IP-адресу узла и маске. Например, если IP-адрес узла равен 192.62.255.182, а маска равна 255.255.240.0, "\
        "то адрес сети равен 192.62.240.0.<br>"\
        "Для узла с IP-адресом {host} адрес сети равен {network}. "\
        "{question} Ответ запишите в виде десятичного числа."


    def category(self):
        return "Последний байт маски"
    
    def level(self):
        return "mid"

    @property
    def max_qty(self):
        return 5000


class SubtypeA(Type5):
    """Последний байт маски"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddressDeterminate(randint(25, 31))
        

    def question_text(self):
        return self.question.format(
            host=self.task.host(),
            network=self.task.network(),
            question="Чему равен последний (самый правый) байт маски?"
        )

    def question_answer(self):
        return str(self.task.netmask()).split(".")[-1]


class SubtypeB(Type5):
    """Наибольшее значение последнего байта маски"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddress(randint(25, 31))
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0] or self.task.host() == self.task.network():
            self.task = LimitMaskedHostAddress(randint(25, 31))

    def category(self):
        return "Наибольшее значение последнего байта маски"
    
    def level(self):
        return "hard"        

    def question_text(self):
        return self.question.format(
            host=self.task.host(),
            network=self.task.network(),
            question="Чему равно наибольшее возможное значение последнего (самого правого) байта маски?"
        )

    def question_answer(self):
        return str(max(self.task.suitable())).split(".")[-1]
    

class SubtypeC(Type5):
    """Наименьшее значение последнего байта маски"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddress(randint(25, 31))
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0] or self.task.host() == self.task.network():
            self.task = LimitMaskedHostAddress(randint(25, 31))

    def category(self):
        return "Наименьшее значение последнего байта маски"
    
    def level(self):
        return "hard"        

    def question_text(self):
        return self.question.format(
            host=self.task.host(),
            network=self.task.network(),
            question="Чему равно наименьшее возможное значение последнего (самого правого) байта маски?"
        )

    def question_answer(self):
        return str(min(self.task.suitable())).split(".")[-1]
    

