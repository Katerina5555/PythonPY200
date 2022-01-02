from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value      # TODO  инициализировать атрибуты экземпляра класса Node
        self.next_node = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next_node})"      # TODO реализовать метод __repr__ для отображения экземпляра


if __name__ == '__main__':
    first_node = Node(1)        # TODO инициализировать первый узел

    second_node = Node(2)       # TODO инициализировать второй узел
    first_node.next_node = second_node       # TODO через атрибут экземпляра устанавливаем первому узлу следующий узел

    print(first_node)
    print(second_node)
