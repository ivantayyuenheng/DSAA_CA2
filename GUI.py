# Created by: IVAN TAY YUEN HENG (2335133) and CHAN JUN YI (2309347)
from buildParseTree import BuildParseTree
from fileHandling import ReadFile
from fileOutput import OutputFile
from sortExpression import SortExpressions
from expressionPathFinder import NumberPathFinder
from randomExpressionGenerator import RandomExpressionGenerator
from history import History
from algebricEquation import AlgebricEquation
from tokeniser import Tokeniser

class GUI:
    def __init__(self):
        self.history = History()
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
        3. Minimum expression path finder (Ivan Tay)
        4. Random expression generator (Ivan Tay)
        5. Expression history (Chan Jun Yi)
        6. Simplify algebric expression (Chan Jun Yi)
        7. Exit""")

    def option_handling(self, option):
        match option:
            case '1':
                self.evaluate_expression_choice()
            case '2':
                self.sort_expressions()
            case '3':
                self.expression_path_finder()
            case '4':
                self.random_expression_generator()
            case '5':
                self.expresssion_history()
            case '6':
                self.algebric_equation()
            case '7':
                self.exit_program()
            case _:
                print("\nPlease choose from 1 to 7 only")     

    def evaluate_expression_choice(self):
        mytree = BuildParseTree()
        mytree.inputExpression()
        mytree.build()
        result = mytree.evaluate()
        if result != "?":
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print(f"\nExpression Tree:")
            mytree.printTree()
            print(f"\nExpression evaluates to: \n{result}")
            self.history.add(mytree.tokens, result)

        self.cont()

    def sort_expressions(self):
        file_content = ReadFile(1).get_content()  # Read file content
        output_file = OutputFile()  # Create an OutputFile object

        if file_content:  # Check if content is retrieved
            sorter = SortExpressions(file_content)  # Sort expressions
            success = sorter.sort_expressions()  # Sort expressions
            if success != False:
                print("\n>>>Evaluation and sorting started:\n")
                print(sorter.sortedList)
                output_file.send_file(str(sorter.sortedList))  # Write to output file
            else:
                print("Sorting failed due to invalid expressions. Output file was not created.")

            output_file.send_file(str(sorter.sortedList))  # Write to output file
        else:
            print("Error: Unable to read file content.")
            
        self.cont()

    def expression_path_finder(self):
        path_finder = NumberPathFinder()
        path_finder.main_menu()
        self.cont()

    def random_expression_generator(self):
        generator = RandomExpressionGenerator()
        generator.expression_sub_menu()
        self.cont()

    def expresssion_history(self):
        isHistory = self.history.showLast5()
        if isHistory:
            mytree = BuildParseTree()
            print()
            mytree.exp = self.history.editFromHistory()
            #print(mytree.exp)
            if mytree.exp != None:
                mytree.tokens = Tokeniser(mytree.exp).tokenise()
                #print(mytree.tokens)
                mytree.build()
                result = mytree.evaluate()
                if result != "?":
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)
                    print(f"\nExpression Tree:")
                    mytree.printTree()
                    print(f"\nExpression evaluates to: \n{result}")
                    self.history.add(mytree.tokens, result)

        self.cont()

    def algebric_equation(self):
        mytree = AlgebricEquation()
        mytree.inputExpression()
        mytree.build()
        try:
            result = mytree.evaluate()
            print(f"Simplified expression: {mytree.simplify(result)}")
        except Exception as e:
            print(e)

        self.cont()

    def exit_program(self):
        # Option 7: Exit the program.   
        print("\nBye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter")
        exit()

# Run the program
if __name__ == "__main__":
    gui = GUI()
