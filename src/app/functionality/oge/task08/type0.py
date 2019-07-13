from .common import *
from random import randint, sample, shuffle, random
from sympy import divisors as divs
from copy import copy
from re import search, finditer

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

class Type0(Task8):
    """Программирование. Линейный алгоритм"""
    def __init__(self):
        super().__init__()
        self.question = "В программе «:=» обозначает оператор присваивания, знаки «+», «–», «*» и «/» – "\
        "соответственно операции сложения, вычитания, умножения и деления. {xtra_condition} "\
        "Правила выполнения операций и порядок действий соответствуют правилам арифметики. Переменные <i>a</i>"\
        " и <i>b</i> - целочисленные.\n"\
        "Определите значение переменной <code>{target}</code> после выполнения данного алгоритма:\n"\
        "<pre>{code}</pre>"\
        "<p>В ответе укажите одно целое число – значение переменной <code>{target}</code>.</p>"

    def category(self):
        return "Линейный алгоритм"

class SubtypeA(Type0):
    """Арифметические операции"""
    def __init__(self):
        super().__init__()
        self._xtra_condition = ""
        code =  "a := {a}\n"\
                "b := {b}\n"\
                "a := {expr1}\n"\
                "b := {expr2}"
        targs = ["a", "b", "b", "b", "b", "b"]
        self._target = choices(targs)[0]

        def generate_expression(scope, bins):
            PROP_PARANTHESIS = .3
            scope = list(scope)
            shuffle(scope)
            ex = choices(bins)[0] % (scope[0], scope[1])
            if random() < PROP_PARANTHESIS:
                ex = "(%s)" % ex
            ex = choices(bins)[0] % (ex, scope[2])
            return ex

        self._answer = "1001"
        while abs(int(self._answer)) > 1000:
            try:
                scope = ["a", "b", "c"]
                binaries = ["%s + %s", "%s - %s", "%s * %s", "%s / %s"]
                #########################################################
                #========================EXPR 1=========================#
                #########################################################

                expr1 = generate_expression(scope, binaries)
                if expr1.count("/") == 2 and expr1.count(")") == 0:
                    if random() < .5:
                        expr1 = f"({expr1[:5]}) / {expr1[-1]}"
                    else:
                        expr1 = f"{expr1[0]} / ({expr1[-5:]})"

                divisors = search(r'(\(+[^)]+\)+|[^ (]+) \/ (\(+[^)]+\)+|[^ )]+)', expr1)
                multipls = search(r'(\(+[^)]+\)+|[^ (]+) \* (\(+[^)]+\)+|[^ )]+)', expr1)

                ldict = {}
                a = None
                b = None
                c = None

                if divisors:
                    if "(" in divisors[0]:
                        if "(" in divisors[1]:
                            exec(f"{divisors[2]} = {randint(2, 10)}", globals(), ldict)
                            prod = randint(2, 10) * eval(divisors[2], globals(), ldict)
                            if "/" in divisors[1]:
                                x2 = randint(2, 4)
                                x1 = x2 * prod
                            elif "*" in divisors[1]:
                                x1 = choices(divs(prod))[0]
                                x2 = prod // x1
                            else:
                                if divisors[1][3] == "+":
                                    x1 = randint(2, prod - 1)
                                    x2 = prod - x1
                                else:
                                    x1 = randint(prod + 1, prod + 15)
                                    x2 = x1 - prod
                            exec(f"{divisors[1][1]} = {x1}", globals(), ldict)
                            exec(f"{divisors[1][-2]} = {x2}", globals(), ldict)
                        else:
                            if "/" in divisors[2]:
                                x2 = randint(2, 10)
                                x1 = x2 * randint(2, 10)
                            elif "*" in divisors[2]:
                                x1 = randint(2, 20)
                                x2 = randint(2, 5)
                            else:
                                x1 = randint(2, 99)
                                x2 = randint(2, 39)
                            exec(f"{divisors[2][1]} = {x1}", globals(), ldict)
                            exec(f"{divisors[2][-2]} = {x2}", globals(), ldict)
                            prod = randint(2, 10) * eval(divisors[2], globals(), ldict)
                            exec(f"{divisors[1]} = {prod}", globals(), ldict)
                    else:
                        exec(f"{divisors[2]} = {randint(2, 10)}", globals(), ldict)
                        exec(f"{divisors[1]} = {divisors[2]}*{randint(2, 10)}", globals(), ldict)
                        if "*" in expr1:
                            x1 = randint(2, 20)
                        else:
                            x1 = randint(2, 46)
                        if not ldict.get("a", None):
                            ldict["a"] = x1
                        elif not ldict.get("b", None):
                            ldict["b"] = x1
                        else:
                            ldict["c"] = x1

                elif multipls:
                    if "(" in multipls[0]:
                        if "(" in multipls[1]:
                            mult1 = multipls[1]
                            mult2 = multipls[2]
                        else:
                            mult1 = multipls[2]
                            mult2 = multipls[1]
                        
                        exec(f"{mult2} = {randint(2, 20)}", globals(), ldict)
                        if "*" in mult2:
                            x1 = randint(2, 10)
                            x2 = randint(2, 10)
                        else:
                            x1 = randint(2, 20)
                            x2 = randint(2, 20)
                        exec(f"{mult1[1]} = {x1}", globals(), ldict)
                        exec(f"{mult1[-2]} = {x2}", globals(), ldict)
                    else:
                        exec(f"{multipls[1]} = {randint(2, 20)}", globals(), ldict)
                        exec(f"{multipls[2]} = {randint(2, 20)}", globals(), ldict)
                        if expr1.count("*") == 2:
                            x1 = randint(2, 20)
                        else:
                            x1 = randint(2, 99)
                        if not ldict.get("a", None):
                            ldict["a"] = x1
                        elif not ldict.get("b", None):
                            ldict["b"] = x1
                        else:
                            ldict["c"] = x1
                else:
                    ldict["a"] = randint(2, 59)
                    ldict["b"] = randint(2, 39)
                    ldict["c"] = randint(2, 79)

                if not a:
                    a = int(ldict["a"])
                if not b:
                    b = int(ldict["b"])
                if not c:
                    c = int(ldict["c"])

                self._a = a

                #########################################################
                #========================EXPR 2=========================#
                #########################################################
                a = eval(expr1.replace("/", "//"))
                d = randint(2, 10)
                check_vals_a = {b: "b", d: "d", b+d: "b + d", b-d: "b - d", b*d: "b * d", d-b: "d - b"}
                check_vals_b = {a: "a", d: "d", a+d: "a + d", a-d: "a - d", a*d: "a * d", d-a: "d - a"}
                check_vals_c = {b: "b", a: "a", b+a: "b + a", b-a: "b - a", b*a: "b * a", a-b: "a - b"}

                intersec_a = list(set(divs(a)[1:]) & set(check_vals_a.keys()))
                intersec_b = list(set(divs(b)[1:]) & set(check_vals_b.keys()))
                intersec_c = list(set(divs(d)[1:]) & set(check_vals_c.keys()))

                prob = random() < 0.8

                if intersec_a and prob:
                    x2 = choices(intersec_a)[0]
                    if len(check_vals_a[x2]) > 1:
                        expr2 = f"a / ({check_vals_a[x2]})"
                    else:
                        expr2 = f"a / {check_vals_a[x2]}"
                        if check_vals_a[x2] == "b":
                            x1 = "d"
                        else:
                            x1 = "b"
                        sign = choices(["+", "-", "*"])[0]
                        if random() < .5 and sign != "*":
                            expr2 = f"{x1} {sign} {expr2}"
                        else:
                            expr2 = f"{expr2} {sign} {x1}"
                elif intersec_b and prob:
                    x2 = choices(intersec_b)[0]
                    if len(check_vals_b[x2]) > 1:
                        expr2 = f"b / ({check_vals_b[x2]})"
                    else:
                        expr2 = f"b / {check_vals_b[x2]}"
                        if check_vals_b[x2] == "a":
                            x1 = "d"
                        else:
                            x1 = "a"
                        sign = choices(["+", "-", "*"])[0]
                        if random() < .5 and sign != "*":
                            expr2 = f"{x1} {sign} {expr2}"
                        else:
                            expr2 = f"{expr2} {sign} {x1}"
                elif intersec_c and prob:
                    x2 = choices(intersec_c)[0]
                    if len(check_vals_c[x2]) > 1:
                        expr2 = f"d / ({check_vals_c[x2]})"
                    else:
                        expr2 = f"d / {check_vals_c[x2]}"
                        if check_vals_c[x2] == "a":
                            x1 = "b"
                        else:
                            x1 = "a"
                        sign = choices(["+", "-", "*"])[0]
                        if random() < .5 and sign != "*":
                            expr2 = f"{x1} {sign} {expr2}"
                        else:
                            expr2 = f"{expr2} {sign} {x1}"
                else:
                    scope = ["a", "b", "d"]
                    binaries = ["%s + %s", "%s - %s", "%s * %s"]
                    expr2 = generate_expression(scope, binaries)

                self._code = code.format(
                    a=self._a,
                    b=b,
                    expr1=expr1.replace("c", str(c)),
                    expr2=expr2.replace("d", str(d))
                )
                if self._target == "a":
                    a = self._a
                    self._answer = "{:.0f}".format(eval(expr1.replace("/", "//")))
                else:
                    self._answer = "{:.0f}".format(eval(expr2.replace("/", "//")))
            except Exception as e:
                print(e)
                continue

    def level(self):
        return "ez"

    def category(self):
        return "Арифметические операции"

    def question_text(self):
        return self.question.format(
            xtra_condition=self._xtra_condition, 
            target=self._target,
            code=self._code
        )

    def question_answer(self):
        return self._answer

    @property
    def max_qty(self):
        return 5000


class SubtypeB(Type0):
    """ Целочисленное деление """
    def __init__(self):
        super().__init__()
        self._xtra_condition = "Выражение x mod y означает остаток от деления числа x на число y, а выражение x div y означает целую часть результата деления числа x на число y."
        code =  "a := {a}\n"\
                "b := {b}\n"\
                "a := {expr1}\n"\
                "b := {expr2}"

        targs = ["a", "b", "b", "b", "b", "b"]
        self._target = choices(targs)[0]
        self._code = code

        def generate_expression(scope, bins):
            PROP_PARANTHESIS = .3
            scope = list(scope)
            shuffle(scope)
            ex = choices(bins)[0] % (scope[0], scope[1])
            if random() < PROP_PARANTHESIS:
                ex = "(%s)" % ex
            ex = choices(bins)[0] % (ex, scope[2])
            return ex

        self._answer = "1001"
        self._aa = -1
        while abs(int(self._answer)) > 1000 or self._aa <= 0 or ("div" not in self._code and "mod" not in self._code):
            try:
                scope = ["a", "b", "c"]
                binaries = ["%s + %s", "%s - %s", "%s * %s", "%s / %s", "%s mod %s", "%s div %s"]
                #########################################################
                #========================EXPR 1=========================#
                #########################################################

                expr1 = generate_expression(scope, binaries)
                if expr1.count("/") == 2 and expr1.count(")") == 0:
                    if random() < .5:
                        expr1 = f"({expr1[:5]}) / {expr1[-1]}"
                    else:
                        expr1 = f"{expr1[0]} / ({expr1[-5:]})"

                divisors = search(r'(\(+[^)]+\)+|[^ (]+) \/ (\(+[^)]+\)+|[^ )]+)', expr1)
                multipls = search(r'(\(+[^)]+\)+|[^ (]+) \* (\(+[^)]+\)+|[^ )]+)', expr1)

                ldict = {}
                a = None
                b = None
                c = None

                if divisors:
                    if "(" in divisors[0]:
                        if "(" in divisors[1]:
                            exec(f"{divisors[2]} = {randint(2, 10)}", globals(), ldict)
                            prod = randint(2, 10) * eval(divisors[2].replace("div", "//").replace("mod", "%"), globals(), ldict)
                            if "/" in divisors[1]:
                                x2 = randint(2, 4)
                                x1 = x2 * prod
                            elif "div" in divisors[1]:
                                x2 = randint(2, 5)
                                x1 = x2 * prod + randint(0, x2-1)
                            elif "mod" in divisors[1]:
                                x2 = randint(prod+1, prod+5)
                                x1 = x2 * randint(1, 3) + prod
                            elif "*" in divisors[1]:
                                x1 = choices(divs(prod))[0]
                                x2 = prod // x1
                            else:
                                if divisors[1][3] == "+":
                                    x1 = randint(2, prod - 1)
                                    x2 = prod - x1
                                else:
                                    x1 = randint(prod + 1, prod + 15)
                                    x2 = x1 - prod
                            exec(f"{divisors[1][1]} = {x1}", globals(), ldict)
                            exec(f"{divisors[1][-2]} = {x2}", globals(), ldict)
                        else:
                            if "/" in divisors[2]:
                                x2 = randint(2, 10)
                                x1 = x2 * randint(2, 10)
                            elif "div" in divisors[2]:
                                x2 = randint(2, 10)
                                x1 = x2 * randint(2, 8) + randint(0, x2-1)
                            elif "mod" in divisors[2]:
                                x2 = randint(2, 10)
                                x1 = x2 * randint(1, 3) + randint(2, 7)
                            elif "*" in divisors[2]:
                                x1 = randint(2, 20)
                                x2 = randint(2, 5)
                            else:
                                x1 = randint(2, 99)
                                x2 = randint(2, 39)
                            exec(f"{divisors[2][1]} = {x1}", globals(), ldict)
                            exec(f"{divisors[2][-2]} = {x2}", globals(), ldict)
                            prod = randint(2, 10) * eval(divisors[2].replace("div", "//").replace("mod", "%"), globals(), ldict)
                            exec(f"{divisors[1]} = {prod}", globals(), ldict)
                    else:
                        if expr1[2:].startswith("div"):
                            x2 = randint(2, 10)
                            x1 = x2 * randint(2, 8) + randint(0, x2-1)
                            exec(f"{expr1[0]} = {x1}", globals(), ldict)
                            exec(f"{divisors[1]} = {x2}", globals(), ldict)
                            res = choices(divs(x1 // x2))[0]
                            exec(f"{divisors[2]} = {res}", globals(), ldict)
                        elif expr1[2:].startswith("mod"):
                            x2 = randint(2, 10)
                            x1 = x2 * randint(1, 3) + randint(2, 7)
                            exec(f"{expr1[0]} = {x1}", globals(), ldict)
                            exec(f"{divisors[1]} = {x2}", globals(), ldict)
                            res = choices(divs(x1 % x2))
                            res = randint(2, 34) if not res else res[0]
                            exec(f"{divisors[2]} = {res}", globals(), ldict)
                        else:
                            exec(f"{divisors[2]} = {randint(2, 10)}", globals(), ldict)
                            exec(f"{divisors[1]} = {divisors[2]}*{randint(2, 10)}", globals(), ldict)
                            if "*" in expr1:
                                x1 = randint(2, 20)
                            elif "div" in expr1:
                                divr = choices(divs(eval(f"{divisors[1]} // {divisors[2]}", globals(), ldict))[1:])[0]
                                x1 = divr - randint(0, divr - 1) + 1
                            elif "mod" in expr1:
                                divr = choices(divs(eval(f"{divisors[1]} // {divisors[2]}", globals(), ldict))[1:])[0]
                                x1 = divr - randint(0, divr - 1) + 1
                            else:
                                x1 = randint(2, 46)
                            if not ldict.get("a", None):
                                ldict["a"] = x1
                            elif not ldict.get("b", None):
                                ldict["b"] = x1
                            else:
                                ldict["c"] = x1

                elif multipls:
                    if "(" in multipls[0]:
                        if "(" in multipls[1]:
                            mult1 = multipls[1]
                            mult2 = multipls[2]
                        else:
                            mult1 = multipls[2]
                            mult2 = multipls[1]
                        
                        exec(f"{mult2} = {randint(2, 20)}", globals(), ldict)
                        if "*" in mult2:
                            x1 = randint(2, 10)
                            x2 = randint(2, 10)
                        elif "div" in mult1:
                            x2 = randint(2, 5)
                            x1 = x2 * randint(1, 6) + randint(0, x2-1)
                        elif "mod" in mult1:
                            x2 = randint(2, 10)
                            x1 = x2 * randint(1, 3) + randint(0, x2-1)
                        else:
                            x1 = randint(2, 20)
                            x2 = randint(2, 20)
                        exec(f"{mult1[1]} = {x1}", globals(), ldict)
                        exec(f"{mult1[-2]} = {x2}", globals(), ldict)
                    else:
                        exec(f"{multipls[1]} = {randint(2, 20)}", globals(), ldict)
                        exec(f"{multipls[2]} = {randint(2, 20)}", globals(), ldict)
                        if expr1.count("*") == 2:
                            x1 = randint(2, 20)
                        elif "div" in expr1:
                            x1 = randint(2, min(eval(f"{multipls[1]}", globals(), ldict), eval(f"{multipls[2]}", globals(), ldict)))
                        elif "mod" in expr1:
                            x1 = randint(2, min(eval(f"{multipls[1]}", globals(), ldict), eval(f"{multipls[2]}", globals(), ldict)))
                        else:
                            x1 = randint(2, 99)
                        if not ldict.get("a", None):
                            ldict["a"] = x1
                        elif not ldict.get("b", None):
                            ldict["b"] = x1
                        else:
                            ldict["c"] = x1
                else:
                    if "div" in expr1:
                        ddiv = search(r'(\(+[^)]+\)+|[^ (]+) div (\(+[^)]+\)+|[^ )]+)', expr1)
                        if "(" in ddiv[0]:
                            if "(" in ddiv[1]:
                                rrr = randint(2, 8)
                                exec(f"{ddiv[2]} = {rrr}", globals(), ldict)
                                exec(f"{ddiv[1][1]} = {randint(rrr, 29)}", globals(), ldict)
                                exec(f"{ddiv[1][-2]} = {randint(rrr, eval(ddiv[1][1]))}", globals(), ldict)
                            else:
                                rrr = randint(2, 8)
                                exec(f"{ddiv[1][-2]} = {rrr}", globals(), ldict)
                                exec(f"{ddiv[1][1]} = {randint(rrr, 29)}", globals(), ldict)
                                exec(f"{ddiv[2]} = {randint(eval(ddiv[1][1]), 59)}", globals(), ldict)
                        else:
                            rrr = randint(2, 8)
                            exec(f"{ddiv[2]} = {rrr}", globals(), ldict)
                            exec(f"{ddiv[1]} = {randint(rrr, 29)}", globals(), ldict)
                            if "mod" in expr1:
                                if expr1.find("mod") > expr1.find("div"):
                                    x1 = randint(2, eval(f"{ddiv[1]} // {ddiv[2]}", globals(), ldict))
                                else:
                                    x1 = randint(eval(f"{ddiv[1]} // {ddiv[2]}", globals(), ldict), 59)
                            else:
                                x1 = randint(2, 35)
                            if not ldict.get("a", None):
                                ldict["a"] = x1
                            elif not ldict.get("b", None):
                                ldict["b"] = x1
                            else:
                                ldict["c"] = x1
                    elif "mod" in expr1:
                        ddiv = search(r'(\(+[^)]+\)+|[^ (]+) mod (\(+[^)]+\)+|[^ )]+)', expr1)
                        if "(" in ddiv[0]:
                            if "(" in ddiv[1]:
                                rrr = randint(2, 8)
                                exec(f"{ddiv[2]} = {rrr}", globals(), ldict)
                                exec(f"{ddiv[1][1]} = {randint(rrr, 29)}", globals(), ldict)
                                exec(f"{ddiv[1][-2]} = {randint(rrr, eval(ddiv[1][1]))}", globals(), ldict)
                            else:
                                rrr = randint(2, 8)
                                exec(f"{ddiv[1][-2]} = {rrr}", globals(), ldict)
                                exec(f"{ddiv[1][1]} = {randint(rrr, 29)}", globals(), ldict)
                                exec(f"{ddiv[2]} = {randint(eval(ddiv[1][1]), 59)}", globals(), ldict)
                        else:
                            rrr = randint(2, 8)
                            exec(f"{ddiv[2]} = {rrr}", globals(), ldict)
                            exec(f"{ddiv[1]} = {randint(rrr, 29)}", globals(), ldict)
                            x1 = randint(2, 35)
                            if not ldict.get("a", None):
                                ldict["a"] = x1
                            elif not ldict.get("b", None):
                                ldict["b"] = x1
                            else:
                                ldict["c"] = x1
                    else:
                        ldict["a"] = randint(2, 59)
                        ldict["b"] = randint(2, 39)
                        ldict["c"] = randint(2, 79)

                if not a:
                    a = int(ldict["a"])
                if not b:
                    b = int(ldict["b"])
                if not c:
                    c = int(ldict["c"])

                self._a = a

                #########################################################
                #========================EXPR 2=========================#
                #########################################################
                a = eval(expr1.replace("/", "//").replace("div", "//").replace("mod", "%"))
                self._aa = a
                q = randint(2, 10)
                check_vals_a = {b: "b", q: "q", b+q: "b + q", b-q: "b - q", b*q: "b * q", q-b: "q - b"}
                check_vals_b = {a: "a", q: "q", a+q: "a + q", a-q: "a - q", a*q: "a * q", q-a: "q - a"}
                check_vals_c = {b: "b", a: "a", b+a: "b + a", b-a: "b - a", b*a: "b * a", a-b: "a - b"}

                intersec_a = list(set(divs(a)[1:]) & set(check_vals_a.keys()))
                intersec_b = list(set(divs(b)[1:]) & set(check_vals_b.keys()))
                intersec_c = list(set(divs(q)[1:]) & set(check_vals_c.keys()))

                prob = random() < 0.8

                if intersec_a and prob:
                    x2 = choices(intersec_a)[0]
                    if len(check_vals_a[x2]) > 1:
                        expr2 = f"a / ({check_vals_a[x2]})"
                    else:
                        expr2 = f"a / {check_vals_a[x2]}"
                        if check_vals_a[x2] == "b":
                            x1 = "q"
                        else:
                            x1 = "b"
                        sign = choices(["+", "-", "*"])[0]
                        if random() < .5 and sign != "*":
                            expr2 = f"{x1} {sign} {expr2}"
                        else:
                            expr2 = f"{expr2} {sign} {x1}"
                elif intersec_b and prob:
                    x2 = choices(intersec_b)[0]
                    if len(check_vals_b[x2]) > 1:
                        expr2 = f"b / ({check_vals_b[x2]})"
                    else:
                        expr2 = f"b / {check_vals_b[x2]}"
                        if check_vals_b[x2] == "a":
                            x1 = "q"
                        else:
                            x1 = "a"
                        sign = choices(["+", "-", "*"])[0]
                        if random() < .5 and sign != "*":
                            expr2 = f"{x1} {sign} {expr2}"
                        else:
                            expr2 = f"{expr2} {sign} {x1}"
                elif intersec_c and prob:
                    x2 = choices(intersec_c)[0]
                    if len(check_vals_c[x2]) > 1:
                        expr2 = f"q / ({check_vals_c[x2]})"
                    else:
                        expr2 = f"q / {check_vals_c[x2]}"
                        if check_vals_c[x2] == "a":
                            x1 = "b"
                        else:
                            x1 = "a"
                        sign = choices(["+", "-", "*"])[0]
                        if random() < .5 and sign != "*":
                            expr2 = f"{x1} {sign} {expr2}"
                        else:
                            expr2 = f"{expr2} {sign} {x1}"
                else:
                    scope = ["a", "b", "q"]
                    binaries = ["%s + %s", "%s * %s", "%s mod %s", "%s div %s"]
                    expr2 = generate_expression(scope, binaries)

                self._code = code.format(
                    a=self._a,
                    b=b,
                    expr1=expr1.replace("c", str(c)),
                    expr2=expr2.replace("q", str(q))
                )
                if self._target == "a":
                    a = self._a
                    self._answer = "{:.0f}".format(eval(expr1.replace("/", "//").replace("div", "//").replace("mod", "%")))
                else:
                    self._answer = "{:.0f}".format(eval(expr2.replace("/", "//").replace("div", "//").replace("mod", "%")))
            except Exception as e:
                print(e)
                continue
            

    def question_text(self):
        return self.question.format(
            xtra_condition=self._xtra_condition, 
            target=self._target,
            code=self._code
        )

    def category(self):
        return "Целочисленное деление"

    def question_answer(self):
        return self._answer
    
    def level(self):
        return "mid"

    @property
    def max_qty(self):
        return 5000