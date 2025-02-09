import random
from fileOutput import OutputFile  # Import file output handler
from buildParseTree import BuildParseTree  # Import expression evaluator

class RandomExpressionGenerator:
    def __init__(self):
        self.operators = ['+', '-', '*', '/', '**']
        self.correct_answers = 0  
        self.total_attempts = 0  
        self.current_expression = None
        self.current_answer = None
        self.current_difficulty = None
        self.content = ""  # Variable to store all generated expressions

    def generate_expression(self, difficulty):
        """Generates a new random expression based on difficulty."""
        if difficulty == 1:  
            num_operators = 1
            value_range = (1, 10)
        elif difficulty == 2:  
            num_operators = random.randint(2, 3)
            value_range = (1, 20)
        elif difficulty == 3:  
            num_operators = random.randint(4, 5)
            value_range = (1, 100)
        else:
            raise ValueError("Invalid difficulty level.")

        while True:
            expression = ""
            for _ in range(num_operators + 1):
                num = str(random.randint(*value_range))
                if not expression:
                    expression = num
                else:
                    operator = random.choice(self.operators)
                    expression = f'({expression} {operator} {num})'

            try:
                result = self.evaluate_expression(expression)
                if isinstance(result, (int, float)) and -9999 <= result <= 9999:
                    self.current_expression = expression
                    self.current_answer = result
                    self.current_difficulty = difficulty
                    # Append the generated expression to the content variable
                    self.content += f"{expression}\n"
                    return expression, result
            except OverflowError:
                continue  

    def evaluate_expression(self, expression):
        """Evaluates the mathematical expression."""
        try:
            result = eval(expression)
            return round(result, 2)
        except ZeroDivisionError:
            return "Undefined (Division by Zero)"
        except OverflowError:
            return "Overflow Error"

    def expression_sub_menu(self):
        """Sub-menu for generating or answering an expression."""
        while True:
            print("\n===== Random Expression Generator =====")
            print(f"Score: {self.correct_answers}/{self.total_attempts} correct")

            print("\nGenerated Expression:", self.current_expression if self.current_expression else "None")
            print("\n1) Generate Expression (Easy, Medium, Hard)")
            print("2) Answer the expression")
            print("3) Save all generated expressions to file")
            print("4) Use evaluate expression") 
            print("5) Return to GUI")
            choice = input("Select an option: ")

            if choice == '1':
                difficulty = self.select_difficulty()
                self.generate_expression(difficulty)
            elif choice == '2' and self.current_expression:
                self.answer_expression()
            elif choice == '3':
                self.save_expressions_to_file()
            elif choice == '4':
                self.evaluate_expression_choice()
            elif choice == '5':
                print("\nReturning to GUI...")
                return  # Exit loop, returning control to GUI
            else:
                print("Invalid choice. Please try again.")

    def select_difficulty(self):
        """Prompts the user to select a difficulty level."""
        while True:
            print("\nSelect Difficulty Level:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            choice = input("Enter choice: ")
            if choice in ['1', '2', '3']:
                return int(choice)
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

    def answer_expression(self):
        """Handles user answering the expression."""
        while True:
            if self.current_expression == None:
                print("No expression available to answer. Please generate an expression first.")
                return
            

            user_input = input("Enter your answer: ")

            try:
                user_answer = round(float(user_input), 2)
                self.total_attempts += 1  

                if user_answer == self.current_answer:
                    self.correct_answers += 1  
                    print("✅ Correct!")
                else:
                    print(f"❌ Incorrect! The correct answer was: {self.current_answer}")

                # Reset current expression after answering
                self.current_expression = None
                self.current_answer = None
                self.current_difficulty = None
                break

            except ValueError:
                print("Invalid input! Please enter a numerical answer.")

    def save_expressions_to_file(self):
        """Saves all generated expressions to a file."""
        if not self.content:
            print("No expressions available to save.")
            return
        
        print("\nGenerated Expressions:")
        print(self.content)
        
        output_handler = OutputFile()
        output_handler.send_file(self.content)
        print(f"✅ Expressions saved to {output_handler.get_output_file_name()}")

    def evaluate_expression_choice(self):
        """Evaluates an expression using a parse tree."""
        evaluate_expression = BuildParseTree()
        tree = evaluate_expression.build()
        result = evaluate_expression.evaluate()

        print(tree)