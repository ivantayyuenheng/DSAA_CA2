class expressionTree:
    def __init__(self, tree):
        self.tree = tree
        self.row = 0
        self.col = 0


    def printExpressionTree(self):
        self.data = self.tree.myStack
        processed_array_within = self.split_elements_within_array()
        highest_row = self.find_highest_row(processed_array_within)

        self.row = highest_row + 1
        self.col = len(self.tree.myStack)

        multiplication_grid = self.create_multiplication_grid(self.row, self.col)

        for col_index, items in enumerate(processed_array_within):  # Iterate through columns of the array
            for value, row_index in items:  # For each value in the array column
                multiplication_grid[row_index][col_index] = value  # Place value into the correct grid position

        grid_string = '\n'.join([''.join(row) for row in multiplication_grid])

        # Display the resulting string
        print(grid_string)

 
    #for printing expression tree
    def split_elements_within_array(self):
        result = []
        for item in self.data:
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