from .common import *


class Type4(Task12):
    """Третий слева байт маски"""
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
        return "Третий слева байт маски"
    
    def level(self):
        return "mid"
    
    @property
    def max_qty(self):
        return 5000


class SubtypeA(Type4):
    """Третий слева байт маски"""
    def __init__(self):
        super().__init__()
        #ограничение на маску &&&&&&&&?????????????????????
        self.task = LimitMaskedHostAddressDeterminate(randint(17, 24))
        

    def question_text(self):
        return self.question.format(
            host=self.task.host(),
            network=self.task.network(),
            question="Чему равен третий слева байт маски?"
        )

    def question_answer(self):
        return str(self.task.netmask()).split(".")[2]
    

class SubtypeB(Type4):
    """Третий слева октет маски"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddressDeterminate(randint(17, 24))

    def category(self):
        return "Третий слева октет маски"
        

    def question_text(self):
        return self.question.format(
            host=self.task.host(),
            network=self.task.network(),
            question="Чему равен третий слева октет маски?"
        )

    def question_answer(self):
        return str(self.task.netmask()).split(".")[2]


class SubtypeС(Type4):
    """Наибольшее значение третьего байта маски"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddress(randint(17, 24))
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0]:
            self.task = LimitMaskedHostAddress(randint(17, 24))

    def category(self):
        return "Наибольшее значение третьего байта маски"
    
    def level(self):
        return "hard"        

    def question_text(self):
        return self.question.format(
            host=self.task.host(),
            network=self.task.network(),
            question="Чему равно наибольшее возможное значение третьего слева байта маски?"
        )

    def question_answer(self):
        return str(max(self.task.suitable())).split(".")[2]
    


class SubtypeD(Type4):
    """Наименьшее значение третьего байта маски"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddress(randint(17, 24))
        while len(self.task.suitable()) != choices([2, 3, 4, 5])[0]:
            self.task = LimitMaskedHostAddress(randint(17, 24))

    def category(self):
        return "Наименьшее значение третьего байта маски"
    
    def level(self):
        return "hard"        

    def question_text(self):
        return self.question.format(
            host=self.task.host(),
            network=self.task.network(),
            question="Чему равно наименьшее возможное значение третьего слева байта маски?"
        )

    def question_answer(self):
        return str(min(self.task.suitable())).split(".")[2]
    


