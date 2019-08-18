from .common import *
from random import randint

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

class Type4(Task10):
    """Другие алгоритмы"""
    def __init__(self):
        super().__init__()

        self.question = choices(["В таб­ли­це Tok хра­нят­ся дан­ные из­ме­ре­ний сред­не­су­точ­ной "\
        "тем­пе­ра­ту­ры за {length} дней в гра­ду­сах (Tok[1] — дан­ные за пер­вый день, "\
        "Tok[2] — за вто­рой и т. д.). Определите, какое число будет на­пе­ча­та­но в"\
        " ре­зуль­та­те ра­бо­ты сле­ду­ю­щей программы. Текст про­грам­мы приведён на пяти язы­ках программирования.{table}",
        "В таблице Tok представлены данные о количестве голосов, поданных за {length} исполнителей народных"\
        " песен (Tok[1] – количество голосов, поданных за первого исполнителя; Tok[2] – за второго и т. д.)."\
        " Определите, какое число будет напечатано в результате работы следующей программы. "\
        "Текст программы приведён на пяти языках программирования.<br>{table}"])[0]
        
    def category(self):
        return "Анализ алгоритмов - Другие алгоритмы"
    
    def level(self):
        return "mid"

class SubtypeA(Type4):
    """Другие алгоритмы"""
    def __init__(self):
        super().__init__()
        self._length = choices([10, 12])[0]
        if "температуры" in self.question:
            median = randint(-10, 20)
        else:
            median = randint(50, 80)
        dat = [median+randint(-7, 7) for i in range(self._length)]
        m = 0
        start = choices([0, randint(0, self._length-3)], weights=[8, 1])[0]
        end = choices([self._length, randint(start+1, self._length)], weights=[9, 1])[0]
        elem_cnt = choices(dat+[median+5])[0]
        sign = choices(["<", "<=", ">", ">="])[0]
        inc = randint(1, 5)

        dat_init_pascal = ""
        dat_init_basic = ""
        dat_init_algo = ""
        dat_init_cpp = "{"
        dat_init_py = "["
        for num, d in enumerate(dat):
            dat_init_pascal += f"    Tok[{num+1}] := {d};" if num % 2 == 0 else f" Tok[{num+1}] := {d};\n"
            dat_init_basic += f"Tok({num+1}) = {d}:" if num % 2 == 0 else f" Tok({num+1}) = {d}\n"
            dat_init_algo += f"Tok[{num+1}] := {d}\n"
            if num == self._length-1:
                dat_init_cpp += f"{str(d)}}};"
                dat_init_py += f"{str(d)}]"
            else:
                dat_init_cpp += str(d)
                dat_init_py += str(d)
                if (num+1) == self._length//2:
                    dat_init_cpp += ",\n"
                    dat_init_py += ",\n           "
                else:
                    dat_init_cpp += ", "
                    dat_init_py += ", "

        prog_pascal = "var k, m: integer;\n"\
        f"Tok: array[1..{self._length}] of integer;\n"\
        "begin\n"
        prog_pascal += dat_init_pascal
        prog_pascal += f"    m := {m};\n"\
        f"    for k := {start+1} to {end} do\n"\
        f"        if Tok[k] {sign} {elem_cnt} then\n"\
        "        begin\n"\
        f"            m := m + {inc};\n"\
        "        end;\n"\
        "    writeln(m);\n"\
        "end.\n"

        prog_python = f"Tok = {dat_init_py}\n"\
        f"m = {m}\n"\
        f"for k in range({start}, {end}):\n"\
        f"    if Tok[k] {sign} {elem_cnt}:\n"\
        f"        m += {inc}\n"\
        f"print(m)\n"
        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int Tok[{self._length}] = {dat_init_cpp}\n"\
        f"    int m = {m};\n"\
        f"    for (int k = {start}; k < {end}; k++)\n"\
        f"        if (Tok[k] {sign} {elem_cnt}) m += {inc};\n"\
        "    cout << m;\n"\
        "    return 0;\n"\
        "}\n"

        prog_basic = f"DIM Tok({self._length}) AS INTEGER\n"\
        f"DIM k, m AS INTEGER\n"
        prog_basic += dat_init_basic
        prog_basic += f"m = {m}\n"\
        f"FOR k = {start+1} TO {end}\n"\
        f"IF Tok(k) {sign} {elem_cnt} THEN\n"\
        f"m = m + {inc}\n"\
        "END IF\n"\
        "NEXT k\n"\
        "PRINT m\n"

        prog_algo = "алг\n"\
        "нач\n"\
        f"целтаб Tok[1:{self._length}]\n"\
        "цел k, m\n"
        prog_algo += dat_init_algo
        prog_algo += f"m := {m}\n"\
        f"нц для k от {start+1} до {end}\n"\
        f"    если Tok[k] {sign} {elem_cnt} то\n"\
        f"        m := m + {inc}\n"\
        "    все\n"\
        "кц\n"\
        "вывод m\n"\
        "кон\n"


        table = "<table border='1' class='one-pager'>\n<tr><th name='qbasic'>Бейсик</th><th name='pascal'>Pascal</th><th name='algori'>Алгоритмический</th></tr>\n<tr>"
        table += f"<td name='qbasic'><pre>{prog_basic}</pre></td>"
        table += f"<td name='pascal'><pre>{prog_pascal}</pre></td>"
        table += f"<td name='algori'><pre>{prog_algo}</pre></td>"
        table += "\n</tr></table><table border='1'><tr><th name='python'>Python</th><th name='cpplus'>C++</th></tr>\n<tr>"
        table += f"<td name='python'><pre>{prog_python}</pre></td>"
        table += f"<td name='cpplus'><pre>{prog_cpp}</pre></td>"
        table += f"</tr>\n</table>"


        ldict = {}
        exec(prog_python[:-2].replace("print(", ""), globals(), ldict)
        self._answer = str(ldict["m"])
        self._table = table

    def question_text(self):
        return self.question.format(
            length=self._length,
            table=self._table
        )

    def question_answer(self):
        return self._answer

    def category(self):
        return "Другие алгоритмы"

    @property
    def max_qty(self):
        return 5000
    
    @property
    def get_subtype_num(self):
        return 1