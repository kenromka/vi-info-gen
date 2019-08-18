from .common import *
import numpy as np
import scipy.sparse.csgraph as csg
from random import randint
from ...tools.choices import choices

class Type0(Task4):
    """Простейшие модели информации"""
    def __init__(self):
        super().__init__()
        
    def category(self):
        return "Простейшие модели информации"
    
    @property
    def get_type_num(self):
        return 1
	
    def level(self):
        return "ez"


class SubtypeA(Type0):
    """Кратчайший путь в графе - матрица смежности"""
    def __init__(self):
        super().__init__()

        self.question = """
Между населёнными пунктами <i>{cities}</i> построены дороги, протяжённость которых (в километрах) приведена в таблице.

{table}
<br>
Определите длину кратчайшего пути между пунктами  <i>{startpoint}</i> и <i>{endpoint}</i>, проходящего через пункт <i>{midpoint}</i>. Передвигаться можно только по дорогам, протяжённость которых указана в таблице.
        """


#===========================================================================
        cities = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        n = randint(5, 7) #number of cities
        
        while True:
            adjacency_matrix = np.ceil(np.random.rand(n, n)*3*np.random.randint(0, 3, (n, n)))
            adjacency_matrix = np.tril(adjacency_matrix, -1) + np.tril(adjacency_matrix, -1).T
#============================================================================
            dist_matrix, predecessor_matrix = csg.dijkstra(adjacency_matrix, return_predecessors=True)

            unreachable_points = dist_matrix == float("inf")
            
            if np.any(unreachable_points):
                continue

            self._endpoint = sorted(zip(range(len(predecessor_matrix.T)), list(map(lambda x: len(np.unique(x)), predecessor_matrix.T))), key=lambda kv: kv[1])[0][0]

            candidates = list(set(np.nonzero(dist_matrix[self._endpoint])[0]) - set(predecessor_matrix.T[self._endpoint]))
            if len(candidates) != 0:
                self._midpoint = choices(candidates)[0]
            else:
                continue
            
            candidates = list(set(np.nonzero(dist_matrix[self._midpoint])[0]) - set(predecessor_matrix.T[self._midpoint]) - set([self._endpoint]))
            if len(candidates) != 0:
                self._startpoint = choices(candidates)[0]
            else:
                continue

            self._answer = dist_matrix[self._startpoint, self._midpoint] + dist_matrix[self._midpoint, self._endpoint]
            #print(dist_matrix) if self._answer == float("inf") else print()

            self._table = """<table align="center" border="1">
            <tbody><tr><td bgcolor="#CCCCFF">&nbsp;</td>"""
            for i in range(n):
                self._table += f"<td><b>{cities[i]}</b></td>"
            self._table += "</tr>"
            for i in range(n):
                self._table += f"""<tr>
                <td><b>{cities[i]}</b></td>"""
                for num, j in enumerate(adjacency_matrix[i]):
                    if i == num:
                        self._table += '<td bgcolor="#CCCCFF">&nbsp;</td>'
                    elif j == 0:
                        self._table += '<td>&nbsp;</td>'
                    else:
                        self._table += f"<td>{int(j)}</td>"
                self._table += "</tr>"
            self._table += "</tbody>\n</table>"

            self._cities = cities[:n]
            break

    def question_text(self):
        return self.question.format(
            cities=", ".join(list(self._cities)),
            table=self._table,
            startpoint=self._cities[self._startpoint],
            midpoint=self._cities[self._midpoint],
            endpoint=self._cities[self._endpoint]
        )

    def question_answer(self):
        return int(self._answer)

    def category(self):
        return "Кратчайший путь в графе - матрица смежности"
    
    @property
    def get_subtype_num(self):
        return 1

    @property
    def max_qty(self):
        return 5000
    
    def stepik_jsonify(self):
        return self.jsonify_basic_text()
