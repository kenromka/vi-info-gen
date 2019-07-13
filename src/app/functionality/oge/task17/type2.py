from .common import *
from random import shuffle
from copy import copy

class Type2(Task17):
    """Электронная почта"""
    def __init__(self):
        super().__init__()
        
        nicknames = ["Ivanov_Maksim", "Ivanov_Ivan", "Ivanova_Nina", "Ivanova_Masha", "Masha", "Nina", "Natasha", "Natasha93", "Zina5", "Zina", "Ivanov_Pasha", "Pasha", "Olga", "Olga95", "Misha", "Misha_Iv", "Vas90", "Mama5", "teacher", "pupil", "best_pupil"]
        domains = ["klass.school.ru", "mail.ru", "gmail.com", "yandex.ru", "school.ru", "work.com", "my.work.com", "my.work.ru", "егэ.рф", "огэ.рф", "школа.рф", "класс.рф"]
        letters = "АБВГДЕЖЗ"
        self._nickname = choices(nicknames)[0]
        self._domain = choices(domains)[0]
        self._letters = letters[:3+self._nickname.count("_")+self._domain.count(".")]
        self.question = "Почтовый ящик {nickname} находится на сервере {domain}. "\
        "Фрагменты адреса электронной почты закодированы буквами от А до {letter}."\
        " Запишите последовательность букв, кодирующую этот адрес.{table}"

    def category(self):
        return "Электронная почта"
    
    def level(self):
        return "ez"

class SubtypeA(Type2):
    """Электронная почта"""
    def __init__(self):
        super().__init__()
        
        nick = self._nickname.split("_")
        fragments = [nick[0]]
        if len(nick) == 2:
            fragments.append(f"_{nick[1]}")
        fragments.append("@")
        dom = self._domain.split(".")
        fragments.extend([dom[0], f".{dom[1]}"])
        if len(dom) == 3:
            fragments.append(f".{dom[2]}")
        ans_frags = copy(fragments)
        values = fragments
        shuffle(fragments)
        
        self._answer = []
        table_values = zip(fragments, self._letters)
        values = dict(zip(fragments, self._letters))

        table = "<table border='1'>\n<tr>"
        for l in self._letters:
            table += f"<th>{l}</th>"
        table += "</tr>\n<tr>"
        for val, _ in table_values:
            table += f"<td>{val}</td>"

        for frag in ans_frags:
            self._answer.append(values[frag])
        self._answer = "".join(self._answer)
        table += "\n</tr></table>"
        self._table = table

    def question_text(self):
        return self.question.format(
            nickname = self._nickname,
            domain = self._domain,
            letter = self._letters[-1],
            table = self._table
        )

    def question_answer(self):
        return self._answer

    def category(self):
        return "Электронная почта"

    @property
    def max_qty(self):
        return 252