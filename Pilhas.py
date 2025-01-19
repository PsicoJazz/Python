class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push (self, elemen):
        node = Node(elemen)
        node.next = self.top
        self.top = node
        self.size += 1




    def __repr__(self):
        if self.size == 0:
            return 'Pilha vazia'

    s = ''
    p = self.top

    while(p):
        s += str(p.data) + '\n'
        p = self.next
    print (s)
        
        
