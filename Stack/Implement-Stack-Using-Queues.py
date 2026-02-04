from collections import deque 

class MyStack:

    def __init__(self):
        self.q = deque()

        # Quick lookup for peek, keep track
        self.peek = 0

    # Simply add to queue
    def push(self, x: int) -> None:
        self.q.appendleft(x)
        self.peek = x

    # O(n), we simply shuffle through until we get to the leftmost
    def pop(self) -> int:
        temp = None
        for i in range(len(self.q) - 1):
            temp = self.q.pop()
            self.q.appendleft(temp)
            self.peek = temp
        return self.q.pop()
        
    def top(self) -> int:
        return self.peek

    def empty(self) -> bool:
        return len(self.q) == 0