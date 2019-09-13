from .common import *
from random import randint

class Type6(Task10Old):
    """Цикл while"""
    def __init__(self):
        super().__init__()
        var_sum_names = ["i", "k", "n"]
        var_cnt_names = ["s", "m", "t"]
        
        self._var_cnt_name = choices(var_cnt_names)[0]
        self._var_sum_name = choices(var_sum_names)[0]

        self.question = "Определите, что будет напечатано в результате работы следующей"\
        " программы. Текст программы приведён на пяти языках программирования.{table}"
        
    def category(self):
        return "Анализ алгоритмов - Цикл while"
    
    @property
    def get_type_num(self):
        return 6
    
    def level(self):
        return "mid"

class SubtypeA(Type6):
    """Цикл while"""
    def __init__(self):
        super().__init__()
        diff = randint(-20, 20)
        while diff == 0:
            diff = randint(-20, 20)
        times = randint(3, 11)
        self._var_cnt_vals = [randint(0, 100)]
        self._var_sum_val = randint(0, 100)
        self._sum_item = randint(-9, 9)
        while self._sum_item == 0:
            self._sum_item = randint(-9, 9)

        sign_func = lambda a: "-" if a < 0 else "+" 

        if diff > 0:
            sign = choices(["<", "<="])[0]
            if sign == "<":
                self._var_cnt_vals.append(self._var_cnt_vals[0] + diff * times)
            else:
                self._var_cnt_vals.append(self._var_cnt_vals[0] + diff * (times - 1))
        else:
            sign = choices([">", ">="])[0]
            if sign == ">":
                self._var_cnt_vals.append(self._var_cnt_vals[0] - diff * times)
            else:
                self._var_cnt_vals.append(self._var_cnt_vals[0] - diff * (times - 1))

        prog_pascal = f"var {self._var_sum_name}, {self._var_cnt_name}: integer;\n"\
        "begin\n"\
        f"    {self._var_cnt_name} := {self._var_cnt_vals[0]};\n"\
        f"    {self._var_sum_name} := {self._var_sum_val};\n"\
        f"    while {self._var_cnt_name} {sign} {self._var_cnt_vals[1]} do\n"\
        f"    begin\n"\
        f"        {self._var_cnt_name} := {self._var_cnt_name} {sign_func(diff)} {abs(diff)};\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} {sign_func(self._sum_item)} {abs(self._sum_item)};\n"\
        f"    end;\n"\
        f"    writeln({self._var_sum_name});\n"\
        "end."

        prog_python = f"{self._var_cnt_name} = {self._var_cnt_vals[0]}\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"while {self._var_cnt_name} {sign} {self._var_cnt_vals[1]}:\n"\
        f"    {self._var_cnt_name} {sign_func(diff)}= {abs(diff)}\n"\
        f"    {self._var_sum_name} {sign_func(self._sum_item)}= {abs(self._sum_item)}\n"\
        f"print({self._var_sum_name})"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {self._var_cnt_name} = {self._var_cnt_vals[0]};\n"\
        f"    int {self._var_sum_name} = {self._var_sum_val};\n"\
        f"    while ({self._var_cnt_name} {sign} {self._var_cnt_vals[1]}) {{\n"\
        f"        {self._var_cnt_name} {sign_func(diff)}= {abs(diff)};\n"\
        f"        {self._var_sum_name} {sign_func(self._sum_item)}= {abs(self._sum_item)};\n"\
        "     }\n"\
        f"    cout << {self._var_sum_name};\n"\
        "    return 0;\n"\
        "}"

        prog_basic = f"DIM {self._var_cnt_name}, {self._var_sum_name} AS INTEGER\n"\
        f"{self._var_cnt_name} = {self._var_cnt_vals[0]}\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"WHILE {self._var_cnt_name} {sign} {self._var_cnt_vals[1]}\n"\
        f"    {self._var_cnt_name} = {self._var_cnt_name} {sign_func(diff)} {abs(diff)}\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} {sign_func(self._sum_item)} {abs(self._sum_item)}\n"\
        f"WEND\n"\
        f"PRINT {self._var_sum_name}"

        prog_algo = "алг\n"\
        "нач\n"\
        f"    цел {self._var_sum_name}, {self._var_cnt_name}\n"\
        f"    {self._var_cnt_name} := {self._var_cnt_vals[0]}\n"\
        f"    {self._var_sum_name} := {self._var_sum_val}\n"\
        f"    нц пока {self._var_cnt_name}{sign}{self._var_cnt_vals[1]}\n"\
        f"        {self._var_cnt_name} := {self._var_cnt_name} {sign_func(diff)} {abs(diff)}\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} {sign_func(self._sum_item)} {abs(self._sum_item)}\n"\
        f"    кц\n"\
        f"    вывод {self._var_sum_name}\n"\
        "кон"

        table = "<table border='1' class='one-pager'>\n<tr><th name='qbasic' colspan='2'>Бейсик</th>"\
        "<th name='pascal' colspan='2'>Pascal</th><th name='algori' colspan='2'>Python</th></tr>\n<tr>"
        table += f"<td name='qbasic' colspan='2'><pre>{prog_basic}</pre></td>"
        table += f"<td name='pascal' colspan='2'><pre>{prog_pascal}</pre></td>"
        table += f"<td name='python' colspan='2'><pre>{prog_python}</pre></td>"
        table += "\n</tr><tr><th name='python' colspan='3'>Алгоритмический</th>"\
        "<th name='cpplus' colspan='3'>C++</th></tr>\n<tr>"
        table += f"<td name='algori' colspan='3'><pre>{prog_algo}</pre></td>"
        table += f"<td name='cpplus' colspan='3'><pre>{prog_cpp}</pre></td>"
        table += f"</tr>\n</table>"


        exec(prog_python[:-1].replace("print(", ""))
        self._answer = str(eval(self._var_sum_name))
        self._table = table

    def question_text(self):
        return self.question.format(
            table=self._table
        )

    def question_answer(self):
        return self._answer

    def category(self):
        return "Цикл while"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000