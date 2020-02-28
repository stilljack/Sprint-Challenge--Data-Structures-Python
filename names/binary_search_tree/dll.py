"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode(object):
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    def __repr__(self):
        return f"ListNode =({self.value})"

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList(object):
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            #empty list
            self.head=new_node
            self.tail=new_node

        else:
            # we know the list is populated and we must update without losing data
            #so set self.head to the .next of the new node
            new_node.next = self.head
            #set the prev to the new node
            self.head.prev=new_node
            #finally update nself.head
            self.head = new_node
        #print(self.head)
        #print(new_node)
        return self.head

    def __repr__(self):
        return f"dll head =({self.head.value})\ndll tail =({self.tail.value})"

        #what do we need to think about?
        #what are the scnearios?
    #this needs to be head were adding to head
    #update privous head
    #increase length
    #edge cases? if self.is none than there is no list no tail
    #if here is no tail ... new becomes new tail as well

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        prev = self.head.value
        self.delete(self.head)
        return prev

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        self.length+=1
        if not self.head and not self.tail:
            self.head =self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.head and not self.tail:
            #       print(f"ERROR delete method called for {node.key}, list is empty ")
            return
        self.length -= 1
        if self.head == self.tail == node:
            #           print(f"self.head == self.tail == node \n{self.head} == {self.tail} == {node}")
            self.head = None
            self.tail = None
            return
        if self.head == node:
            self.head = self.head.next
            node.delete()
            return
        elif self.tail == node:
            self.tail = self.tail.prev
            return
        else:
            node.delete()
            return

    """Returns the highest value currently in the list"""
    def print_list(self, node=None):
        if node is None:
            node =self.head
        while(node is not None):
            #  print( node.value )
            #  print(f"object value is  {node}")
            last = node
            node = node.next

        # print("\nTraversal in reverse direction")
        while(last is not None):
            #   print(f"object value is  {last}")
            #   print (last.value)
            last = last.prev

    def get_max(self):

        final = self.head.value
        #   print (self.head.value)
        rel=self.head
        for i in range(self.length):
            if rel.next:
                rel=rel.next
                if final < rel.value:
                    final = rel.value

        #    print (f"self.head={self.head}\nself.tail={self.tail}\nself.length={self.length}")
        #    print("head:")
        #      self.print_list(self.head)
        #     print("tail:")
        #    self.print_list(self.tail)
        #    print("final:")
        #     print(final)
        return final



#
