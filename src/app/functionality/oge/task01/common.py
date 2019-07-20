from ...tools.task import *


class Task1(BaseTaskOge):
    """ОГЭ по информатике - Задача номер 1"""
    def __init__(self):
        pass

    def category(self):
        return "Задание 1"
    
    @property
    def get_task_num(self):
        return 1

