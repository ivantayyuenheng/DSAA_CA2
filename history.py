from tokeniser import Tokeniser

class history:
    def __init__(self):
        self.history = []
        self.edit_tokens = []

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

        #choose from hisory
        if not self.history:
            print("\nNo history to edit.")
            return
        inputChoice = self.inputChoice()

        #exit history
        if inputChoice == 0:
            return
        
        #edit from  history
        choice = self.history[-inputChoice]
        self.edit_tokens = self.editTokens(choice[0])
        print(self.edit_tokens)

        #display editting
        for i in range(1, len(self.edit_tokens), 2):
            display = self.edit_tokens.copy()
            editting = "_" * len(self.edit_tokens[i])
            display[i] = editting
            print("".join(display))
            self.updateToken(i)
            print(''.join(self.edit_tokens))

        return self.edit_tokens


    def editTokens(self, tokens):
        output = [' ']
        for token in tokens:
            #is bracket and previous token is bracket
            if token in ['(', ')'] and output[-1][-1] in ['(', ')'] or  output[-1] == '':
                output[-1] = output[-1] + token
            #is bracket and previous token is number or operator
            elif token in ['(', ')']:
                output.append(token)
            #is number and previous token is bracket
            elif token.isdigit() and output[-1][-1] in ['(', ')']:
                output.append(token)
            #is number and previous token is operator
            elif token.isdigit():
                output[-1] = output[-1] + token
            #is operator and previous token is number or operator
            elif output[-1][-1].isdigit() or output[-1][-1] in ['+', '-', '*', '/', '*']:
                output[-1] = output[-1] + token
            #is operator and previous token is bracket
            else:
                output.append(token)
        #drop first space
        output = output[1:]
        return output
    
    def updateToken(self, i):
            invalidFormat = True
            while invalidFormat:
                updated_tokens = input(f"Enter the updated expression this format {' '.join(['op.' if format == None else 'no.' for format in self.getTokenFormat(self.edit_tokens[i])])}: ")
                if updated_tokens != '':
                    if self.getTokenFormat(updated_tokens) == self.getTokenFormat(self.edit_tokens[i]):
                        self.edit_tokens[i] = updated_tokens
                        invalidFormat = False
                    else:
                        print("Invalid format. Please enter a valid expression.")
                else:
                    return
    
    def getTokenFormat(self, tokens):
        #print()
        #print(tokens)
        tokens = Tokeniser(tokens).partial_tokenise()
        #print(tokens)
        format = []
        for i in range(len(tokens)):
            #0 if digit, else operator
            try:
                format.append(float(tokens[i])-float(tokens[i]))
            except:
                format.append(None)
        #print(format)
        return format
        
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




print([format for format in [1, 2, 3] if format == 1])