"""
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

"""

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = []
    def next(self, val: int) -> float:
        if len(self.q) != self.size:
            self.q.append(val)
            return sum(self.q)/len(self.q)
        elif len(self.q) == self.size:
            self.q.pop(0)
            self.q.append(val)
            return sum(self.q)/self.size
