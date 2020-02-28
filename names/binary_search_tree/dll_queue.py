import sys
from dll import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.head:
            return self.storage.remove_from_head()
        else:
     #       print(f"nothing to offer, sorry [internall dll.length = {self.len()}]")
            return None

    def len(self):
        return self.storage.length



