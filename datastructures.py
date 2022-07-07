class Stack:
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        temp = self.stack[-1]
        self.stack = self.stack[:-1]
        return temp

class Queue:
    def __init__(self):
        self.q = []
    def push(self,value):
        self.q.append(value)
    def pop(self):
        temp = self.q[0]
        self.q = self.q[1:]
        return temp

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,val):
        if(self.head == None):
            self.head = Node(val)
        else:
            pointer = self.head
            while(pointer.next != None):
                pointer = pointer.next
            pointer.next = Node(val)
    def remove(self,val):
        pointer = self.head
        if(pointer.next == None):
            if(pointer.val==val):
                self.head = None
        while(pointer.next != None):
            if(pointer.next.val == val):
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
    def reverse(self):
        left = self.head
        right = self.head.next
        left.next = None
        while(right != None):
            self.head = right
            right = self.head.next
            self.head.next = left
            left = self.head
    def traverse(self):
        pointer = self.head
        while(pointer.next != None):
            print(pointer.val,end=", ")
            pointer = pointer.next
        print(pointer.val)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert(self,val):
        if(self.head == None):
            self.head = Node(val)
        else:
            new = Node(val)
            pointer = self.head
            while(pointer.next != None):
                pointer = pointer.next
            pointer.next = new
            new.prev = pointer
    def remove(self,val):
        pointer = self.head
        if(pointer.next == None):
            if(pointer.val==val):
                self.head = None
        while(pointer.next != None):
            if(pointer.next.val == val):
                pointer.next = pointer.next.next
                pointer.next.prev = pointer
                break
            pointer = pointer.next
    def reverse(self):
        left = self.head
        right = self.head.next
        left.next = None
        while(right != None):
            self.head = right
            right = self.head.next
            self.head.next = left
            self.head.prev = right
            left = self.head
    def traverse(self):
        pointer = self.head
        while(pointer.next != None):
            print(pointer.val,end=", ")
            pointer = pointer.next
        print(pointer.val)