from buildParseTree import BuildParseTree


class SortExpressions(BuildParseTree):
    def __init__(self, file_content):
        self.file_content = file_content

    def split_expressions(self):
        
    def sort_expressions(self, expression):
        # Sort the expressions
        self.sort_expression = sorted(expression)

        return self.sort_expression