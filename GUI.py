class GUI:
    def __init__(self):
        self.title_bar()
        self.cont()

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
        3. Detect Objects
        4. Identify Objects
        5. Object Removal
        6. Create Input Text Files
        7. Exit""")

    def option_handling(self, option):
            match option:
                case '1':
                    self.evaluate_expression()
                case '2':
                    self.sort_expressions()
                case '3':
                    self.detect_objects()
                case '4':
                    self.identify_objects()
                case '5':
                    self.delete_objects()
                case '6':
                    self.create_input_files()
                case '7':
                    self.exit_program()
                case _:
                    print("\nPlease choose from 1 to 7 only")
                
            
    def evaluate_expression(self):
        self.cont()

    def sort_expressions(self):
        self.cont()

    def detect_objects(self):
       self.cont()

    def identify_objects(self):
        self.cont()

    def delete_objects(self):
        self.cont()

    def create_input_files(self):
        self.cont()

    def exit_program(self):
        # Option 7: Exit the program.
        print("\nBye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter")
        exit()
