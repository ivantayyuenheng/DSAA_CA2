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
        
    


