from .common import *
from random import randint, randrange
from ...tools.choices import choices

class Type0(Task1):
    """Объем памяти текстовых данных"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Объем памяти текстовых данных"
    
    @property
    def get_type_num(self):
        return 1
	
    def level(self):
        return "ez"


class SubtypeA(Type0):
    """Объем памяти текстовых данных - фикс кодировка Unicode"""
    def __init__(self):
        super().__init__()

        self.question = ' В одной из кодировок Unicode каждый символ кодируется {bitsize} битами.'\
        '<br>Вова написал текст (в нём нет лишних пробелов): <br><br> «{txt}».<br><br>  '\
        'Ученик вычеркнул из списка название одного из животных. Заодно он вычеркнул ставшие лишними '\
        'запятые и пробелы  –  два пробела не должны идти подряд. При этом размер нового предложения '\
        'в данной кодировке оказался на {decreasebyte} байт меньше, чем размер исходного предложения.'\
        '<br>Напишите в ответе вычеркнутое название животного.'


#===========================================================================
        bitsize_lst = [8, 16, 32]
        animal_dct = {
            2: ['ёж', 'уж'],
            3: ['лев', 'ёрш', 'рак'],
            4: ['слон', 'рысь', 'тигр', 'жаба'],
            5: ['олень', 'крыса', 'филин', 'фазан'],
            6: ['тюлень', 'тритон', 'гадюка', 'голубь'],
            7: ['носорог', 'ящерица', 'журавль', 'медведь'],
            8: ['крокодил', 'скорпион', 'дикобраз', 'обезьяна'],
            9: ['аллигатор', 'орангутан'],
            10: ['броненосец', 'каракатица']
        }
        common_str = " - дикие животные"

#============================================================================
        number_of_animals = randint(5, 8)
        lengths = list(range(2, 11))
        bitsize = choices(bitsize_lst)[0]

        animals = []
        for animal_num in (lengths.pop(randrange(0,len(lengths))) for _ in range(number_of_animals)):
            animals.append(
                animal_dct[animal_num].pop(randrange(0,len(animal_dct[animal_num])))
            )
        
        self._bitsize = bitsize
        self._txt = str(", ".join(animals) + common_str).capitalize()
        self._answer = animals.pop(randrange(0,len(animals)))
        self._decreasebyte = (
            (len(self._txt) - len(str(", ".join(animals) + common_str).capitalize()))
            *
            self._bitsize
            //
            8
        )


    def question_text(self):
        return self.question.format(
            bitsize=self._bitsize,
            txt=self._txt,
            decreasebyte=self._decreasebyte
        )

    def question_answer(self):
        return self._answer

    def category(self):
        return "Фикс размер кодировки Unicode"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
