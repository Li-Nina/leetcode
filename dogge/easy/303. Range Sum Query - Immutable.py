class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.memo = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.memo[i + 1] = self.memo[i] + v

    def sumRange(self, i: int, j: int) -> int:
        return self.memo[j + 1] - self.memo[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.memo)
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))
