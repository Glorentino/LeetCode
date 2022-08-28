#232. Implement Stack using Queues
# Easy
#Implement a last-in-first-out (LIFO) stack using only two queues. 
# The implemented stack should support all the 
# functions of a normal stack (push, top, pop, and empty).

class MyStack:

    def __init__(self):
        self.items = []
        
    def push(self, x: int) -> None:
        return self.items.append(x)

    def pop(self) -> int:
        if self.empty():
            return "Can pop"
        return self.items.pop()
    def top(self) -> int:
        if self.empty():
            return "No items to view"
        return self.items[len(self.items)-1]

    def empty(self) -> bool:
        if self.items == []:
            return True
        return False