from buildParseTree import BuildParseTree
from tokeniser import Tokeniser
from sortedList import SortedList
from sortedNode import Node


class SortExpressions():
    def __init__(self, file_content):
        self.file_content = file_content
        self.sortedList = SortedList()
        self.expressions = None
        self.evaluatedResults = None

    # def split_expressions(self):
    def sort_expressions(self):

        self.expressions = self.file_content.splitlines()
        self.evaluatedResults = self.evaluateExpressions()
        
        for expr, result in self.evaluatedResults:
            if result == '?':
                # Skip invalid expressions
                return False
            else:
                node = Node((expr, result))  # Create a Node with (expression, result)
                self.sortedList.insert(node)

        print(self.sortedList)

    
    def evaluateExpressions(self):
        results = []
        for exp in self.expressions:
            try:
                # Remove spaces
                exp = exp.replace(" ", "")

                # Build parse tree
                mytree = BuildParseTree()

                mytree.tokens = Tokeniser(exp).tokenise()
                mytree.build()
                # Evaluate the parse tree
                result = mytree.evaluate()
                
                # Change integer results to int
                if isinstance(result, float) and result.is_integer():
                    result = int(result)


                
                # Append the expression and result as a tuple
                results.append((exp, result))

            except Exception as e:
                # Handle invalid expressions
                results.append((exp, f"Error: {e}"))
        return results
    
    def __str__(self):
        return str(self.sortedList)