from buildParseTree import BuildParseTree
from fileHandling import ReadFile
from fileOutput import OutputFile
from sortExpression import SortExpressions

class GUI:
    def __init__(self):
        self.title_bar()

    def title_bar(self):
        # Show the title bar
        print("""
*************************************************************************
* ST1507 DSAA: Expression Evaluator & Sorter                            *
* ----------------------------------------------------------------------*
*                                                                       *
*     - Done by: IVAN TAY YUEN HENG (2335133) & CHAN JUN YI (2309347)   *
*     - Class DAAA/2A/21                                                *
*                                                                       *
*************************************************************************
""")
        self.cont()

    def cont(self):
        input("\nPress Enter, to continue....\n")
        self.run()

    def run(self):
        while True:
            self.menu()
            option = input("Enter choice: ")
            self.option_handling(option)

    def menu(self):
        # Selection menu
        print("""Please select your choice ('1', '2', '3', '4', '5', '6', '7'):
        1. Evaluate expression
        2. Sort expressions
        3. Extra Feature 1 (Ivan Tay)
        4. Extra Feature 2 (Ivan Tay)
        5. Extra Feature 1 (Chan Jun Yi)
        6. Extra Feature 2 (Chan Jun Yi)
        7. Exit""")

    def option_handling(self, option):
        match option:
            case '1':
                self.evaluate_expression_choice()
            case '2':
                self.sort_expressions()
            case '3':
                self.cont()
            case '4':
                self.cont()
            case '5':
                self.cont()
            case '6':
                self.cont()
            case '7':
                self.exit_program()
            case _:
                print("\nPlease choose from 1 to 7 only")     

    def evaluate_expression_choice(self):
        evaluate_expression = BuildParseTree()
        tree = evaluate_expression.build()
        result = evaluate_expression.evaluate()

        print("")
        print("Expression tree:")


    
        self.cont()

    def sort_expressions(self):
        file_content = ReadFile().get_content()  # Read file content

        if file_content:  # Check if content is retrieved
            evaluate_expression = BuildParseTree()  # Create instance only when needed
            sorted_expressions = SortExpressions(file_content)  # Sort expressions
            print("Sorted Expressions:", sorted_expressions)  # Display sorted result
        else:
            print("Error: Unable to read file content.")
            
        self.cont()

    def exit_program(self):
        # Option 7: Exit the program.   
        print("\nBye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter")
        exit()

# Run the program
if __name__ == "__main__":
    gui = GUI()
