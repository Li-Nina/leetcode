class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_A = []  # helper stack
        self.stack_B = []  # data stack

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack_B:
            self.stack_A.append(self.stack_B.pop())
        self.stack_B.append(x)
        while self.stack_A:
            self.stack_B.append(self.stack_A.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack_B.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack_B[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_B

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
