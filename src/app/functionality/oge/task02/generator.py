import random, json, sys, hmac, hashlib, itertools, functools
from ..tools import boolequation
from ..tools import table

alphabet = 'abcdefghijklmnopqrstuvwxyz'
fun_name = 'αβγδεζηθικλμνξοπρστυφχψω'
latex = lambda x: '\( ' + str(x) + ' \)'

task = """Логическая функция {f} задаётся выражением {fun}.<br>
Дан частично заполненный фрагмент таблицы истинности функции {f}.
{table}
Определите, какому столбцу таблицы истинности соответствует каждая из переменных {names}.
В ответе напишите подряд без разделителей буквы {names} в том порядке, в котором идут соответствующие им столбцы."""


def erase_two(s):
    return [[x if x != 2 else None for x in row] for row in s]


def generate():
    qtype = 4 if len(sys.argv) < 2 else int(sys.argv[1])
    n = 10 if len(sys.argv) < 3 else int(sys.argv[2])
    r = {"category": "$course$/ЕГЭ/Задача 2/Тип " + str(qtype), "question_type": "shortanswer", "questions": []}
    for i in range(n):
        number_of_variables = 4
        f = random.choice(fun_name)
        terms = boolequation.create_terms(number_of_variables, alphabet)
        fun = boolequation.create_function(terms[:])

        table_head = ['Переменная {}'.format(i) for i in range(1, number_of_variables + 1)] + [latex(f)]
        
        table_body = erase_two(boolequation.generate_slice_table(fun, terms))
        if table_body == [[]]:
            continue;

        table_data = [table_head] + table_body
        table_src = table.create_table(table_data)
        
        answer = ''.join(map(str, terms))
        random.shuffle(terms)
        params = {'f': latex(f), 'fun': latex(fun), 'names': ','.join(map(latex, terms)), 'table': table_src}
        ready_text = task.format(**params)

        r["questions"].append({"question_name": "Задача №" + hmac.new(bytearray(ready_text, 'utf-8'),
                                                                      bytearray('text', 'utf-8'),
                                                                      hashlib.sha1).hexdigest(),
                               "question_text": ready_text, "question_answer": answer})
    return json.dumps(r)


if __name__ == "__main__":
    print(generate())
