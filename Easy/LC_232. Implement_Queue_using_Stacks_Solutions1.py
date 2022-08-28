#232. Implement Queue using Stacks
# Easy

#Implement a first in first out (FIFO) 
# queue using only two stacks. 
# The implemented queue should support all the 
# functions of a normal queue (push, peek, pop, and empty). 


class MyQueue:
    
    def __init__(self):
        self.items1 = []
        self.items2 = []

    def push(self, x: int) -> None:
        self.items1.append(x)

    def pop(self) -> int:
        if self.items2 == []:
            while self.items1:
                self.items2.append(self.items1.pop())
        return self.items2.pop()
        

    def peek(self) -> int:
        if self.items2 == []:
            return self.items1[0]
        return self.items2[-1]

    def empty(self) -> bool:
        if self.items1 == [] and self.items2 == []:
            return True
        return False