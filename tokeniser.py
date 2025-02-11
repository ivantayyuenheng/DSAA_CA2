# Created by: IVAN TAY YUEN HENG (2335133) and CHAN JUN YI (2309347)

class Tokeniser:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = []
        self.output = []

    def tokenise(self):
        if self.is_valid_expression():
            number = ""
            i = 0 

            while i < len(self.expression):
                char = self.expression[i]

                if char.isdigit() or char == '.':  # Build multi-digit numbers & decimals
                    number += char

                else:
                    if number:  # Store the completed number
                        self.tokens.append(number)
                        number = ""

                    # Check for '**' operator
                    if char == '*' and i + 1 < len(self.expression) and self.expression[i + 1] == '*':
                        self.tokens.append('**')
                        i += 1  # Skip the next '*'

                    elif char in "+-*/()":  # Other operators and parentheses
                        self.tokens.append(char)
                        
                i += 1  # Move to next character

            i = 0
            while i < len(self.tokens):
                # Check if the current element is a negative sign and the previous one is an operator
                if self.tokens[i] in ['-', '+'] and i - 1 >= 0 and self.tokens[i - 1] in ['+', '-', '*', '/', '(', '**']:
                    self.output.append(self.tokens[i] + self.tokens[i + 1])  # Merge '-' and the next number
                    i += 2  # Skip the next element, since it's already merged
                else:
                    self.output.append(self.tokens[i])
                    i += 1

            output = self.output

            self.output = []
            self.tokens = []

            return output
        else:
            return None
        

    def partial_tokenise(self):
        number = ""
        i = 0 

        while i < len(self.expression):
            char = self.expression[i]
            
            if char.isdigit() or char == '.':  # Build multi-digit numbers & decimals
                number += char

            else:
                if number:  # Store the completed number
                    self.tokens.append(number)
                    number = ""

                # Check for '**' operator
                if char == '*' and i + 1 < len(self.expression) and self.expression[i + 1] == '*':
                    self.tokens.append('**')
                    i += 1  # Skip the next '*'

                elif char in "+-*/":  # Other operators and parentheses
                    self.tokens.append(char)
                    
            i += 1  # Move to next character
        if number != "":
            self.tokens.append(number)

        i = 0
        while i < len(self.tokens):
            # Check if there is a next element
            if i + 1 < len(self.tokens):
                # Check if the current element is a negative sign and the previous one is an operator
                if self.tokens[i] in ['-', '+'] and ( (i - 1 >= 0 and self.tokens[i - 1] in ['+', '-', '*', '/', '**']) or i == 0):
                    self.output.append(self.tokens[i] + self.tokens[i + 1])  # Merge '-' and the next number
                    i += 2  # Skip the next element, since it's already merged
                else:
                    self.output.append(self.tokens[i])
                    i += 1
            else:
                self.output.append(self.tokens[i])
                i += 1

        output = self.output

        self.output = []
        self.tokens = []

        return output

    
    def is_valid_expression(self):
        stack = []  # Stack to store bracketed expressions
        i = 0
        n = len(self.expression)
        validation = 0
        while i < n:
            # Make sure everything must be under one bracket first
            if stack == []:
                validation += 1

            # If all of the expression is not under 1 bracket, return False
            if validation > 1:
                return False
        
            char = self.expression[i]
            if char == '(':
                stack.append([])  # Start a new bracketed expression
            elif char == ')':
                if not stack or not stack[-1]:  # Check for misplaced brackets
                    return False
                sub_expr = stack.pop()  # Get the last bracketed expression
                if not self.is_valid_subexpression(sub_expr):  # Validate its contents
                    return False
                if stack:
                    stack[-1].append('N')  # Represent valid nested expression as 'N'
            elif char.isdigit() or char == '.':  # Check for numbers (including floating points)
                num = char
                decimal_seen = char == '.'  # Track if we see a decimal point
                while i + 1 < n and (self.expression[i + 1].isdigit() or (self.expression[i + 1] == '.' and not decimal_seen)):
                    i += 1
                    if self.expression[i] == '.':
                        decimal_seen = True
                    num += self.expression[i]
                if num.count('.') > 1:  # More than one decimal in a number is invalid
                    return False
                if stack:
                    stack[-1].append(num)
            elif char in '+-*/':  # Check for operators
                # Handle exponentiation `**` as a single operator
                if char == '*' and i + 1 < n and self.expression[i + 1] == '*':
                    char = '**'
                    i += 1
                # Handle negative numbers
                if char == '-' and (i == 0 or self.expression[i - 1] == '(' or self.expression[i - 1] in '+-*/'):
                    num = char
                    while i + 1 < n and (self.expression[i + 1].isdigit() or self.expression[i + 1] == '.'):
                        i += 1
                        num += self.expression[i]
                    if num.count('.') > 1:  # More than one decimal in a number is invalid
                        return False
                    if stack:
                        stack[-1].append(num)
                else:
                    if stack:
                        stack[-1].append(char)
            elif char == ' ':
                pass  # Ignore spaces
            else:
                return False  # Invalid character

            i += 1

        return not stack  # Stack should be empty if all brackets are properly closed

    def is_valid_subexpression(self, sub_expr):
        """
        Checks if a bracketed expression is valid:
        - Either contains exactly [operand, operator, operand]
        - OR contains a valid nested expression.
        """
        if len(sub_expr) == 3 and self.is_number(sub_expr[0]) and sub_expr[1] in ['+', '-', '*', '/', '**'] and self.is_number(sub_expr[2]):
            return True
        elif len(sub_expr) == 3 and sub_expr[0] == 'N' and sub_expr[1] in ['+', '-', '*', '/', '**'] and self.is_number(sub_expr[2]):
            return True
        elif len(sub_expr) == 3 and self.is_number(sub_expr[0]) and sub_expr[1] in ['+', '-', '*', '/', '**'] and sub_expr[2] == 'N':
            return True
        elif len(sub_expr) == 3 and sub_expr[0] == 'N' and sub_expr[1] in ['+', '-', '*', '/', '**'] and sub_expr[2] == 'N':  
            return True
        return False

    def is_number(self, value):
        """ Helper function to check if a string represents a valid integer or float """
        try:
            float(value)  # Works for both integers and floating point numbers
            return True
        except ValueError:
            return False