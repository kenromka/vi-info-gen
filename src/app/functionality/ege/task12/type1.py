from .common import *

class Type1(Task12):
    """Количество адресов"""
    def __init__(self):
        super().__init__()
        self.question = "В терминологии сетей TCP/IP маской подсети называется 32-разрядное двоичное число,"\
        " определяющее, какие именно разряды IP-адреса компьютера являются общими для всей подсети"\
        " – в этих разрядах маски стоит 1. Обычно маски записываются в виде"\
        " четверки десятичных чисел - по тем же правилам, что и IP-адреса.<br>Для некоторой подсети"\
        " используется маска {netmask}. Сколько различных адресов компьютеров теоретически допускает"\
        " эта маска, если два адреса (адрес сети и широковещательный) не используют?"

    def category(self):
        return "Количество адресов"
    
    def level(self):
        return "mid"




class SubtypeA(Type1):
    """Количество адресов"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddressDeterminate()

    def question_text(self):
        return self.question.format(
            netmask=self.task.netmask()
        )

    def question_answer(self):
        return 2**(self.task.network_mask.zeros()) - 2
    
    @property
    def max_qty(self):
        return 9

class SubtypeB(Type1):
    """Наименьшее количество адресов"""
    def __init__(self):
        super().__init__()
        self.examples = [
            {"host": "192.62.255.182", "network_mask": "255.255.240.0", "network": "192.62.240.0"}
        ]
        self.question = "В терминологии сетей TCP/IP маской сети называется двоичное число, определяющее,"\
        " какая часть IP-адреса узла сети относится к адресу сети, а какая — к адресу "\
        "самого узла в этой сети. При этом в маске сначала (в старших разрядах) стоят единицы,"\
        " а затем с некоторого места — нули. Обычно маска записывается по тем же правилам, что"\
        " и IP-адрес, — в виде четырёх байтов, причём каждый байт записывается в виде десятичного "\
        "числа. Адрес сети получается в результате применения поразрядной конъюнкции к"\
        " заданному IP-адресу узла и маске.\nНапример, если IP-адрес узла равен {example_host},"\
        " а маска равна {example_hostmask}, то адрес сети равен {example_network}.<br>Для узла с IP-адресом {host}"\
        " адрес сети равен {network}. Чему равно наименьшее количество возможных адресов в этой сети?"

        n_ones = randint(20, 29)
        self.task = LimitMaskedHostAddress(n_ones)
        while len(self.task.suitable()) != choices([2, 3, 4])[0]:
            self.task = LimitMaskedHostAddress(n_ones)
    
    def category(self):
        return "Наименьшее количество адресов"
    
    def level(self):
        return "hard"

    def question_text(self):
        example = choices(self.examples)[0]
        return self.question.format(
            example_host=example["host"],
            example_hostmask=example["network_mask"],
            example_network=example["network"],
            host=self.task.host(),
            network=self.task.network()
        )

    def question_answer(self):
        return 2**(max(self.task.suitable()).zeros())
    
    @property
    def max_qty(self):
        return 5000
