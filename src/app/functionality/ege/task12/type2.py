from .common import *
from random import shuffle


class Type2(Task12):
    """Адрес сети"""
    def __init__(self):
        super().__init__()
        self.question = "В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть"\
        " IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. "\
        "Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу "\
        "узла и его маске.<br>По заданным IP-адресу узла и маске определите адрес сети: "\
        "IP-адрес: {host} Маска: {netmask}<br>"\
        "При записи ответа выберите из приведенных в таблице чисел четыре элемента IP-адреса"\
        " и запишите в нужном порядке соответствующие им буквы без точек."\
        "{table}<br><p>Пример. Пусть искомый адрес сети 192.168.128.0 и дана таблица</p>"\
        "<table border='1'>"\
        "<tr><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th></tr>"\
        "<tr><td>128</td><td>168</td><td>255</td><td>8</td><td>127</td><td>0</td><td>17</td><td>192</td></tr>"\
        "</table>"\
        "<p>В этом случае правильный ответ будет HBAF.</p>"

    def category(self):
        return "Адрес сети"
    
    def level(self):
        return "mid"


class SubtypeA(Type2):
    """Адрес сети"""
    def __init__(self):
        super().__init__()
        self.task = LimitMaskedHostAddressDeterminate(randint(9, 31))
        right_vals = str(self.task.network()).split(".")
        values = []
        values.extend(right_vals)
        if "0" not in right_vals:
            values.append("0")
        if "255" not in right_vals:
            values.append("255")
        while len(values) != 8:
            val = str(randint(1, 254))
            if val not in right_vals:
                values.append(val)
        
        shuffle(values)
        
        self._answer = [None]*4
        table_values = zip("ABCDEFGH", values)

        table = "<table border='1'>\n<tr><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th></tr>\n<tr>"
        for letter, val in table_values:
            if val in right_vals:
                self._answer[right_vals.index(val)] = letter
                right_vals[right_vals.index(val)] = None
            table += f"<td>{val}</td>"
        self._answer = "".join(self._answer)
        table += "</tr>\n</table>"
        self._table = table

    def question_text(self):
        return self.question.format(
            host=self.task.host(),
            netmask=self.task.netmask(),
            table=self._table
        )

    def question_answer(self):
        return self._answer
    
    @property
    def max_qty(self):
        return 5000

