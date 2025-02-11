# Created by: CHAN JUN YI (2309347)
from tokeniser import Tokeniser

class AlgebricTokeniser(Tokeniser):
    def __init__(self, exp):
        self.algebra = exp
        super().__init__(exp)

    def tokenise(self):
        #print(self.expression)
        if self.is_valid_expression():
            self.expression = self.algebra
            number = ""
            i = 0 

            while i < len(self.expression):
                char = self.expression[i]

                if char not in "+-*/()" or char == '.':  # Build multi-digit numbers & decimals
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

    def is_valid_expression(self):
        super().algebric_tokenise()
        return super().is_valid_expression()