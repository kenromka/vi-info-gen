import random, json, sys, hmac, hashlib, itertools, functools

alphabet = 'abcdefghijklmnopqrstuvwxyz'
fun_name = 'αβγδεζηθικλμνξοπρστυφχψω'

conjunction = lambda x, y: '{ ' + x + ' } \\wedge { ' + y + ' }'
disjunction = lambda x, y: '{ ' + x + ' } \\vee { ' + y + ' }'
positive = lambda x: x
negation = lambda x: '\\overline { ' + x + ' }'
equal = lambda x, y: '{ ' + x + ' } \\equiv { ' + y + ' }'
notequal = lambda x, y: '{ ' + x + ' } \\neq { ' + y + ' }'
implication = lambda x, y: '{ ' + x + ' } \\implies { ' + y + ' }'
latex = lambda x: '\( ' + x + ' \)'

td = lambda x: '<td>' + x + '</td>'
tr = lambda x: '<tr align="center">' + x + '</tr>'

task = """Логическая функция {F} задаётся выражением {fun}.<br>
Дан частично заполненный фрагмент таблицы истинности функции {F}.
{t}
Определите, какому столбцу таблицы истинности соответствует каждая из переменных {x1}, {x2}, {x3}.
В ответе напишите подряд без разделителей буквы {x1}, {x2}, {x3} в том порядке, в котором идут соответствующие им столбцы."""


def generate():
    qtype = 0 if len(sys.argv) < 2 else int(sys.argv[1])
    n = 10 if len(sys.argv) < 3 else int(sys.argv[2])
    r = {"category": "$course$/ЕГЭ/Задача 2/Тип " + str(qtype), "question_type": "shortanswer", "questions": []}
    for i in range(n):
        fun = random.choice(fun_name)
        x1, x2, x3 = 0, 0, 0
        while x1 == x2 or x2 == x3 or x3 == x1:
            x1, x2, x3 = random.choices(alphabet, k = 3)
        result = random.randint(0, 1)
        main_operation = [disjunction, conjunction][result]
        sign1 = random.randint(0, 1)
        A = [negation, positive][sign1](x1)
        sign3 = random.randint(0, 1)
        order = [[negation, positive][sign3](x3), A]
        random.shuffle(order)
        if result == 0:
            B = '(' + random.choice([notequal(negation(x1), x2), equal(x1, x2), notequal(x1, negation(x2))]) + ')'
            C = '(' + conjunction(*order) + ')'
        else:
            B = '(' + random.choice([equal(negation(x1), x2), notequal(x1, x2), equal(x1, negation(x2))]) + ')'
            C = '(' + disjunction(*order) + ')'
        a, b, c = random.choice(list(itertools.permutations([0, 1, 2])))
        A, B, C = [A, B, C][a], [A, B, C][b], [A, B, C][c]
        if result == 0:
            m = [functools.reduce(disjunction, [A, B, C])]
            if sign1 == 1 or a != 0:
                m.append(disjunction('\\bigl (' + implication(negation(A), B) + '\\bigr )', C))
            if sign1 == 1 or b != 0:
                m.append(disjunction(A, '\\bigl (' + implication(negation(B), C) + '\\bigr )'))
            if sign1 == 1 or c == 0:
                m.append(implication('\\bigl (' + conjunction(negation(A), negation(B)) + '\\bigr )', C))
            final = random.choice(m)
        else:
            final = functools.reduce(conjunction, [A, B, C])
        answer = [x1, x2, x3]
        random.shuffle(answer)
        answer = ''.join(answer)
        table = [['Переменная 1', 'Переменная 2', 'Переменная 3', latex(fun)], ['', '', '', str(result)], ['', '', '', str(result)]]
        ones = random.randint(0, 3)
        if ones == 0:
            xzero = x2 if result == sign1 else x1
            table[1][answer.index(xzero)] = '0'
            table[2][answer.index(xzero)] = '0'
            table[random.randint(1, 2)][answer.index(x3)] = '0'
        elif ones == 1:
            xzero = x2 if result == sign1 else x1
            row = random.randint(1, 2)
            table[row][answer.index(xzero)] = '0'
            table[row][answer.index(x3)] = '0'
            table[1 + 2 - row][answer.index(x3)] = '1'
        elif ones == 2:
            xones = x1 if result == sign1 else x2
            row = random.randint(1, 2)
            table[row][answer.index(xones)] = '1'
            table[row][answer.index(x3)] = '1'
            table[1 + 2 - row][answer.index(x3)] = '0'
        elif ones == 3:
            xones = x1 if result == sign1 else x2
            table[1][answer.index(xones)] = '1'
            table[2][answer.index(xones)] = '1'
            table[random.randint(1, 2)][answer.index(x3)] = '1'
        values = '<table border = 1px cellpadding = 4px><tbody>' + tr(''.join(map(td, table[0]))) + tr(''.join(map(td, table[1]))) + tr(''.join(map(td, table[2]))) + '</tbody></table>'
        params = {'F': latex(fun), 'fun': latex(final), 'x1': latex(x1), 'x2': latex(x2), 'x3': latex(x3), 't': values}
        ready_text = task.format(**params)
        r["questions"].append({"question_name": "Задача №" + hmac.new(bytearray(ready_text, 'utf-8'),
                                                                      bytearray('text', 'utf-8'),
                                                                      hashlib.sha1).hexdigest(),
                               "question_text": ready_text, "question_answer": answer})
    return json.dumps(r)


if __name__ == "__main__":
    print(generate())
