#!/usr/bin/env python3

"""
A singly-linked list class that can be reversed in place.
Avoids cycles and duplicate nodes in list.
"""

class Node(object):
    """A node in a singly-linked list."""
    def __init__(self, value):
        self.next = None
        self.value = value

class SinglyLinkedList(object):
    """A singly-linked list of nodes."""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        """Append a node to the end this list.  No duplicates or cycles allowed."""
        # Do not allow duplicate nodes in the list.
        n = self.head
        while n:
            if n == node: raise ValueError("illegal append of duplicate node")
            n = n.next

        if self.tail:
            self.tail.next = node
        self.tail = node

        node.next = None # Prevent cycles.
        if not self.head:
            self.head = node

    def reverse(self):
        """Reverse this list in place."""
        head = self.head
        if head is None: return # Size 0.
        if head.next is None: return # Size 1.

        new_head = head.next
        while new_head:
            # A -> B -> C
            # h
            #      n
            temp = new_head.next
            new_head.next = head
            if head == self.head:
                head.next = None
            head = new_head
            new_head = temp
            # A <- B C
            #        t
            #      h
            #        n
            #----
            # A <- B <- C
            #              t
            #           h
            #              n

        self.tail = self.head
        self.head = head

    def __str__(self):
        """Render this list as a string."""
        s = ""
        n = self.head
        s += "s["
        while n:
            s += n.value
            n = n.next
            if n: s += " -> "
        s += "]"
        return s


# Create a list and reverse it.
sll = SinglyLinkedList()
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
sll.append(node1)
sll.append(node2)
sll.append(node3)
sll.append(node4)
try:
    sll.append(node2)
except ValueError:
    print("Okay, not adding duplicate node.")
print(sll)
sll.reverse()
print(sll)



