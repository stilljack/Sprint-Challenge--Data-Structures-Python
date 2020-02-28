from doubly_linked_list import DoublyLinkedList
#
# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is
# full and a new element is inserted, the oldest element in the ring buffer is
# overwritten with the newest element. This kind of data structure is very useful
# for use cases such as storing logs and history information, where you typically
# want to store information up until it reaches a certain age, after which you don't ' \
#                                                                                 'care about it anymore and don't mind seeing it overwritten by newer data.
#
# Implement this behavior in the RingBuffer class. RingBuffer has two methods
# , append and get. The append method adds elements to the buffer. The get method,
# which is provided, returns all of the elements in the buffer in a list in their
# given order. It should not return any None values in the list even if they are present in the ring buffer.
#
# You may not use a Python List in your implementation of the append method
# (except for the stretch goal)
#
# Stretch Goal: Another method of implementing a ring buffer uses an array
# (Python List) instead of a linked list. What are the advantages and disadvantages
# of using this method? What disadvantage normally found in arrays is overcome with this arrangement?

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if capacity need to get filled, just add it and set the current to the head of the list
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current=self.storage.head
        else:
        #else so capcity has been reached,
        #save the value at the head to temp,
        #remove it from the head,
        #add the new item to the end (preserving order)
        #if that temp is equal to our saved self.current value, switch current to the tail
            temp = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if temp == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        #add current value
        list_buffer_contents.append(self.current.value)
        #if there is a next object from the current position in the DLL, set next node like that, else set nextnode as the head
        if self.current.next:
            nextNode = self.current.next
        else:
            nextNode = self.storage.head
        # get all the values by walking through the dll until next node is our "current" node
        while nextNode is not self.current:
            list_buffer_contents.append(nextNode.value)
            if nextNode.next:
                nextNode = nextNode.next
            else:
                nextNode = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
