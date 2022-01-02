from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next_node = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next_node})"


if __name__ == "__main__":
    list_nodes = [Node(i) for i in range(10)]  # TODO с помощью list comprehension сделать список узлов со значениями от 0 до 9
    print(list_nodes)

    for elem in list_nodes:
        print(elem.value)          # TODO распечатать значения узлов
