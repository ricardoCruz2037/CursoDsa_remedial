from Node import Node
import logging
class Stack:
    def __init__(self, top_item = None, size = 0, limit = 1000):
        
        self.top_item = top_item
        self.size = size
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            logging.warning("La pila esta llena ¡No queda espacio!")
    
    def pop(self):
        # self.size > 0
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = self.top_item.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else: 
            logging.warning("La pila esta totalmente vacia!")
           
    def peek(self):
        # self.size > 0
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            logging.warning("La pila esta totalmente vacia!")
            
    def has_space(self):
        if self.limit > self.size:
            return True
        
    def is_empty(self):
        if self.size == 0:
            return True
    