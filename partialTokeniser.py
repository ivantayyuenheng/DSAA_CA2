# Created by: Chan Jun Yi (2309347)
class partialTokeniser:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = []
        self.output = []

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