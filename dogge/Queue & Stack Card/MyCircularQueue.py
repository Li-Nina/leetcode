class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__data = [0 for _ in range(k)]
        self.__head = -1
        self.__tail = -1
        self.__size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.__head = 0
            self.__tail = (self.__tail + 1) % self.__size
            self.__data[self.__tail] = value
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.__head == self.__tail:
            self.__head = self.__tail = -1
            return True
        else:
            self.__head = (self.__head + 1) % self.__size
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.isEmpty() else self.__data[self.__head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.isEmpty() else self.__data[self.__tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__head == -1 and self.__tail == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        tail 的下一个是 head
        """
        return (self.__tail + 1) % self.__size == self.__head

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
