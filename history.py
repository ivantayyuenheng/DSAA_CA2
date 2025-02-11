class history:
    def __init__(self):
        self.history = []

    def add(self, tokens, result):
        self.history.append((tokens, result))
    
    def show(self):
        for i, (tokens, result) in enumerate(self.history):
            print(f"\nExpression {i + 1}: {' '.join(tokens)}")
            print(f"Result: {result}")

    def showLast5(self):
        if len(self.history) == 0:
            print("\nNo history to show.")
        if len(self.history) > 5:
            for i, (tokens, result) in enumerate(self.history[-5:]):
                print(f"\nExpression {len(self.history) - 5 + i + 1}: {' '.join(tokens)}")
                print(f"Result: {result}")
        else:
            self.show()


