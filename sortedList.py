# Created by: IVAN TAY YUEN HENG (2335133) and CHAN JUN YI (2309347)

class SortedList:
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode

    def insert(self, newNode):
        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return
    
        # Check if it is going to be new head
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return
        
        # Traverse and insert at appropriate location
        node = self.headNode

        while node.nextNode != None and not (newNode < node.nextNode):
            node = node.nextNode
        
        newNode.nextNode = node.nextNode
        node.nextNode = newNode
        
    
    def __str__(self):
        group = {}
        node = self.headNode

        while node != None:
            value = node.data[1]
            if value not in group:
                group[value] = []
            group[value].append(node.data[0])
            node = node.nextNode

        # Output
        output = []

        for key in sorted(group.keys(), reverse=True):
            output.append(f"*** Expressions with value= {key}")
            for value in group[key]:
                output.append(f"{value}==>{key}")

            output.append("")

        return "\n".join(output)