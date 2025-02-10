class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __lt__(self, other):
        if self.data[1] != other.data[1]:
            return self.data[1] > other.data[1]  
        return len(self.data[0]) < len(other.data[0])  

    def __str__(self):
        return str(self.data)