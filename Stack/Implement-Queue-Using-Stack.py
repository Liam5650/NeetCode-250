class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:

        # Flip the stack so we append at the back
        temp = []
        for _ in range(len(self.stack)):
            temp.append(self.stack.pop())

        # Append
        temp.append(x)

        # Flip back
        for _ in range(len(temp)):
            self.stack.append(temp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()