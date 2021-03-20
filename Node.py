import pygame


class Node:
    def __init__(self, key):
        self.key = key
        self.Left = None
        self.Right = None
        self.Parent = None

    def Height(self):
        if self.Left is None and self.Right is None:
            return 0
        elif self.Left is not None:
            if self.Right is not None:
                return Max(self.Left.Height() + 1, self.Right.Height() + 1)
            else:
                return self.Left.Height() + 1
        else:
            return self.Right.Height() + 1

    def hasLeft(self):
        if self.Left is None:
            return False
        else:
            return True

    def hasRight(self):
        if self.Right is None:
            return False
        else:
            return True

    def printWithPadding(self, padding):
        print(padding * " " + str(self.key))

    def printAllNodes(self, padding):
        if self is not None:
            if self.hasRight():
                self.Right.printAllNodes(padding + 5)
            self.printWithPadding(padding)
            if self.hasLeft():
                self.Left.printAllNodes(padding + 5)

    def addNode(self, key):
        if key > self.key:
            if self.Right is None:
                self.Right = Node(key)
                self.Right.Parent = self
            else:
                self.Right.addNode(key)
        elif key < self.key:
            if self.Left is None:
                self.Left = Node(key)
                self.Left.Parent = self
            else:
                self.Left.addNode(key)


def Max(x1, x2):
    if x1 > x2:
        return x1
    else:
        return x2


class BST:

    def __init__(self):
        self.head = None
        self.height = 0

    def getHeight(self):
        if self.head is None:
            return 0
        else:
            return self.head.Height()

    def PrintNodes(self):
        self.head.printAllNodes(5)

    def addNode(self, key):
        if self.head is None:
            self.head = Node(key)
        else:
            self.head.addNode(key)
        self.height = self.getHeight()

    def Search(self, key):
        if self.head is None:
            return None
        curr = self.head
        while True:
            if curr.key == key:
                return curr
            else:
                if key < curr.key:
                    if curr.Left is not None:
                        curr = curr.Left
                    else:
                        return None
                else:
                    if curr.Right is not None:
                        curr = curr.Right
                    else:
                        return None

    def DeleteNode(self, key):
        node = self.Search(key)
        if node == self.head:
            root = True
        else:
            root = False
        if node is not None:
            if not root:
                mod = node.key < node.Parent.key
            if node.Left is None and node.Right is None:
                if not root:
                    if mod:
                        node.Parent.Left = None
                    else:
                        node.Parent.Right = None
                else:
                    self.head = None
            else:
                if node.Left is not None and node.Right is not None:
                    LeafNode = node.Left
                    ok = False
                    while LeafNode.Right is not None:
                        LeafNode = LeafNode.Right
                        ok = True
                    node.key = LeafNode.key
                    if ok:
                        LeafNode.Parent.Right = LeafNode.Left
                    else:
                        LeafNode.Parent.Left = LeafNode.Left
                elif node.Left is not None:
                    if not root:
                        node.Left.Parent = node.Parent
                        if mod:
                            node.Parent.Left = node.Left
                        else:
                            node.Parent.Right = node.Left
                    else:
                        self.head = node.Left

                else:
                    if not root:
                        node.Right.Parent = node.Parent
                        if mod:
                            node.Parent.Left = node.Right
                        else:
                            node.Parent.Right = node.Right
                    else:
                        self.head = node.Right
        self.height = self.getHeight()

    def getMIN(self):
        if self.head is None:
            return None
        else:
            curr = self.head
            while curr.Left is not None:
                curr = curr.Left
            return curr.key
    def getMAX(self):
        if self.head is None:
            return None
        else:
            curr = self.head
            while curr.Right is not None:
                curr = curr.Right
            return curr.key

