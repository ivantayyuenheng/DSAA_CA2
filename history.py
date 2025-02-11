class history:
    def __init__(self):
        self.history = []

    def add(self, tokens, result):
        self.history.append((tokens, result))

    def showLast5(self):
        print()
        if not self.history:
            print("\nNo history to show.")
            return
        
        for i, (tokens, result) in enumerate(self.history[-5:]):
            print(f"{min(5, len(self.history)) - i}: {''.join(tokens)} = {result}")

    def editFromHistory(self):
        if not self.history:
            print("\nNo history to edit.")
            return
        inputChoice = self.inputChoice()
        #exit history
        if inputChoice == 0:
            return
        #edit from  history
        choice = self.history[-inputChoice]
        print(f"{''.join(choice[0])} = {choice[1]}")
        
    def inputChoice(self):
        try:
            index = int(input("Please enter the number of the expression history you want to edit:"))
            #not in history
            if index < 0 or index > min(len(self.history), 5):
                print("Invalid index. Please enter a number between 0 and", min(len(self.history), 5))
                return self.inputChoice()
            return index
        except ValueError:
            print("Invalid index. Please enter a number between 0 and", min(len(self.history), 5))
            return self.inputChoice()




