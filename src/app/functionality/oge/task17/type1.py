from .common import *
from random import shuffle

class Type1(Task17):
    """Восстановить IP-адрес"""
    def __init__(self):
        super().__init__()
        
        self.question = "На месте преступления были обнаружены четыре обрывка бумаги. Следствие установило, что"\
        " на них записаны фрагменты одного IP-адреса. Криминалисты "\
        "обозначили эти фрагменты буквами А, Б, В и Г. Восстановите IP-адрес. {table}"\
        "<p>В ответе укажите последовательность букв, обозначающих фрагменты,"\
        " в порядке, соответствующем IP-адресу.</p>"
    def category(self):
        return "Восстановить IP-адрес"
    
    def level(self):
        return "ez"
    
    @property
    def max_qty(self):
        return 5000


class SubtypeA(Type1):
    """Составить IP-адрес"""
    def __init__(self):
        super().__init__()
        result_ip = f"{randint(100, 255)}.{randint(100, 255)}.{randint(100, 255)}.{randint(26, 255)}"
        
        fragments = [result_ip[:2], result_ip[2:6], result_ip[6:11], result_ip[11:]]
        values = fragments[:]
        shuffle(fragments)
        
        self._answer = []
        table_values = zip(fragments, "АБВГ")
        values2 = dict(zip(fragments, "АБВГ"))

        table = "<table border='1'>\n<tr>"
        for val, _ in table_values:
            table += f"<th>{val}</th>"

        for frag in values:
            self._answer.append(values2[frag])
        self._answer = "".join(self._answer)
        table += "\n</tr><tr><td>А</td><td>Б</td><td>В</td><td>Г</td></tr>\n</table>"
        self._table = table

    def question_text(self):
        return self.question.format(
            table=self._table
        )

    def question_answer(self):
        return self._answer
