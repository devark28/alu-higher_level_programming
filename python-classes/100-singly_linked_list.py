#!/usr/bin/python3
"""
a Node class
"""


class Node:
    """
    Node class
    """
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """
    SinglyLinkedList class
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        string = ""
        current = self.__head
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return
        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        current.next_node = Node(value, current.next_node)
