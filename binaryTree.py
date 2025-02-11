from tree import Tree

class BinaryTree(Tree):
    def __init__(self,key, leftTree = None, rightTree = None):
        super().__init__()
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key
    
    def getLeftTree(self):
        return self.leftTree
    
    def getRightTree(self):
        return self.rightTree
    
    def insertLeft(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree

    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree

    def printPreorder(self, level):
        print( str(level*'-') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1) 

    def printInorder(self, level, leafStack):
        if self.leftTree != None:
            self.leftTree.printInorder(level+1, leafStack)
        print( str(level*'-') + str(self.key))
        leafStack.append([self.key, level])
        if self.rightTree != None:
            self.rightTree.printInorder(level+1, leafStack) 
        self.myStack = leafStack

    def printPostorder(self, level):
        if self.leftTree != None:
            self.leftTree.printPostorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPostorder(level+1) 
        print( str(level*'-') + str(self.key))

    def stackInorder(self, level, leafStack):
        if self.leftTree != None:
            self.leftTree.stackInorder(level+1, leafStack)
        leafStack.append([self.key, level])
        if self.rightTree != None:
            self.rightTree.stackInorder(level+1, leafStack) 
        self.myStack = leafStack