from .common import *
from random import randint

class Type5(Task10):
    """Цикл for"""
    def __init__(self):
        super().__init__()
        var_cnt_names = ["i", "k", "n"]
        var_sum_names = ["s", "m", "t"]
        
        self._var_cnt_name = choices(var_cnt_names)[0]
        self._var_sum_name = choices(var_sum_names)[0]

        self.question = "Определите, что будет напечатано в результате работы следующей"\
        " программы. Текст программы приведён на пяти языках программирования.<br>{table}"
        
    def category(self):
        return "Анализ алгоритмов - Цикл for"
    
    @property
    def get_type_num(self):
        return 5
	
    def level(self):
        return "mid"

class SubtypeA(Type5):
    """Цикл for - сложение"""
    def __init__(self):
        super().__init__()
        diff = randint(4, 12)
        self._var_cnt_vals = [randint(0, 20)]
        self._var_cnt_vals.append(self._var_cnt_vals[0]+diff)
        self._var_sum_val = randint(0, 40)
        self._sum_item = randint(3, 12)

        prog_pascal = f"var {self._var_sum_name}, {self._var_cnt_name}: integer;\n"\
        "begin\n"\
        f"    {self._var_sum_name} := {self._var_sum_val};\n"\
        f"    for {self._var_cnt_name} := {self._var_cnt_vals[0]} to {self._var_cnt_vals[1]-1} do\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} + {self._sum_item};\n"\
        f"    writeln({self._var_sum_name});\n"\
        "end."

        prog_python = f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"for {self._var_cnt_name} in range({self._var_cnt_vals[0]}, {self._var_cnt_vals[1]}):\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} + {self._sum_item}\n"\
        f"print({self._var_sum_name})"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {self._var_sum_name} = {self._var_sum_val};\n"\
        f"    for (int {self._var_cnt_name} = {self._var_cnt_vals[0]}; {self._var_cnt_name} <= {self._var_cnt_vals[1]-1}; {self._var_cnt_name}++)\n"\
        f"        {self._var_sum_name} += {self._sum_item};\n"\
        f"    cout << {self._var_sum_name};\n"\
        "    return 0;\n"\
        "}"

        prog_basic = f"DIM {self._var_cnt_name}, {self._var_sum_name} AS INTEGER\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"FOR {self._var_cnt_name} = {self._var_cnt_vals[0]} TO {self._var_cnt_vals[1]-1}\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} + {self._sum_item}\n"\
        f"NEXT {self._var_cnt_name}\n"\
        f"PRINT {self._var_sum_name}"

        prog_algo = "алг\n"\
        "нач\n"\
        f"    цел {self._var_sum_name}, {self._var_cnt_name}\n"\
        f"    {self._var_sum_name} := {self._var_sum_val}\n"\
        f"    нц для {self._var_cnt_name} от {self._var_cnt_vals[0]} до {self._var_cnt_vals[1]-1}\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} + {self._sum_item}\n"\
        f"    кц\n"\
        f"    вывод {self._var_sum_name}\n"\
        "кон"


#------------------old table version----------------------
        """
        table = "<table border='1'>\n<tr><th name='qbasic'>Бейсик</th><th name='python'>Python</th></tr>\n<tr>"
        table += f"<td name='qbasic'><pre>{prog_basic}</pre></td>"
        table += f"<td name='python'><pre>{prog_python}</pre></td>"
        table += "\n</tr><tr><th name='pascal'>Pascal</th><th name='algori'>Алгоритмический</th></tr>\n<tr>"
        table += f"<td name='pascal'><pre>{prog_pascal}</pre></td>"
        table += f"<td name='algori'><pre>{prog_algo}</pre></td>"
        table += f"\n</tr><tr><th name='cpplus' colspan='2'>C++</th></tr>\n<tr><td name='cpplus' colspan='2'><pre>{prog_cpp}</pre></td></tr>\n</table>"
        """
#----------------------------------------------------------

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
        return "Цикл for - сложение"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000

class SubtypeB(Type5):
    """Цикл for - вычитание"""
    def __init__(self):
        super().__init__()
        diff = randint(4, 12)
        self._var_cnt_vals = [randint(0, 20)]
        self._var_cnt_vals.append(self._var_cnt_vals[0]+diff)
        self._var_sum_val = randint(0, 40)
        self._sum_item = randint(3, 12)

        prog_pascal = f"var {self._var_sum_name}, {self._var_cnt_name}: integer;\n"\
        "begin\n"\
        f"    {self._var_sum_name} := {self._var_sum_val};\n"\
        f"    for {self._var_cnt_name} := {self._var_cnt_vals[0]} to {self._var_cnt_vals[1]-1} do\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} - {self._sum_item};\n"\
        f"    writeln({self._var_sum_name});\n"\
        "end."

        prog_python = f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"for {self._var_cnt_name} in range({self._var_cnt_vals[0]}, {self._var_cnt_vals[1]}):\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} - {self._sum_item}\n"\
        f"print({self._var_sum_name})"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {self._var_sum_name} = {self._var_sum_val};\n"\
        f"    for (int {self._var_cnt_name} = {self._var_cnt_vals[0]}; {self._var_cnt_name} <= {self._var_cnt_vals[1]-1}; {self._var_cnt_name}++)\n"\
        f"        {self._var_sum_name} -= {self._sum_item};\n"\
        f"    cout << {self._var_sum_name};\n"\
        "    return 0;\n"\
        "}"

        prog_basic = f"DIM {self._var_cnt_name}, {self._var_sum_name} AS INTEGER\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"FOR {self._var_cnt_name} = {self._var_cnt_vals[0]} TO {self._var_cnt_vals[1]-1}\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} - {self._sum_item}\n"\
        f"NEXT {self._var_cnt_name}\n"\
        f"PRINT {self._var_sum_name}"

        prog_algo = "алг\n"\
        "нач\n"\
        f"    цел {self._var_sum_name}, {self._var_cnt_name}\n"\
        f"    {self._var_sum_name} := {self._var_sum_val}\n"\
        f"    нц для {self._var_cnt_name} от {self._var_cnt_vals[0]} до {self._var_cnt_vals[1]-1}\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} - {self._sum_item}\n"\
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
        return "Цикл for - вычитание"
    
    @property
    def get_subtype_num(self):
        return 2

    @property
    def max_qty(self):
        return 5000

class SubtypeC(Type5):
    """Цикл for - умножение"""
    def __init__(self):
        super().__init__()
        diff = randint(2, 5)
        self._var_cnt_vals = [randint(0, 20)]
        self._var_cnt_vals.append(self._var_cnt_vals[0]+diff)
        self._var_sum_val = 1
        self._sum_item = randint(2, 3)

        prog_pascal = f"var {self._var_sum_name}, {self._var_cnt_name}: integer;\n"\
        "begin\n"\
        f"    {self._var_sum_name} := {self._var_sum_val};\n"\
        f"    for {self._var_cnt_name} := {self._var_cnt_vals[0]} to {self._var_cnt_vals[1]-1} do\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} * {self._sum_item};\n"\
        f"    writeln({self._var_sum_name});\n"\
        "end."

        prog_python = f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"for {self._var_cnt_name} in range({self._var_cnt_vals[0]}, {self._var_cnt_vals[1]}):\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} * {self._sum_item}\n"\
        f"print({self._var_sum_name})"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {self._var_sum_name} = {self._var_sum_val};\n"\
        f"    for (int {self._var_cnt_name} = {self._var_cnt_vals[0]}; {self._var_cnt_name} <= {self._var_cnt_vals[1]-1}; {self._var_cnt_name}++)\n"\
        f"        {self._var_sum_name} = {self._var_sum_name} * {self._sum_item};\n"\
        f"    cout << {self._var_sum_name};\n"\
        "    return 0;\n"\
        "}"

        prog_basic = f"DIM {self._var_cnt_name}, {self._var_sum_name} AS INTEGER\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"FOR {self._var_cnt_name} = {self._var_cnt_vals[0]} TO {self._var_cnt_vals[1]-1}\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} * {self._sum_item}\n"\
        f"NEXT {self._var_cnt_name}\n"\
        f"PRINT {self._var_sum_name}"

        prog_algo = "алг\n"\
        "нач\n"\
        f"    цел {self._var_sum_name}, {self._var_cnt_name}\n"\
        f"    {self._var_sum_name} := {self._var_sum_val}\n"\
        f"    нц для {self._var_cnt_name} от {self._var_cnt_vals[0]} до {self._var_cnt_vals[1]-1}\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} * {self._sum_item}\n"\
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
        return "Цикл for - умножение"
    
    def level(self):
        return "mid"
    
    @property
    def get_subtype_num(self):
        return 3

    @property
    def max_qty(self):
        return 1440 #160

class SubtypeD(Type5):
    """Цикл for - возведение в степень"""
    def __init__(self):
        super().__init__()
        diff = randint(2, 3)
        self._var_cnt_vals = [randint(0, 20)]
        self._var_cnt_vals.append(self._var_cnt_vals[0]+diff)
        self._var_sum_val = 2

        prog_pascal = f"var {self._var_sum_name}, {self._var_cnt_name}: integer;\n"\
        "begin\n"\
        f"    {self._var_sum_name} := {self._var_sum_val};\n"\
        f"    for {self._var_cnt_name} := {self._var_cnt_vals[0]} to {self._var_cnt_vals[1]-1} do\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} * {self._var_sum_name};\n"\
        f"    writeln({self._var_sum_name});\n"\
        "end."

        prog_python = f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"for {self._var_cnt_name} in range({self._var_cnt_vals[0]}, {self._var_cnt_vals[1]}):\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} * {self._var_sum_name}\n"\
        f"print({self._var_sum_name})"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {self._var_sum_name} = {self._var_sum_val};\n"\
        f"    for (int {self._var_cnt_name} = {self._var_cnt_vals[0]}; {self._var_cnt_name} <= {self._var_cnt_vals[1]-1}; {self._var_cnt_name}++)\n"\
        f"        {self._var_sum_name} = {self._var_sum_name} * {self._var_sum_name};\n"\
        f"    cout << {self._var_sum_name};\n"\
        "    return 0;\n"\
        "}"

        prog_basic = f"DIM {self._var_cnt_name}, {self._var_sum_name} AS INTEGER\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"FOR {self._var_cnt_name} = {self._var_cnt_vals[0]} TO {self._var_cnt_vals[1]-1}\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} * {self._var_sum_name}\n"\
        f"NEXT {self._var_cnt_name}\n"\
        f"PRINT {self._var_sum_name}"

        prog_algo = "алг\n"\
        "нач\n"\
        f"    цел {self._var_sum_name}, {self._var_cnt_name}\n"\
        f"    {self._var_sum_name} := {self._var_sum_val}\n"\
        f"    нц для {self._var_cnt_name} от {self._var_cnt_vals[0]} до {self._var_cnt_vals[1]-1}\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} * {self._var_sum_name}\n"\
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
        return "Цикл for - возведение в степень"
    
    def level(self):
        return "mid"
    
    @property
    def get_subtype_num(self):
        return 4

    @property
    def max_qty(self):
        return 360 #40

class SubtypeE(Type5):
    """Цикл for - сложение + умножение"""
    def __init__(self):
        super().__init__()
        diff = randint(2, 5)
        self._var_cnt_vals = [randint(1, 5)]
        self._var_cnt_vals.append(self._var_cnt_vals[0]+diff)
        self._var_sum_val = 0
        self._sum_item = randint(2, 4)

        prog_pascal = f"var {self._var_sum_name}, {self._var_cnt_name}: integer;\n"\
        "begin\n"\
        f"    {self._var_sum_name} := {self._var_sum_val};\n"\
        f"    for {self._var_cnt_name} := {self._var_cnt_vals[0]} to {self._var_cnt_vals[1]-1} do\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name};\n"\
        f"    writeln({self._var_sum_name});\n"\
        "end."

        prog_python = f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"for {self._var_cnt_name} in range({self._var_cnt_vals[0]}, {self._var_cnt_vals[1]}):\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name}\n"\
        f"print({self._var_sum_name})"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {self._var_sum_name} = {self._var_sum_val};\n"\
        f"    for (int {self._var_cnt_name} = {self._var_cnt_vals[0]}; {self._var_cnt_name} <= {self._var_cnt_vals[1]-1}; {self._var_cnt_name}++)\n"\
        f"        {self._var_sum_name} = {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name};\n"\
        f"    cout << {self._var_sum_name};\n"\
        "    return 0;\n"\
        "}"

        prog_basic = f"DIM {self._var_cnt_name}, {self._var_sum_name} AS INTEGER\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"FOR {self._var_cnt_name} = {self._var_cnt_vals[0]} TO {self._var_cnt_vals[1]-1}\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name}\n"\
        f"NEXT {self._var_cnt_name}\n"\
        f"PRINT {self._var_sum_name}"

        prog_algo = "алг\n"\
        "нач\n"\
        f"    цел {self._var_sum_name}, {self._var_cnt_name}\n"\
        f"    {self._var_sum_name} := {self._var_sum_val}\n"\
        f"    нц для {self._var_cnt_name} от {self._var_cnt_vals[0]} до {self._var_cnt_vals[1]-1}\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name}\n"\
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
        return "Цикл for - сложение + умножение"
    
    def level(self):
        return "hard"
    
    @property
    def get_subtype_num(self):
        return 5

    @property
    def max_qty(self):
        return 540 #60

class SubtypeF(Type5):
    """Цикл for - downto"""
    def __init__(self):
        super().__init__()
        diff = randint(2, 5)
        self._var_cnt_vals = [randint(1, 5)]
        self._var_cnt_vals.append(self._var_cnt_vals[0]+diff)
        self._var_sum_val = 0
        self._sum_item = randint(2, 4)

        prog_pascal = f"var {self._var_sum_name}, {self._var_cnt_name}: integer;\n"\
        "begin\n"\
        f"    {self._var_sum_name} := {self._var_sum_val};\n"\
        f"    for {self._var_cnt_name} := {self._var_cnt_vals[1]-1} downto {self._var_cnt_vals[0]} do\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name};\n"\
        f"    writeln({self._var_sum_name});\n"\
        "end."

        prog_python = f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"for {self._var_cnt_name} in range({self._var_cnt_vals[1]-1}, {self._var_cnt_vals[0]-1}, -1):\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name}\n"\
        f"print({self._var_sum_name})"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {self._var_sum_name} = {self._var_sum_val};\n"\
        f"    for (int {self._var_cnt_name} = {self._var_cnt_vals[1]-1}; {self._var_cnt_name} >= {self._var_cnt_vals[0]}; {self._var_cnt_name}--)\n"\
        f"        {self._var_sum_name} = {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name};\n"\
        f"    cout << {self._var_sum_name};\n"\
        "    return 0;\n"\
        "}"

        prog_basic = f"DIM {self._var_cnt_name}, {self._var_sum_name} AS INTEGER\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"FOR {self._var_cnt_name} = {self._var_cnt_vals[1]-1} TO {self._var_cnt_vals[0]} "\
        "STEP -1\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name}\n"\
        f"NEXT {self._var_cnt_name}\n"\
        f"PRINT {self._var_sum_name}"

        prog_algo = "алг\n"\
        "нач\n"\
        f"    цел {self._var_sum_name}, {self._var_cnt_name}\n"\
        f"    {self._var_sum_name} := {self._var_sum_val}\n"\
        f"    нц для {self._var_cnt_name} от {self._var_cnt_vals[1]-1} до {self._var_cnt_vals[0]} "\
        "шаг -1\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} + {self._sum_item} * {self._var_cnt_name}\n"\
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
        return "Цикл for - downto"
    
    def level(self):
        return "hard"
    
    @property
    def get_subtype_num(self):
        return 6

    @property
    def max_qty(self):
        return 540 #60

class SubtypeG(Type5):
    """Цикл for - вычисления перед циклом"""
    def __init__(self):
        super().__init__()
        diff = randint(2, 5)
        self._var_cnt_vals = [randint(1, 5)]
        self._var_cnt_vals.append(self._var_cnt_vals[0]+diff)
        self._var_sum_val = randint(1, 5)
        self._prod_item = randint(2, 5)

        prog_pascal = f"var {self._var_sum_name}, {self._var_cnt_name}: integer;\n"\
        "begin\n"\
        f"    {self._var_sum_name} := {self._var_sum_val};\n"\
        f"    {self._var_sum_name} := {self._var_sum_name} * {self._prod_item};\n"\
        f"    for {self._var_cnt_name} := {self._var_cnt_vals[0]} to {self._var_cnt_vals[1]-1} do\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} + {self._var_cnt_name};\n"\
        f"    writeln({self._var_sum_name});\n"\
        "end."

        prog_python = f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"{self._var_sum_name} = {self._var_sum_name} * {self._prod_item}\n"\
        f"for {self._var_cnt_name} in range({self._var_cnt_vals[0]}, {self._var_cnt_vals[1]}):\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} + {self._var_cnt_name}\n"\
        f"print({self._var_sum_name})"

        prog_cpp = "#include &lt;iostream&gt;\n"\
        "using namespace std;\n"\
        "int main() {\n"\
        f"    int {self._var_sum_name} = {self._var_sum_val};\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} * {self._prod_item};\n"\
        f"    for (int {self._var_cnt_name} = {self._var_cnt_vals[0]}; {self._var_cnt_name} <= {self._var_cnt_vals[1]-1}; {self._var_cnt_name}++)\n"\
        f"        {self._var_sum_name} += {self._var_cnt_name};\n"\
        f"    cout << {self._var_sum_name};\n"\
        "    return 0;\n"\
        "}"

        prog_basic = f"DIM {self._var_cnt_name}, {self._var_sum_name} AS INTEGER\n"\
        f"{self._var_sum_name} = {self._var_sum_val}\n"\
        f"{self._var_sum_name} = {self._var_sum_name} * {self._prod_item}\n"\
        f"FOR {self._var_cnt_name} = {self._var_cnt_vals[0]} TO {self._var_cnt_vals[1]-1}\n"\
        f"    {self._var_sum_name} = {self._var_sum_name} + {self._var_cnt_name}\n"\
        f"NEXT {self._var_cnt_name}\n"\
        f"PRINT {self._var_sum_name}"

        prog_algo = "алг\n"\
        "нач\n"\
        f"    цел {self._var_sum_name}, {self._var_cnt_name}\n"\
        f"    {self._var_sum_name} := {self._var_sum_val}\n"\
        f"    {self._var_sum_name} := {self._var_sum_name} * {self._prod_item}\n"\
        f"    нц для {self._var_cnt_name} от {self._var_cnt_vals[0]} до {self._var_cnt_vals[1]-1}\n"\
        f"        {self._var_sum_name} := {self._var_sum_name} + {self._var_cnt_name}\n"\
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
        return "Цикл for - вычисления перед циклом"
    
    def level(self):
        return "mid"
    
    @property
    def get_subtype_num(self):
        return 7

    @property
    def max_qty(self):
        return 3600 #400