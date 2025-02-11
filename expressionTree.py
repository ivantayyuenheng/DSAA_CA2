# Created by: IVAN TAY YUEN HENG (2335133) and CHAN JUN YI (2309347)

from tree import Tree

class ExpressionTree(Tree):
    def __init__(self, tree):
        super().__init__()
        self.tree = tree

    def printTree(self):
        self.printExpressionTree()

    def printExpressionTree(self):
        self.data = self.tree.myStack
        processed_array_within = self.split_elements_within_array()
        highest_row = self.find_highest_row(processed_array_within)

        self.row = highest_row + 1
        self.col = len(self.tree.myStack)

        multiplication_grid = self.create_multiplication_grid(self.row, self.col)

        for col_index, items in enumerate(processed_array_within):
            for value, row_index in items:
                multiplication_grid[row_index][col_index] = value

        grid_string = '\n'.join([''.join(row) for row in multiplication_grid])
        print(grid_string)


    #for printing expression tree
    def split_elements_within_array(self):
        result = []
        for item in self.data:
            value, index = item
            # Convert value to string and split into individual characters
            #removing floating point if it is an integer
            if isinstance(value, (int, float)):
                if value == int(value):
                    value = int(value)
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