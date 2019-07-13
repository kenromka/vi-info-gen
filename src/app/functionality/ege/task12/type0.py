from .common import *


class Type0(Task12):
    """Номер компьютера в сети"""
    def __init__(self):
        super().__init__()
        self.question = "Маской подсети называется 32-разрядное двоичное число,"\
        " которое определяет, какая часть IP-адреса компьютера относится к адресу сети,"\
        " а какая часть IP-адреса определяет адрес компьютера в подсети. В маске подсети"\
        " старшие биты, отведенные в IP-адресе компьютера для адреса сети, имеют значение 1;"\
        " младшие биты, отведенные в IP-адресе компьютера для адреса компьютера в подсети, "\
        " имеют значение 0.\n"\
        "<br>Если маска подсети {netmask} и IP-адрес компьютера в сети {host},"\
        " то номер компьютера в сети равен _____"

    def category(self):
        return "Номер компьютера в сети"
    
    def level(self):
        return "mid"
    

class SubtypeA(Type0):
    """Номер компьютера в сети"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddressDeterminate()

    def question_text(self):
        return self.question.format(
            netmask=self.task.netmask(),
            host=self.task.host()
        )

    def question_answer(self):
        return self.task.hostnumber()
    
    @property
    def max_qty(self):
        return 5000


