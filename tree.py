from stack import Stack

class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
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

    def printInorder(self, level):
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)
        print( str(level*'-') + str(self.key))
        if self.rightTree != None:
            self.rightTree.printInorder(level+1)    

    def printPostorder(self, level):
        if self.leftTree != None:
            self.leftTree.printPostorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPostorder(level+1) 
        print( str(level*'-') + str(self.key))

def buildParseTree(exp):
    tokens = exp.replace('(', ' ( ').replace(')', ' ) ').split()
    stack = Stack()
    tree = BinaryTree('?')
    stack.push(tree)
    currentTree = tree
    for t in tokens:
        # RULE 1: If token is '(' add a new node as left child
        # and descend into that node
        if t == '(':
            currentTree.insertLeft('?')
            stack.push(currentTree)
            currentTree = currentTree.getLeftTree() 

        # RULE 2: If token is operator set key of current node
        # to that operator and add a new node as right child
        # and descend into that node
        elif t in ['+', '-', '*', '/', '**']:
            currentTree.setKey(t)
            currentTree.insertRight('?')
            stack.push(currentTree)
            currentTree = currentTree.getRightTree()

        # RULE 3: If token is number, set key of the current node
        # to that number and return to parent
        elif t not in ['+', '-', '*', '/', ')', '**'] :
            try:
                currentTree.setKey(float(t))
                parent = stack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError(f"Invalid token: {t}")

        
        # RULE 4: If token is ')' go to parent of current node
        elif t == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree


def evaluate(tree):

    leftTree = tree.getLeftTree()
    rightTree = tree.getRightTree()
    op = tree.getKey()

    
    if leftTree != None and rightTree != None:
        if op == '+':
            return evaluate(leftTree) + evaluate(rightTree)
        elif op == '-':
            return evaluate(leftTree) - evaluate(rightTree)
        elif op == '*':
            return evaluate(leftTree) * evaluate(rightTree)
        elif op == '/':
            return evaluate(leftTree) / evaluate(rightTree)
        elif op == '**':
            return evaluate(leftTree) ** evaluate(rightTree)
    else:
        return (tree.getKey())

