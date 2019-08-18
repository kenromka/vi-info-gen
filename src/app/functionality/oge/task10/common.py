from ...tools.task import *
from ...tools.choices import *


class Task10(BaseTaskOge):
    """ОГЭ по информатике - Задание номер 10"""
    def __init__(self):
        pass
    
    def category(self):
        return "Задание 10"
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
    
    @property
    def max_qty(self):
        return 5000