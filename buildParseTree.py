from tree import BinaryTree
from stack import Stack

class BuildParseTree():
    def __init__(self):
        self.stack = Stack()
        self.tree = BinaryTree('?')
        self.exp = ""
        self.tokens = ""

    def build(self):
        self.inputExpression()
        self.tokens = self.exp.replace('(', ' ( ').replace(')', ' ) ').split()
        self.stack.push(self.tree)
        currentTree = self.tree
        for t in self.tokens:
            # RULE 1: If token is '(' add a new node as left child
            # and descend into that node
            if t == '(':
                currentTree.insertLeft('?')
                self.stack.push(currentTree)
                currentTree = currentTree.getLeftTree() 

            # RULE 2: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
            elif t in ['+', '-', '*', '/', '**']:
                currentTree.setKey(t)
                currentTree.insertRight('?')
                self.stack.push(currentTree)
                currentTree = currentTree.getRightTree()

            # RULE 3: If token is number, set key of the current node
            # to that number and return to parent
            elif t not in ['+', '-', '*', '/', ')', '**'] :
                try:
                    currentTree.setKey(float(t))
                    parent = self.stack.pop()
                    currentTree = parent
                except ValueError:
                    raise ValueError(f"Invalid token: {t}")

            
            # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = self.stack.pop()
            else:
                raise ValueError
        return self.tree

    def evaluate(self):
        leftTree = self.tree.getLeftTree()
        rightTree = self.tree.getRightTree()
        op = self.tree.getKey()
        
        if leftTree != None and rightTree != None:
            if op == '+':
                return self.evaluate(leftTree) + self.evaluate(rightTree)
            elif op == '-':
                return self.evaluate(leftTree) - self.evaluate(rightTree)
            elif op == '*':
                return self.evaluate(leftTree) * self.evaluate(rightTree)
            elif op == '/':
                return self.evaluate(leftTree) / self.evaluate(rightTree)
            elif op == '**':
                return self.evaluate(leftTree) ** self.evaluate(rightTree)
        else:
            return (self.tree.getKey())

    def inputExpression(self):
        self.exp = input("Please enter the expression you want to evaluate:\n")
