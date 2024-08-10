import dataclasses
from typing import Any


class LinkedList:

    def __init__(self):
        self.start_node = None

    def add(self, value):
        """
        Append a node to last
        :param value: data be saved to list
        :return:
        """
        if self.start_node is None:
            self.start_node = Node(value=value)
        else:
            node = self.start_node
            while node is not None:
                if node.is_last():
                    node.next_node = Node(value)
                    return True
                else:
                    node = node.next_node

    def get(self, value):
        node = self.start_node
        while node is not None:
            if node.value == value:
                return node.value

            node = node.next_node

        return None

    def remove(self, value):
        # Special case, nothing to remove
        if self.empty():
            return False

        node = self.start_node
        while node is not None:
            if node.next_node is None:
                if node.value == value:
                    self.start_node = None
                    return True

            else:
                next_next_node = node.next_node.next_node
                if node.next_node.value == value:
                    node.next_node = next_next_node
                    return True

                node = node.next_node

    def empty(self):
        if self.start_node is None:
            return True

        return False


@dataclasses.dataclass
class Node:
    value: Any
    next_node = None

    def is_last(self):
        if self.next_node is None:
            return True

        return False
