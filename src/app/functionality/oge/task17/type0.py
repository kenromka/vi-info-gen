from .common import *
from random import shuffle

class Type0(Task17):
    """Последовательность адреса в интернете"""
    def __init__(self):
        super().__init__()
        
        files = ["slon", "tiger", "cat", "dog", "start", "img", "name", "color", "test", "math", "rus", "hello", "tech", "exam", "lesson", "inf"]
        extensions = [".txt", ".doc", ".docx", ".xls", ".xlsx", ".jpg", ".png", ".exe", ".htm", ".gif", ".pdf"]
        protocols = ["http", "ftp", "https"]
        servers = ["zoo", "game", "pic", "box", "ofis", "home", "cafe", "birthday", "book", "biblioteka", "school", "city", "paris", "happy"]
        tlds = [".org", ".ru", ".com", ".net"]
        self._file = choices(files)[0]
        self._catalog = self._file
        self._extension = choices(extensions)[0]
        self._protocol = choices(protocols)[0]
        self._server = choices(servers)[0]
        self._tld = choices(tlds)[0]
        self.question = "Доступ к файлу {file}{extension}, находящемуся на сервере {server}{tld}, осуществляется "\
        "по протоколу {protocol}. В таблице фрагменты адреса файла закодированы буквами от А до Ж."\
        " Запишите последовательность этих букв, кодирующую адрес указанного файла в сети Интернет.{table}"

    def category(self):
        return "Последовательность адреса в интернете"
    
    def level(self):
        return "ez"

class SubtypeA(Type0):
    """Составить URL-адрес"""
    def __init__(self):
        super().__init__()
        
        fragments = [self._protocol, "://", self._server, self._tld, "/", self._file, self._extension]
        
        values = fragments
        shuffle(fragments)
        
        self._answer = []
        table_values = zip(fragments, "АБВГДЕЖ")
        values = dict(zip(fragments, "АБВГДЕЖ"))

        table = "<table border='1'>\n<tr><th>А</th><th>Б</th><th>В</th><th>Г</th><th>Д</th><th>Е</th><th>Ж</th></tr>\n<tr>"
        for val, _ in table_values:
            table += f"<td>{val}</td>"
        fragments = [self._protocol, "://", self._server, self._tld, "/", self._file, self._extension]
        for frag in fragments:
            self._answer.append(values[frag])
        self._answer = "".join(self._answer)
        table += "\n</tr></table>"
        self._table = table

    def question_text(self):
        return self.question.format(
            file=self._file,
            extension=self._extension,
            server=self._server,
            tld=self._tld,
            protocol=self._protocol,
            table=self._table
        )

    def question_answer(self):
        return self._answer

    def category(self):
        return "Адрес без каталога"

    @property
    def max_qty(self):
        return 5000

class SubtypeB(Type0):
    """Адрес с каталогом"""
    def category(self):
        return "Адрес с каталогом"

    def __init__(self):
        super().__init__()
        self.question = "На сервере {server}{tld} в каталоге {catalog} находится файл {file}{extension}"\
        ", доступ к которому осуществляется по протоколу {protocol}. В таблице фрагменты адреса файла закодированы буквами от А до Ж."\
        "Запишите последовательность этих букв, кодирующую адрес указанного файла в сети Интернет.{table}"

        fragments = [self._protocol, "://", self._server, self._tld, "/", self._file, self._extension]
        
        shuffle(fragments)
        
        self._answer = []
        table_values = zip(fragments, "АБВГДЕЖ")
        values = dict(zip(fragments, "АБВГДЕЖ"))

        table = "<table border='1'>\n<tr><th>А</th><th>Б</th><th>В</th><th>Г</th><th>Д</th><th>Е</th><th>Ж</th></tr>\n<tr>"
        for val, _ in table_values:    
            table += f"<td>{val}</td>"
        
        fragments = [self._protocol, "://", self._server, self._tld, "/", self._catalog, "/", self._file, self._extension]
        for frag in fragments:
            self._answer.append(values[frag])
        self._answer = "".join(self._answer)
        table += "\n</tr></table>"
        self._table = table

    def question_text(self):
        return self.question.format(
            file=self._file,
            catalog=self._catalog,
            extension=self._extension,
            server=self._server,
            tld=self._tld,
            protocol=self._protocol,
            table=self._table
        )

    def question_answer(self):
        return self._answer
    
    @property
    def max_qty(self):
        return 5000
    
    def level(self):
        return "mid"