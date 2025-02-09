# Created by: IVAN TAY YUEN HENG (2335133)

from operation import BaseOperation
class DivideByTwo(BaseOperation):
    def apply(self, num):
        return num // 2 if num % 2 == 0 else None
