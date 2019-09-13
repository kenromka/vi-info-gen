from .common import *
from random import randint
from ...tools.choices import choices

class Type0(Task6):
    """Формальное исполнение алгоритмов - программа"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Формальное исполнение алгоритмов - программа"
    
    @property
    def get_type_num(self):
        return 1
	
    def level(self):
        return "ez"


class SubtypeA(Type0):
    """Условный оператор"""
    def __init__(self):
        super().__init__()

        self.question = """
<p>Ниже приведена программа, записанная на пяти языках программирования.</p>
{table}
<p>Было проведено {launch_num} запусков программы, при которых в качестве значений переменных <i>{var1}</i> и <i>{var2}</i> вводились следующие пары чисел:
<br>
{numbers}
<br>
Сколько было запусков, при которых программа напечатала "{printed}"?</p>
        """


#============================================================================
        vars = 'abcdfgkmnptxyz'
        answers = ('ДА', 'НЕТ')
        signs = ('<', '<=', '>', '>=')
        bool_signs = ['and', 'or']

        var1 = choices(vars)[0]
        var2 = choices(list(set(vars)-set(var1)))[0]
#============================================================================
        printed = choices(answers)[0]
        launch_num = randint(7, 12)
        numbers = [(randint(-5, 15), randint(-5, 15)) for _ in range(launch_num)]

        sign = choices(signs, k=2)
        num = randint(-6, 12), randint(-6, 12)
        bool_sign = choices(bool_signs)[0]
#============================================================================
        cnt = 0
        for a, b in numbers:
            if eval(f'{a} {sign[0]} {num[0]} {bool_sign} {b} {sign[1]} {num[1]}'):
                cnt += 1
        

        prog_pascal = f"var {var1}, {var2}: integer;\n"\
        "begin\n"\
        f"    readln({var1});\n"\
        f"    readln({var2});\n"\
        f"    if ({var1} {sign[0]} {num[0]}) {bool_sign} ({var2} {sign[1]} {num[1]})\n"\
        f"        then writeln(\"ДА\")\n"\
        f"    else writeln(\"НЕТ\");\n"\
        "end.\n"

        prog_python = f"{var1} = int(input())\n"\
        f"{var2} = int(input())\n"\
        f"if {var1} {sign[0]} {num[0]} {bool_sign} {var2} {sign[1]} {num[1]}:\n"\
        f"    print(\"ДА\")\n"\
        f"else:\n"\
        f"    print(\"НЕТ\")\n"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {var1}, {var2};\n"\
        f"    cin >> {var1};\n"\
        f"    cin >> {var2};\n"\
        f"    if ({var1} {sign[0]} {num[0]} {'||' if bool_sign == 'or' else '&&'} {var2} {sign[1]} {num[1]})\n"\
        f"        cout << \"ДА\";\n"\
        f"    else\n"\
        f"        cout << \"НЕТ\";\n"\
        "    return 0;\n"\
        "}\n"

        prog_basic = f"DIM {var1}, {var2} AS INTEGER\n"\
        f"INPUT {var1}\n"\
        f"INPUT {var2}\n"\
        f"IF {var1} {sign[0]} {num[0]} {bool_sign.upper()} {var2} {sign[1]} {num[1]} THEN\n"\
        f"    PRINT 'ДА'\n"\
        f"ELSE\n"\
        f"    PRINT 'НЕТ'\n"\
        f"ENDIF\n"

        prog_algo = "алг\n"\
        "нач\n"\
        f"цел {var1}, {var2}\n"\
        f"ввод {var1}\n"\
        f"ввод {var2}\n"\
        f"если {var1} {sign[0]} {num[0]} {'или' if bool_sign == 'or' else 'и'} {var2} {sign[1]} {num[1]}\n"\
        f"    то вывод \"ДА\"\n"\
        f"    иначе вывод \"НЕТ\"\n"\
        "все\n"\
        "кон\n"


        table = "<table border='1' class='one-pager'>\n<tr><th name='qbasic'>Бейсик</th><th name='pascal'>Pascal</th><th name='algori'>Алгоритмический</th></tr>\n<tr>"
        table += f"<td name='qbasic'><pre>{prog_basic}</pre></td>"
        table += f"<td name='pascal'><pre>{prog_pascal}</pre></td>"
        table += f"<td name='algori'><pre>{prog_algo}</pre></td>"
        table += "\n</tr></table><table border='1'><tr><th name='python'>Python</th><th name='cpplus'>C++</th></tr>\n<tr>"
        table += f"<td name='python'><pre>{prog_python}</pre></td>"
        table += f"<td name='cpplus'><pre>{prog_cpp}</pre></td>"
        table += f"</tr>\n</table>"
        
        self._answer = cnt if printed == 'ДА' else len(numbers) - cnt

        self._table = table
        self._var1 = var1
        self._var2 = var2
        self._launch_num = launch_num
        self._printed = printed
        self._numbers = str(numbers)[1:-1]

    def question_text(self):
        return self.question.format(
            launch_num = self._launch_num,
            var1 = self._var1,
            var2 = self._var2,
            table = self._table,
            printed = self._printed,
            numbers = self._numbers
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Условный оператор"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
