class Node:
    """Узел односвязного списка"""
    def __init__(self, value):
        self.value = value
        self.next = None


class CardQueue:
    """Очередь карт на базе односвязного списка"""
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,value):
        """Функция добавления карты в конец очереди"""
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def pop_left(self):
        """Функция извлечения и возвращения карты из начала
        очереди"""
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_value
    def is_empty(self):
        """Функция проверки на то, что остались карты в колоде
        игрока"""
        return self.head is None