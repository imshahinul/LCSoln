class MyQueue:

    def __init__(self):
        self.receive = []
        self.broadcast = []

    def push(self, x: int) -> None:
        self.receive.append(x)

    def pop(self) -> int:
        self.peek()
        return self.broadcast.pop()

    def peek(self) -> int:
        if not self.broadcast:
            while self.receive:
                self.broadcast.append(self.receive.pop())
        return self.broadcast[-1]

    def empty(self) -> bool:
        return not self.receive and not self.broadcast

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()