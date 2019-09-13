from ...tools.task import *
from ...tools.choices import *


class Task10Old(BaseTaskOge):
    """ОГЭ по информатике - Задание номер 10"""
    def __init__(self):
        pass
    
    def category(self):
        return "Задание 9, 10 OLD"
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
    
    @property
    def max_qty(self):
        return 5000