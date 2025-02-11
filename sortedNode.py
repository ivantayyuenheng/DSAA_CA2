# Created by IVAN TAY YUEN HENG (2335133)
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __lt__(self, other):
        if self.data[1] != other.data[1]:
            return self.data[1] > other.data[1]  
        if self.data[0] != other.data[0]:
            return len(self.data[0]) < len(other.data[0])  
        return self.data[0].count('(') + self.data[0].count(')') < other.data[0].count('(') + other.data[0].count(')') 

    def __str__(self):
        return str(self.data)