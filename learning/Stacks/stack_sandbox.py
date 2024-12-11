from Node import Node
import logging
class Stack:
    def __init__(self, top_item = None):
        
        self.top_item = top_item
 
    def push(self, value):
       #2.1
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
    
    def pop(self):
        item_to_remove = self.top_item
        self.top_item = self.top_item.get_next_node()
        return item_to_remove.get_value()
           
    def peek(self):
        return self.top_item.get_value()