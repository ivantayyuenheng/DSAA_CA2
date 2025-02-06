class Stack:
    def __init__(self):
        self.__list = []

    def isEmpty(self):
        return self.__list == []
    
    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
        
    def clear(self):
        self.__list.clear()
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[len(self.__list)-1]
        
    def size(self):
        return len(self.__list)
    
    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
        
    def getValues(self):
        return [self._getNodeRepresentation(node) for node in self.__list]
    def _getNodeRepresentation(self, node):
        # Helper to extract key values from BinaryTree nodes
        return f"Node(key={node.getKey()}, left={self._childKey(node.getLeftTree())}, right={self._childKey(node.getRightTree())})"

    def _childKey(self, child):
        return child.getKey() if child is not None else "None"
        
    


