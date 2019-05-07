class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queues = ([], [])
        self.cur_point = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        other_point = (self.cur_point + 1) % 2
        queue_cur = self.queues[self.cur_point]
        queue_other = self.queues[other_point]

        queue_other.insert(0, x)
        while queue_cur:
            queue_other.insert(0, queue_cur.pop())
        self.cur_point = other_point

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queues[self.cur_point].pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queues[self.cur_point][-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queues[self.cur_point]

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
