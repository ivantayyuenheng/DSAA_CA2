from tree import BinaryTree
from stack import Stack
from tokeniser import Tokeniser
from expressionTree import expressionTree

class BuildParseTree:
    def __init__(self):
        self.stack = Stack()
        self.tree = BinaryTree('?')
        self.exp = ""
        self.tokens = []
        self.history = None

    def build(self):
        if self.tokens == None:
            print("\nInvalid expression")
            return None
        else:
            self.stack.push(self.tree)
            currentTree = self.tree

            #print("Initial Stack:")
            #print(self.stack.getValues())  # Display initial stack

            for t in self.tokens:
                # RULE 1: If token is '(' add a new node as left child
                # and descend into that node
                if t == '(':
                    currentTree.insertLeft('?')
                    self.stack.push(currentTree)
                    currentTree = currentTree.getLeftTree() 

                # RULE 2: If token is operator, set key of current node,
                # add a new right child, and move to that node
                elif t in {'+', '-', '*', '/', '**'}:
                    currentTree.setKey(t)
                    currentTree.insertRight('?')
                    self.stack.push(currentTree)
                    currentTree = currentTree.getRightTree()

                # RULE 3: If token is a number, set key of current node
                # to that number and return to parent
                elif t not in {'+', '-', '*', '/', ')', '**'}:
                    try:
                        currentTree.setKey(float(t))
                        currentTree = self.stack.pop()
                    except ValueError:
                        raise ValueError(f"Invalid token: {t}")

                # RULE 4: If token is ')', go back to parent node
                elif t == ')':
                    if not self.stack.isEmpty():
                        currentTree = self.stack.pop()

                #add to history
                self.history.add(self.tokens, self.evaluate())
            return self.tree
        
    def printTree(self):
        self.tree.stackInorder(0, [])
        #print("mystack:")
        #print(mytree.tree.myStack)
        
        self.expressionTree = expressionTree(self.tree)
        self.expressionTree.printExpressionTree()

    def evaluate(self, node=None):

        if node is None:
            node = self.tree 
        leftTree = node.getLeftTree()
        rightTree = node.getRightTree()
        op = node.getKey()

        if leftTree is None and rightTree is None:
            return op

        left_val = self.evaluate(leftTree)
        right_val = self.evaluate(rightTree)

        # Perform operation based on operator
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        elif op == '/':
            if right_val == 0:
                raise ZeroDivisionError("Division by zero erorr.")
            return left_val / right_val
        elif op == '**':
            return left_val ** right_val
        else:
            raise ValueError(f"Invalid operator: {op}")

    def inputExpression(self):
        self.exp = input("Please enter the expression you want to evaluate:\n")
        self.tokens = Tokeniser(self.exp).tokenise()
        #print(self.tokens)
