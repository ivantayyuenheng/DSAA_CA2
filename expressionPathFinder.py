# Created by: IVAN TAY YUEN HENG (2335133)

import networkx as nx
from fileOutput import OutputFile
from operation import BaseOperation
from addition import AddOne
from subtract import SubtractOne
from multiplication import MultiplyByTwo
from division import DivideByTwo
from power import Square

class NumberPathFinder():
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed Graph
        self.operations = {
            "+1": AddOne(),
            "-1": SubtractOne(),
            "*2": MultiplyByTwo(),
            "/2": DivideByTwo(),
            "**2": Square()
        }
        self.expressions = []  # Store expressions
        self.__outputfile = None # Output file object
    
    def apply_operation(self, num, op):
        if op in self.operations:
            return self.operations[op].apply(num)
        return None

    def build_graph(self, start, target, max_steps=40, max_num=9999):
        self.graph.clear()
        queue = [(start, 0, "")]  # Track expression string
        visited = {}
        self.graph.add_node(start)

        while queue:
            current, steps, expr = queue.pop(0)

            if current in visited and visited[current] <= steps:
                continue
            visited[current] = steps

            if current > max_num:
                continue

            for operation in self.operations:
                new_num = self.apply_operation(current, operation)
                if new_num is not None and new_num >= 0 and new_num not in visited:
                    new_expr = f"({expr}{operation})" if expr else f"({current}{operation})"
                    self.graph.add_edge(current, new_num, weight=1)
                    queue.append((new_num, steps + 1, new_expr))

    def find_shortest_path(self, start, target):
        if start not in self.graph or target not in self.graph:
            print(f"\nNo path found from {start} to {target}. Please select different numbers or update operations.") 
            return None, 0, ""

        if not nx.has_path(self.graph, start, target):
            print(f"\nNo path found from {start} to {target}. Please select different numbers or update operations.")
            return None, 0, ""

        path = nx.shortest_path(self.graph, source=start, target=target, weight="weight")
        steps = len(path) - 1


        # Only allow paths with steps less than 40
        if steps > 40:
            print("\n❌ The shortest path is higher than 40 steps! Please update your operations or change to a different value.")
            return None, 0, ""
    
        if steps == 0:
            print(f"Start and target numbers are not allowed to be the same. Please enter different numbers.")
            return None, 0, ""


        # Generate expression from path
        expression = str(path[0])
        for i in range(len(path) - 1):
            for op in self.operations:
                if self.apply_operation(path[i], op) == path[i + 1]:
                    expression = f"({expression}{op})"
                    break
        
        self.expressions.append(expression)
        return path, steps, expression

    def main_menu(self):
        print("\nWelcome to Minimum Expression Path Finder")

        while True:
            print("\nPlease select your choice ('1', '2', '3', '4'):")
            print("1) Enter new start & target numbers (max: 9999)")
            print("2) Change allowed operations")
            print("3) View stored expressions")
            print("4) Exit program")
            
            choice = input("Select an option: ").strip()
            
            if choice == "1":
                start, target = self.get_numbers()
                self.build_graph(start, target)
                shortest_path, steps, expr = self.find_shortest_path(start, target)
                if shortest_path:
                    print(f"\n✅ Shortest path from {start} to {target}: {shortest_path} (Steps: {steps})")
                    print(f"Expression: {expr}")
                
            elif choice == "2":
                self.set_operations()
            
            elif choice == "3":
                print("\nStored Expressions:")
                for expr in self.expressions:
                    print(f"{expr}")
                
                # Prompt user to save expressions to a file
                save_choice = input("\nDo you want to save these expressions to a text file? (y/n): ").strip().lower()
                while save_choice not in ["y", "n"]:
                    print("Invalid input! Please enter 'y' or 'n'")
                    save_choice = input("Do you want to save these expressions to a text file? (y/n): ").strip().lower()
                
                if save_choice == "y":
                    self.__outputfile = OutputFile()
                    content = "\n".join(self.expressions)
                    self.__outputfile.send_file(content)
                    print(f"\nExpressions saved to {self.__outputfile.get_output_file_name()}.")
                else:
                    print("\nSave operation cancelled.")
            
            elif choice == "4":
                print("\nExiting minimum expression path finder program.")
                break
            else:
                print("\nPlease choose from 1 to 4 only")

    def get_numbers(self):
        while True:
            try:
                start = int(input("\nEnter the starting number: "))
                target = int(input("Enter the target number: "))
                return start, target
            except ValueError:
                print("Invalid input! Please enter whole numbers.")

    def set_operations(self):
        print("\nCurrent operations:", list(self.operations.keys()))
        print("Operations allow to add or remove are (+1 -1 *2 /2 **2)")
        new_operations = input("Enter new operations separated by spaces (e.g., +1 -1 *2): ").strip().split()
        
        # Define a mapping of valid operations to their corresponding objects
        operation_classes = {
            "+1": AddOne(),
            "-1": SubtractOne(),
            "*2": MultiplyByTwo(),
            "/2": DivideByTwo(),
            "**2": Square()
        }
        
        # Validate operations
        valid_operations = {}
        for op in new_operations:
            if op in operation_classes:
                valid_operations[op] = operation_classes[op]
            else:
                print(f"Invalid operation '{op}' ignored.")
        
        if valid_operations:
            self.operations = valid_operations
            print("\nOperations updated successfully")
            print("Current operations:", list(self.operations.keys()))
        else:
            print("\nNo valid operations provided. Operations remain unchanged.")
            print("Current operations:", list(self.operations.keys()))

