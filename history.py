class history:
    def __init__(self):
        self.history = []

    def add(self, tokens, result):
        self.history.append((tokens, result))

    def showLast5(self):
        if not self.history:
            print("\nNo history to show.")
            return
        
        for i, (tokens, result) in enumerate(self.history[-5:]):
            print(f"{min(5, len(self.history)) - i}: {''.join(tokens)} = {result}")

    def editFromHistory(self):
        inputChoice = self.inputChoice()
        

    def inputChoice(self):
    
        choice = input("Please enter the number of the expression history you want to edit:")
        while choice < len(self.history) and -1 < choice < 6 :
            print("Please enter a valid number")
            choice = input("Please enter the number of the expression history you want to edit:")

        print("accept")




