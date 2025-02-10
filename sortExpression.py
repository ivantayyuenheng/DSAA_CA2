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
            node = Node((expr, result))  # Create a Node with (expression, result)
            self.sortedList.insert(node)

        print(self.sortedList)

    
    def evaluateExpressions(self):
        results = []
        for exp in self.expressions:
            try:
                # Build parse tree
                mytree = BuildParseTree()

                mytree.tokens = Tokeniser(exp).tokenise()
                mytree.build()
                # Evaluate the parse tree
                result = mytree.evaluate()
                
                # Append the expression and result as a tuple
                results.append((exp, result))

            except Exception as e:
                # Handle invalid expressions
                results.append((exp, f"Error: {e}"))
        return results