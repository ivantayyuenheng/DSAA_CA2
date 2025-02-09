from operation import BaseOperation

class AddOne(BaseOperation):
    def apply(self, num):
        return num + 1
