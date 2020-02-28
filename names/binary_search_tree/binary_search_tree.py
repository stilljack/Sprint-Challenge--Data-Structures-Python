import sys

sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack, DoublyLinkedList

import collections


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # value = 7
        # 5                             (x)
        # l:2 R :4

        if not self.value:
            self.value = BinarySearchTree(value)
        # lean right
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            # self.left exists
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to
    # Hint:  Use a recursive, depth first traversal

    # Gonna try this as a decorator pattern
    def in_order_print(self, node):
        final = []

        def iop_helper(node):
            nonlocal final
            if node:
                iop_helper(node.left)

                final.append(node.value)

                iop_helper(node.right)

        iop_helper(node)
        for result in final:
            print(result)
        return final

    def pre_order_dft(self, node):
        final = []

        def preorder_helper(node):
            nonlocal final
            if node:
                final.append(node.value)

                preorder_helper(node.left)

                preorder_helper(node.right)

        preorder_helper(node)
        for result in final[0:]:
            print(result)
        return final

# Print Post-order recursive DFT
    def post_order_dft(self, node):
        final = []

        def post_order_helper(node):
            nonlocal final
            if node:
                post_order_helper(node.left)

                post_order_helper(node.right)

                final.append(node.value)

        post_order_helper(node)
        for result in final[0:]:
            print(result)
        return final



    # finallist =[]
    # lefts =[]
    # rights = []
    # if isinstance(self.left,BinarySearchTree):
    #     lefts= self.in_order_print(self.left)
    #
    # if isinstance(self.right,BinarySearchTree):
    #     rights = self.in_order_print(self.right)
    # finallist =lefts + [self. value] + rights
    # print(finallist)
    # return finallist

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     queue = Queue()
    #     # root into queue
    #     queue.enqueue(node)
    #     #print(f"init queue len ={queue.len}")
    #     while queue.len != 0:
    #         temp: BinarySearchTree = queue.dequeue()
    #         if temp:
    #             if temp.right:
    #                 queue.enqueue(temp.right)
    #             if temp.left:
    #                 queue.enqueue(temp.left)
    #             print(temp.value)
    #         else:
    #             break
    #
    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     stack = Stack()
    #     # root into stack
    #     stack.push(node)
    #     #print(f"init stack len ={stack.len}")
    #     while stack.len != 0:
    #         temp: BinarySearchTree = stack.pop()
    #         if temp:
    #             if temp.right:
    #                 stack.push(temp.right)
    #             if temp.left:
    #                 stack.push(temp.left)
    #             print(temp.value)
    #         else:
    #             break
    #         # stacj

    # root to stack push
    # while stack not empty
    # pop top item out of stack into temp
    # do the thing?
    # if temp has right, put right into stack
    # if temp has left, put into stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

