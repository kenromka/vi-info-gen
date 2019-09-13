from .common import *
from random import randint, shuffle
from ...tools.choices import choices

class Type0(Task7):
    """Принципы адресации ресурсов в сети Интернет"""
    def __init__(self):
        super().__init__()

        files = ["slon", "tiger", "cat", "dog", "start", "img", "name", "color", "test", "math", "rus", "hello", "tech", "exam", "lesson", "inf"]
        extensions = [".txt", ".doc", ".docx", ".xls", ".xlsx", ".jpg", ".png", ".exe", ".htm", ".gif", ".pdf"]
        protocols = ["http", "ftp", "https"]
        servers = ["zoo", "game", "pic", "box", "ofis", "home", "cafe", "birthday", "book", "biblioteka", "school", "city", "paris", "happy"]
        tlds = [".org", ".ru", ".com", ".net"]
        self._file = choices(files)[0]
        self._catalog = choices(list(set(files) - set(self._file)))[0]
        self._extension = choices(extensions)[0]
        self._protocol = choices(protocols)[0]
        self._server = choices(servers)[0]
        self._tld = choices(tlds)[0]
        self.question = "Доступ к файлу <b>{file}{extension}</b>, находящемуся на сервере <b>{server}{tld}</b>, осуществляется "\
        "по протоколу <b>{protocol}</b>. Фрагменты адреса файла закодированы цифрам от <i>1</i> до <i>7</i>."\
        " Запишите в ответе последовательность этих цифр, кодирующую адрес указанного файла в сети Интернет.{list}"
        
    def category(self):
        return "Принципы адресации ресурсов в сети Интернет"
    
    @property
    def get_type_num(self):
        return 1
	
    def level(self):
        return "ez"


class SubtypeA(Type0):
    """Расположение файла - без каталога"""
    def __init__(self):
        super().__init__()

#============================================================================
        fragments = [self._protocol, "://", self._server, self._tld, "/", self._file, self._extension]
        
        values = fragments
        shuffle(fragments)
        
        self._answer = []
        lst_values = zip(fragments, "1234567")
        values = dict(zip(fragments, "1234567"))

        lst = "\n<ol>"
        for val, _ in lst_values:
            lst += f"<li>{val}</li>"
        fragments = [self._protocol, "://", self._server, self._tld, "/", self._file, self._extension]
        for frag in fragments:
            self._answer.append(values[frag])
        self._answer = "".join(self._answer)
        lst += "</ol>\n"
        self._lst = lst
#============================================================================

    def question_text(self):
        return self.question.format(
            file=self._file,
            extension=self._extension,
            server=self._server,
            tld=self._tld,
            protocol=self._protocol,
            list=self._lst
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Расположение файла - без каталога"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()


class SubtypeB(Type0):
    """Расположение файла - с каталогом"""
    def __init__(self):
        super().__init__()

        self.question = "Доступ к файлу <b>{file}{extension}</b>, находящемуся на сервере <b>{server}{tld}</b> в каталоге <b>{catalog}</b>, осуществляется "\
        "по протоколу <b>{protocol}</b>. Фрагменты адреса файла закодированы цифрам от <i>1</i> до <i>8</i>."\
        " Запишите в ответе последовательность этих цифр, кодирующую адрес указанного файла в сети Интернет.{list}"
#============================================================================
        fragments = [self._protocol, "://", self._server, self._tld, "/", self._catalog, self._file, self._extension]
        
        values = fragments
        shuffle(fragments)
        
        self._answer = []
        lst_values = zip(fragments, "12345678")
        values = dict(zip(fragments, "12345678"))

        lst = "\n<ol>"
        for val, _ in lst_values:
            lst += f"<li>{val}</li>"
        fragments = [self._protocol, "://", self._server, self._tld, "/", self._catalog, "/", self._file, self._extension]
        for frag in fragments:
            self._answer.append(values[frag])
        self._answer = "".join(self._answer)
        lst += "</ol>\n"
        self._lst = lst
#============================================================================

    def question_text(self):
        return self.question.format(
            file=self._file,
            extension=self._extension,
            catalog=self._catalog,
            server=self._server,
            tld=self._tld,
            protocol=self._protocol,
            list=self._lst
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Расположение файла - с каталогом"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
