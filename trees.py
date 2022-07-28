from logging import root


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# Binary Search Tree
class BST:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if(self.root == None):
            self.root = Node(value)
        else:
            pointer = self.root
            while(True):
                if(pointer.value < value):
                    if(pointer.right != None):
                        pointer = pointer.right
                    else:
                        pointer.right = Node(value)
                        break
                else:
                    if(pointer.left != None):
                        pointer = pointer.left
                    else:
                        pointer.left = Node(value)
                        break
    def search(self,value):
        pointer = self.root
        exists = 0
        path = []
        while(pointer!=None):
            path.append(pointer.value)
            if(pointer.value == value):
                exists = 1
                break
            elif(pointer.value < value):
                pointer = pointer.right
            else:
                pointer = pointer.left
        return [exists,path]
    def inorder_traversal(self,node):
        if(node!=None):
            left = self.inorder_traversal(node.left)
            center = [node.value]
            right = self.inorder_traversal(node.right)
            return left+center+right
        else:
            return []
    def preorder_traversal(self,node):
        if(node!=None):
            left = self.inorder_traversal(node.left)
            center = [node.value]
            right = self.inorder_traversal(node.right)
            return center+left+right
        else:
            return []
    def postorder_traversal(self,node):
        if(node!=None):
            left = self.inorder_traversal(node.left)
            center = [node.value]
            right = self.inorder_traversal(node.right)
            return left+right+center
        else:
            return []