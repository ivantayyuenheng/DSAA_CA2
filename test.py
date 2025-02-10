from tree import BinaryTree
from stack import Stack
from tokeniser import Tokeniser

class BuildParseTree:
    def __init__(self):
        self.stack = Stack()
        self.tree = BinaryTree('?')
        self.exp = ""
        self.tokens = []

    def build(self):
        self.inputExpression()
        if self.tokens == None:
            print("Invalid expression")
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

            return self.tree

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
        print(self.tokens)

    #for printing expression tree
    def split_elements_within_array(self, data):
        result = []
        for item in data:
            value, index = item
            # Convert value to string and split into individual characters
            value_str = str(value)
            split_subarray = []
            for i, char in enumerate(value_str):
                split_subarray.append([char, index + i])
            result.append(split_subarray)
        return result
    
    def find_highest_row(self, data):
        max_index = float('-inf')
        for subarray in data:
            for element in subarray:
                _, index = element
                if index > max_index:
                    max_index = index
        return max_index
    
    def create_multiplication_grid(self, rows, columns):
        grid = []
        for row in range(rows):
            grid_row = []
            for col in range(columns):
                grid_row.append(' ')
            grid.append(grid_row)
        return grid

while True:
    mytree = BuildParseTree()
    mytree.build()
    print()
    print("mystack:")
    result = mytree.evaluate()
    print(f"Result of expression evaluation: {result}")
    #get mystack
    mytree.tree.stackInorder(0, [])
    print(mytree.tree.myStack)


    processed_array_within = mytree.split_elements_within_array(mytree.tree.myStack)
    highest_row = mytree.find_highest_row(processed_array_within)
    row = highest_row + 1
    col = len(mytree.tree.myStack)
    multiplication_grid = mytree.create_multiplication_grid(row, col)

    for col_index, items in enumerate(processed_array_within):  # Iterate through columns of the array
        for value, row_index in items:  # For each value in the array column
            multiplication_grid[row_index][col_index] = value  # Place value into the correct grid position

    grid_string = '\n'.join([''.join(row) for row in multiplication_grid])

    # Display the resulting string
    print(grid_string)
    
