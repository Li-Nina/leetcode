import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data = []
        self.__min = sys.maxsize

    def push(self, x: int) -> None:
        if self.__min >= x:
            # store the last min num
            self.__data.append(self.__min)
            self.__min = x
        self.__data.append(x)

    def pop(self) -> None:
        if self.__data.pop() == self.__min:
            self.__min = self.__data.pop()

    def top(self) -> int:
        return self.__data[-1]

    def getMin(self) -> int:
        return self.__min

    def getData(self):
        return self.__data


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    obj = MinStack()
    obj.push(7)
    obj.push(8)
    obj.push(5)
    obj.push(9)
    obj.push(1)
    print(obj.getData())
    print(obj.getMin())
    obj.pop()
    print(obj.getData())
    print(obj.getMin())
    obj.pop()
    print(obj.getData())
    print(obj.getMin())
