from dll import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        if self.storage.head:
            return self.storage.remove_from_head()
        else:
         #   print("nothing here to pop() chief")
            return None

    def len(self):
        return self.storage.length
